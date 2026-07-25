"""Separate step trace from path-earned return receipt.

A step event records only what one executed transition realizes:

    source state
    target state
    traversed relation
    boundary contacts

A path receipt records what can only be known after multiple steps:

    ordered step events
    visited states
    final state
    return status
    derived traversal residue

Cycle residue is not stored on individual transition rules or step
events in this scaffold.
"""

from dataclasses import dataclass
from typing import Tuple


StateName = str
RelationName = str
BoundaryContacts = Tuple[str, ...]
RelationRequests = Tuple[str, ...]
TraversalResidue = Tuple[int, ...]


@dataclass(frozen=True)
class StepRule:
    source_state: StateName
    target_state: StateName
    relation_name: RelationName
    boundary_contacts: BoundaryContacts


@dataclass(frozen=True)
class StepSystem:
    states: Tuple[StateName, ...]
    rules: Tuple[StepRule, ...]


@dataclass(frozen=True)
class StepEvent:
    source_state: StateName
    target_state: StateName
    traversed_relation: RelationName
    boundary_contacts: BoundaryContacts


@dataclass(frozen=True)
class PathReceipt:
    initial_state: StateName
    final_state: StateName
    step_events: Tuple[StepEvent, ...]
    visited_states: Tuple[StateName, ...]
    traversed_relations: Tuple[RelationName, ...]
    returned: bool
    traversal_residue: TraversalResidue


def validate_step_rule(
    rule: StepRule,
) -> StepRule:
    if not rule.source_state:
        raise ValueError("source state must not be empty")

    if not rule.target_state:
        raise ValueError("target state must not be empty")

    if not rule.relation_name:
        raise ValueError("relation name must not be empty")

    if not rule.boundary_contacts:
        raise ValueError("boundary contacts must not be empty")

    if any(not contact for contact in rule.boundary_contacts):
        raise ValueError("boundary contacts must not contain empty values")

    if len(set(rule.boundary_contacts)) != len(
        rule.boundary_contacts
    ):
        raise ValueError("boundary contacts must be unique")

    return rule


def validate_step_system(
    system: StepSystem,
) -> StepSystem:
    if not system.states:
        raise ValueError("step system must contain states")

    if any(not state for state in system.states):
        raise ValueError("state names must not be empty")

    if len(set(system.states)) != len(system.states):
        raise ValueError("state names must be unique")

    if not system.rules:
        raise ValueError("step system must contain rules")

    relation_names = tuple(
        rule.relation_name
        for rule in system.rules
    )

    if len(set(relation_names)) != len(relation_names):
        raise ValueError("relation names must be unique")

    known_states = set(system.states)

    for rule in system.rules:
        validate_step_rule(rule)

        if rule.source_state not in known_states:
            raise ValueError("rule source state is not registered")

        if rule.target_state not in known_states:
            raise ValueError("rule target state is not registered")

    return system


def step_rule_by_name(
    system: StepSystem,
    relation_name: RelationName,
) -> StepRule:
    validate_step_system(system)

    for rule in system.rules:
        if rule.relation_name == relation_name:
            return rule

    raise ValueError("requested relation is not registered")


def execute_step(
    system: StepSystem,
    current_state: StateName,
    relation_name: RelationName,
) -> StepEvent:
    validate_step_system(system)

    if current_state not in system.states:
        raise ValueError("current state is not registered")

    rule = step_rule_by_name(
        system,
        relation_name,
    )

    if rule.source_state != current_state:
        raise ValueError(
            "requested relation is not lawful from current state"
        )

    return StepEvent(
        source_state=rule.source_state,
        target_state=rule.target_state,
        traversed_relation=rule.relation_name,
        boundary_contacts=rule.boundary_contacts,
    )


def derive_path_residue(
    system: StepSystem,
    traversed_relations: Tuple[RelationName, ...],
) -> TraversalResidue:
    validate_step_system(system)

    known_relations = tuple(
        rule.relation_name
        for rule in system.rules
    )

    unknown = set(traversed_relations) - set(known_relations)

    if unknown:
        raise ValueError("traversed relation is not registered")

    return tuple(
        traversed_relations.count(relation_name) % 2
        for relation_name in known_relations
    )


def execute_path(
    system: StepSystem,
    initial_state: StateName,
    relation_requests: RelationRequests,
) -> PathReceipt:
    validate_step_system(system)

    if initial_state not in system.states:
        raise ValueError("initial state is not registered")

    if not relation_requests:
        raise ValueError("path must request at least one relation")

    current_state = initial_state
    events = []
    visited_states = [initial_state]
    traversed_relations = []

    for relation_name in relation_requests:
        event = execute_step(
            system=system,
            current_state=current_state,
            relation_name=relation_name,
        )

        events.append(event)
        traversed_relations.append(
            event.traversed_relation
        )

        current_state = event.target_state
        visited_states.append(current_state)

    traversed_tuple = tuple(traversed_relations)

    return PathReceipt(
        initial_state=initial_state,
        final_state=current_state,
        step_events=tuple(events),
        visited_states=tuple(visited_states),
        traversed_relations=traversed_tuple,
        returned=current_state == initial_state,
        traversal_residue=derive_path_residue(
            system,
            traversed_tuple,
        ),
    )
