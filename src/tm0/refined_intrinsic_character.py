"""Refine intrinsic character with state-deletion damage profiles.

Cycle-rank loss is basis-independent but coarse.

This scaffold derives a richer perturbation signature for each state:

    cycle-rank loss
    increase in undirected component count
    surviving directed return-class count
    largest surviving return-class size

Each scalar is encoded as a fixed-width unary binary block.

The concatenated blocks form a basis-independent binary character field
compatible with the body and thalion pipeline.

State deletion is a structural probe, not an executed transition.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Set
from typing import Tuple

from .derived_body_candidate import StateCharacterMap
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import validate_motion_graph
from .derived_return_character import derive_return_classes
from .intrinsic_cycle_character import graph_without_state
from .intrinsic_cycle_character import undirected_cycle_rank


StateName = str


@dataclass(frozen=True)
class PerturbationSignature:
    state: StateName
    cycle_rank_loss: int
    component_gain: int
    surviving_return_class_count: int
    largest_surviving_return_class_size: int


def undirected_component_count(
    graph: MotionGraph,
) -> int:
    validate_motion_graph(graph)

    adjacency = {
        state: set()
        for state in graph.states
    }

    for rule in graph.rules:
        adjacency[rule.source_state].add(
            rule.target_state
        )
        adjacency[rule.target_state].add(
            rule.source_state
        )

    visited: Set[StateName] = set()
    component_count = 0

    for start in sorted(graph.states):
        if start in visited:
            continue

        component_count += 1
        frontier = [start]
        visited.add(start)

        while frontier:
            current = frontier.pop()

            for neighbor in adjacency[current]:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                frontier.append(neighbor)

    return component_count


def is_rank_zero_placeholder_graph(
    graph: MotionGraph,
) -> bool:
    return (
        len(graph.rules) == 1
        and graph.rules[0].relation_name
        == "__rank_zero_placeholder__"
    )


def reduced_cycle_rank(
    graph: MotionGraph,
) -> int:
    if is_rank_zero_placeholder_graph(graph):
        return 0

    return undirected_cycle_rank(graph)


def reduced_return_classes(
    graph: MotionGraph,
) -> Tuple[Tuple[StateName, ...], ...]:
    if is_rank_zero_placeholder_graph(graph):
        return tuple(
            (state,)
            for state in sorted(graph.states)
        )

    return derive_return_classes(graph)


def derive_perturbation_signature(
    graph: MotionGraph,
    state: StateName,
) -> PerturbationSignature:
    validate_motion_graph(graph)

    if state not in graph.states:
        raise ValueError("state is not registered")

    total_cycle_rank = undirected_cycle_rank(graph)
    original_component_count = undirected_component_count(
        graph
    )

    reduced = graph_without_state(
        graph,
        state,
    )

    deleted_cycle_rank = reduced_cycle_rank(
        reduced
    )

    deleted_component_count = undirected_component_count(
        reduced
    )

    return_classes = reduced_return_classes(
        reduced
    )

    largest_return_class_size = max(
        len(return_class)
        for return_class in return_classes
    )

    return PerturbationSignature(
        state=state,
        cycle_rank_loss=(
            total_cycle_rank - deleted_cycle_rank
        ),
        component_gain=max(
            0,
            deleted_component_count
            - original_component_count,
        ),
        surviving_return_class_count=len(
            return_classes
        ),
        largest_surviving_return_class_size=(
            largest_return_class_size
        ),
    )


def unary_block(
    value: int,
    width: int,
) -> Tuple[int, ...]:
    if value < 0:
        raise ValueError("unary value must not be negative")

    if width < 0:
        raise ValueError("unary width must not be negative")

    if value > width:
        raise ValueError("unary value exceeds width")

    return tuple(
        int(index < value)
        for index in range(width)
    )


def derive_refined_intrinsic_character_field(
    graph: MotionGraph,
) -> StateCharacterMap:
    validate_motion_graph(graph)

    signatures = tuple(
        derive_perturbation_signature(
            graph,
            state,
        )
        for state in graph.states
    )

    rank_width = max(
        signature.cycle_rank_loss
        for signature in signatures
    )

    component_width = max(
        signature.component_gain
        for signature in signatures
    )

    return_class_width = max(
        signature.surviving_return_class_count
        for signature in signatures
    )

    largest_class_width = max(
        signature.largest_surviving_return_class_size
        for signature in signatures
    )

    field: StateCharacterMap = {}

    for signature in signatures:
        field[signature.state] = (
            *unary_block(
                signature.cycle_rank_loss,
                rank_width,
            ),
            *unary_block(
                signature.component_gain,
                component_width,
            ),
            *unary_block(
                signature.surviving_return_class_count,
                return_class_width,
            ),
            *unary_block(
                signature.largest_surviving_return_class_size,
                largest_class_width,
            ),
        )

    return field


def perturbation_signatures(
    graph: MotionGraph,
) -> Dict[StateName, PerturbationSignature]:
    validate_motion_graph(graph)

    return {
        state: derive_perturbation_signature(
            graph,
            state,
        )
        for state in graph.states
    }
