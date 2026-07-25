"""Derive state character from mutual return structure.

Two states belong to the same return class when each is reachable from
the other through directed motion.

Return classes are the strongly connected components of the motion
graph.

Each state receives a canonical one-hot character identifying its
return class.

The character field is therefore derived from lawful return structure
rather than assigned directly.

This is a bounded return-character scaffold.
"""

from typing import Dict
from typing import List
from typing import Set
from typing import Tuple

from .derived_body_candidate import StateCharacterMap
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import validate_motion_graph


StateName = str
ReturnClass = Tuple[StateName, ...]
ReturnClasses = Tuple[ReturnClass, ...]


def directed_adjacency(
    graph: MotionGraph,
) -> Dict[StateName, Tuple[StateName, ...]]:
    validate_motion_graph(graph)

    adjacency = {
        state: []
        for state in graph.states
    }

    for rule in graph.rules:
        adjacency[rule.source_state].append(
            rule.target_state
        )

    return {
        state: tuple(sorted(targets))
        for state, targets in adjacency.items()
    }


def reverse_directed_adjacency(
    graph: MotionGraph,
) -> Dict[StateName, Tuple[StateName, ...]]:
    validate_motion_graph(graph)

    adjacency = {
        state: []
        for state in graph.states
    }

    for rule in graph.rules:
        adjacency[rule.target_state].append(
            rule.source_state
        )

    return {
        state: tuple(sorted(sources))
        for state, sources in adjacency.items()
    }


def finishing_order(
    graph: MotionGraph,
) -> Tuple[StateName, ...]:
    adjacency = directed_adjacency(graph)
    visited: Set[StateName] = set()
    finished: List[StateName] = []

    def visit(state: StateName) -> None:
        if state in visited:
            return

        visited.add(state)

        for target in adjacency[state]:
            visit(target)

        finished.append(state)

    for state in sorted(graph.states):
        visit(state)

    return tuple(finished)


def derive_return_classes(
    graph: MotionGraph,
) -> ReturnClasses:
    validate_motion_graph(graph)

    reverse_adjacency = reverse_directed_adjacency(graph)
    order = tuple(reversed(finishing_order(graph)))
    assigned: Set[StateName] = set()
    components = []

    def collect(
        state: StateName,
        component: Set[StateName],
    ) -> None:
        if state in assigned:
            return

        assigned.add(state)
        component.add(state)

        for source in reverse_adjacency[state]:
            collect(source, component)

    for state in order:
        if state in assigned:
            continue

        component: Set[StateName] = set()
        collect(state, component)
        components.append(tuple(sorted(component)))

    return tuple(
        sorted(
            components,
            key=lambda component: component,
        )
    )


def derive_return_character_field(
    graph: MotionGraph,
) -> StateCharacterMap:
    classes = derive_return_classes(graph)

    field: StateCharacterMap = {}

    for class_index, return_class in enumerate(classes):
        character = tuple(
            int(index == class_index)
            for index in range(len(classes))
        )

        for state in return_class:
            field[state] = character

    return field
