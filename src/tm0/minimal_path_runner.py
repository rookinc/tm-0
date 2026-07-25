"""Run an ordered transition path and derive return residue.

A path begins at one registered state and executes an ordered sequence
of named relations.

The runner records:

    initial state
    realized step sequence
    visited states
    traversed relations
    final state
    whether the path returned

Cycle residue is derived from traversal history rather than copied from
one transition rule.

For each registered relation, the residue records traversal parity:

    0 means traversed an even number of times
    1 means traversed an odd number of times

This is a bounded path-execution scaffold.
"""

from dataclasses import dataclass
from typing import Tuple

from .minimal_transition_executor import StepResult
from .minimal_transition_executor import TransitionSystem
from .minimal_transition_executor import execute_transition
from .minimal_transition_executor import validate_transition_system


RelationRequests = Tuple[str, ...]
VisitedStates = Tuple[str, ...]
TraversedRelations = Tuple[str, ...]
TraversalResidue = Tuple[int, ...]


@dataclass(frozen=True)
class PathResult:
    initial_state: str
    final_state: str
    steps: Tuple[StepResult, ...]
    visited_states: VisitedStates
    traversed_relations: TraversedRelations
    returned: bool
    traversal_residue: TraversalResidue


def derive_traversal_residue(
    system: TransitionSystem,
    traversed_relations: TraversedRelations,
) -> TraversalResidue:
    validate_transition_system(system)

    known_relations = tuple(
        rule.relation_name
        for rule in system.rules
    )

    unknown = set(traversed_relations) - set(known_relations)

    if unknown:
        raise ValueError(
            "traversed relation is not registered"
        )

    return tuple(
        traversed_relations.count(relation_name) % 2
        for relation_name in known_relations
    )


def run_transition_path(
    system: TransitionSystem,
    initial_state: str,
    relation_requests: RelationRequests,
) -> PathResult:
    validate_transition_system(system)

    if initial_state not in system.states:
        raise ValueError("initial state is not registered")

    if not relation_requests:
        raise ValueError("path must request at least one relation")

    current_state = initial_state
    steps = []
    visited_states = [initial_state]
    traversed_relations = []

    for relation_name in relation_requests:
        step = execute_transition(
            system=system,
            current_state=current_state,
            relation_name=relation_name,
        )

        steps.append(step)
        traversed_relations.append(
            step.event.traversed_relation
        )

        current_state = step.next_state
        visited_states.append(current_state)

    traversed_tuple = tuple(traversed_relations)

    return PathResult(
        initial_state=initial_state,
        final_state=current_state,
        steps=tuple(steps),
        visited_states=tuple(visited_states),
        traversed_relations=traversed_tuple,
        returned=current_state == initial_state,
        traversal_residue=derive_traversal_residue(
            system,
            traversed_tuple,
        ),
    )
