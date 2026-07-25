"""Execute motion with runtime-derived boundary contact.

A motion rule contains only lawful movement:

    source state
    target state
    relation name

A boundary is registered separately.

Execution derives boundary contact at runtime and emits a
boundary-aware step event.

A path receipt accumulates those events and derives return residue from
the executed relation history.
"""

from dataclasses import dataclass
from typing import Tuple

from .derived_boundary_contact import Boundary
from .derived_boundary_contact import BoundaryContact
from .derived_boundary_contact import MotionRule
from .derived_boundary_contact import derive_boundary_contact
from .derived_boundary_contact import validate_boundary
from .derived_boundary_contact import validate_motion_rule


StateName = str
RelationName = str
RelationRequests = Tuple[RelationName, ...]
TraversalResidue = Tuple[int, ...]


@dataclass(frozen=True)
class BoundaryAwareSystem:
    states: Tuple[StateName, ...]
    rules: Tuple[MotionRule, ...]
    boundary: Boundary


@dataclass(frozen=True)
class BoundaryAwareStepEvent:
    source_state: StateName
    target_state: StateName
    traversed_relation: RelationName
    boundary_contact: BoundaryContact


@dataclass(frozen=True)
class BoundaryAwarePathReceipt:
    initial_state: StateName
    final_state: StateName
    step_events: Tuple[BoundaryAwareStepEvent, ...]
    visited_states: Tuple[StateName, ...]
    traversed_relations: Tuple[RelationName, ...]
    returned: bool
    traversal_residue: TraversalResidue


def validate_boundary_aware_system(
    system: BoundaryAwareSystem,
) -> BoundaryAwareSystem:
    if not system.states:
        raise ValueError("system must contain states")

    if any(not state for state in system.states):
        raise ValueError("state names must not be empty")

    if len(set(system.states)) != len(system.states):
        raise ValueError("state names must be unique")

    if not system.rules:
        raise ValueError("system must contain motion rules")

    relation_names = tuple(
        rule.relation_name
        for rule in system.rules
    )

    if len(set(relation_names)) != len(relation_names):
        raise ValueError("relation names must be unique")

    known_states = set(system.states)

    for rule in system.rules:
        validate_motion_rule(rule)

        if rule.source_state not in known_states:
            raise ValueError("rule source state is not registered")

        if rule.target_state not in known_states:
            raise ValueError("rule target state is not registered")

    validate_boundary(system.boundary)

    unknown_inside_states = (
        set(system.boundary.inside_states) - known_states
    )

    if unknown_inside_states:
        raise ValueError(
            "boundary contains unregistered inside states"
        )

    unknown_boundary_relations = (
        set(system.boundary.boundary_relations)
        - set(relation_names)
    )

    if unknown_boundary_relations:
        raise ValueError(
            "boundary contains unregistered relations"
        )

    return system


def motion_rule_by_name(
    system: BoundaryAwareSystem,
    relation_name: RelationName,
) -> MotionRule:
    validate_boundary_aware_system(system)

    for rule in system.rules:
        if rule.relation_name == relation_name:
            return rule

    raise ValueError("requested relation is not registered")


def execute_boundary_aware_step(
    system: BoundaryAwareSystem,
    current_state: StateName,
    relation_name: RelationName,
) -> BoundaryAwareStepEvent:
    validate_boundary_aware_system(system)

    if current_state not in system.states:
        raise ValueError("current state is not registered")

    rule = motion_rule_by_name(
        system,
        relation_name,
    )

    if rule.source_state != current_state:
        raise ValueError(
            "requested relation is not lawful from current state"
        )

    contact = derive_boundary_contact(
        rule,
        system.boundary,
    )

    return BoundaryAwareStepEvent(
        source_state=rule.source_state,
        target_state=rule.target_state,
        traversed_relation=rule.relation_name,
        boundary_contact=contact,
    )


def derive_boundary_aware_path_residue(
    system: BoundaryAwareSystem,
    traversed_relations: Tuple[RelationName, ...],
) -> TraversalResidue:
    validate_boundary_aware_system(system)

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


def execute_boundary_aware_path(
    system: BoundaryAwareSystem,
    initial_state: StateName,
    relation_requests: RelationRequests,
) -> BoundaryAwarePathReceipt:
    validate_boundary_aware_system(system)

    if initial_state not in system.states:
        raise ValueError("initial state is not registered")

    if not relation_requests:
        raise ValueError("path must request at least one relation")

    current_state = initial_state
    step_events = []
    visited_states = [initial_state]
    traversed_relations = []

    for relation_name in relation_requests:
        event = execute_boundary_aware_step(
            system=system,
            current_state=current_state,
            relation_name=relation_name,
        )

        step_events.append(event)
        traversed_relations.append(
            event.traversed_relation
        )

        current_state = event.target_state
        visited_states.append(current_state)

    traversed_tuple = tuple(traversed_relations)

    return BoundaryAwarePathReceipt(
        initial_state=initial_state,
        final_state=current_state,
        step_events=tuple(step_events),
        visited_states=tuple(visited_states),
        traversed_relations=traversed_tuple,
        returned=current_state == initial_state,
        traversal_residue=derive_boundary_aware_path_residue(
            system,
            traversed_tuple,
        ),
    )
