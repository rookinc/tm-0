"""Execute a lawful transition and emit a realized event.

A minimal transition system contains explicit directed relations.

Each relation records:

    source state
    target state
    relation name
    boundary contacts
    cycle residue

Execution succeeds only when the requested relation begins at the
current state.

A successful step returns both the next state and the realized event
record required by the witness-context layer.

This is a bounded transition-execution scaffold.
"""

from dataclasses import dataclass
from typing import Tuple

from .realized_event_context import RealizedEvent
from .realized_event_context import validate_realized_event


StateName = str
RelationName = str
BoundaryContacts = Tuple[str, ...]
CycleResidue = Tuple[int, ...]


@dataclass(frozen=True)
class TransitionRule:
    source_state: StateName
    target_state: StateName
    relation_name: RelationName
    boundary_contacts: BoundaryContacts
    cycle_residue: CycleResidue


@dataclass(frozen=True)
class TransitionSystem:
    states: Tuple[StateName, ...]
    rules: Tuple[TransitionRule, ...]


@dataclass(frozen=True)
class StepResult:
    prior_state: StateName
    next_state: StateName
    rule: TransitionRule
    event: RealizedEvent


def validate_transition_rule(
    rule: TransitionRule,
) -> TransitionRule:
    event = RealizedEvent(
        source_state=rule.source_state,
        target_state=rule.target_state,
        traversed_relation=rule.relation_name,
        boundary_contacts=rule.boundary_contacts,
        cycle_residue=rule.cycle_residue,
    )

    validate_realized_event(event)

    return rule


def validate_transition_system(
    system: TransitionSystem,
) -> TransitionSystem:
    if not system.states:
        raise ValueError("transition system must contain states")

    if any(not state for state in system.states):
        raise ValueError("state names must not be empty")

    if len(set(system.states)) != len(system.states):
        raise ValueError("state names must be unique")

    if not system.rules:
        raise ValueError("transition system must contain rules")

    relation_names = tuple(
        rule.relation_name
        for rule in system.rules
    )

    if len(set(relation_names)) != len(relation_names):
        raise ValueError("relation names must be unique")

    known_states = set(system.states)

    for rule in system.rules:
        validate_transition_rule(rule)

        if rule.source_state not in known_states:
            raise ValueError("rule source state is not registered")

        if rule.target_state not in known_states:
            raise ValueError("rule target state is not registered")

    return system


def rule_by_name(
    system: TransitionSystem,
    relation_name: RelationName,
) -> TransitionRule:
    validate_transition_system(system)

    for rule in system.rules:
        if rule.relation_name == relation_name:
            return rule

    raise ValueError("requested relation is not registered")


def execute_transition(
    system: TransitionSystem,
    current_state: StateName,
    relation_name: RelationName,
) -> StepResult:
    validate_transition_system(system)

    if current_state not in system.states:
        raise ValueError("current state is not registered")

    rule = rule_by_name(
        system,
        relation_name,
    )

    if rule.source_state != current_state:
        raise ValueError(
            "requested relation is not lawful from current state"
        )

    event = RealizedEvent(
        source_state=rule.source_state,
        target_state=rule.target_state,
        traversed_relation=rule.relation_name,
        boundary_contacts=rule.boundary_contacts,
        cycle_residue=rule.cycle_residue,
    )

    validate_realized_event(event)

    return StepResult(
        prior_state=current_state,
        next_state=rule.target_state,
        rule=rule,
        event=event,
    )
