"""Derive state character from directed cycle participation.

The motion graph is searched for simple directed cycles.

Each cycle is normalized by cyclic rotation while preserving direction.

The canonical cycle order defines character coordinates.

A state's binary character records whether that state participates in
each directed cycle.

This refines mutual-return class identity by preserving differences in
local cycle participation.

The exhaustive cycle search is intended only for small graphs.
"""

from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Set
from typing import Tuple

from .derived_body_candidate import StateCharacterMap
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import validate_motion_graph


StateName = str
RelationName = str


@dataclass(frozen=True)
class DirectedCycle:
    states: Tuple[StateName, ...]
    relations: Tuple[RelationName, ...]

    @property
    def length(self) -> int:
        return len(self.relations)


def normalize_directed_cycle(
    states: Tuple[StateName, ...],
    relations: Tuple[RelationName, ...],
) -> DirectedCycle:
    if not relations:
        raise ValueError("cycle must contain relations")

    if len(states) != len(relations):
        raise ValueError(
            "cycle state and relation counts must match"
        )

    rotations = []

    for index in range(len(relations)):
        rotated_states = (
            states[index:]
            + states[:index]
        )

        rotated_relations = (
            relations[index:]
            + relations[:index]
        )

        rotations.append(
            (
                rotated_relations,
                rotated_states,
            )
        )

    normalized_relations, normalized_states = min(
        rotations
    )

    return DirectedCycle(
        states=normalized_states,
        relations=normalized_relations,
    )


def outgoing_rules_by_state(
    graph: MotionGraph,
):
    validate_motion_graph(graph)

    outgoing = {
        state: []
        for state in graph.states
    }

    for rule in graph.rules:
        outgoing[rule.source_state].append(rule)

    return {
        state: tuple(
            sorted(
                rules,
                key=lambda rule: (
                    rule.relation_name,
                    rule.target_state,
                ),
            )
        )
        for state, rules in outgoing.items()
    }


def enumerate_simple_directed_cycles(
    graph: MotionGraph,
) -> Tuple[DirectedCycle, ...]:
    validate_motion_graph(graph)

    outgoing = outgoing_rules_by_state(graph)
    found: Dict[
        Tuple[RelationName, ...],
        DirectedCycle,
    ] = {}

    def search(
        start: StateName,
        current: StateName,
        state_path: Tuple[StateName, ...],
        relation_path: Tuple[RelationName, ...],
        visited_states: Set[StateName],
    ) -> None:
        for rule in outgoing[current]:
            target = rule.target_state

            if target == start:
                cycle = normalize_directed_cycle(
                    states=state_path,
                    relations=(
                        *relation_path,
                        rule.relation_name,
                    ),
                )

                found[cycle.relations] = cycle
                continue

            if target in visited_states:
                continue

            search(
                start=start,
                current=target,
                state_path=(
                    *state_path,
                    target,
                ),
                relation_path=(
                    *relation_path,
                    rule.relation_name,
                ),
                visited_states=(
                    visited_states | {target}
                ),
            )

    for start in sorted(graph.states):
        search(
            start=start,
            current=start,
            state_path=(start,),
            relation_path=(),
            visited_states={start},
        )

    return tuple(
        found[key]
        for key in sorted(found)
    )


def derive_cycle_participation_character_field(
    graph: MotionGraph,
) -> StateCharacterMap:
    cycles = enumerate_simple_directed_cycles(graph)

    if not cycles:
        raise ValueError(
            "motion graph contains no directed cycles"
        )

    field: StateCharacterMap = {}

    for state in graph.states:
        field[state] = tuple(
            int(state in cycle.states)
            for cycle in cycles
        )

    return field


def states_without_cycle_participation(
    graph: MotionGraph,
) -> Tuple[StateName, ...]:
    field = derive_cycle_participation_character_field(
        graph
    )

    return tuple(
        sorted(
            state
            for state, character in field.items()
            if not any(character)
        )
    )
