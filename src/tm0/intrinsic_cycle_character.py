"""Derive a basis-independent state character from cycle-rank loss.

Fundamental-cycle coordinates depend on a selected spanning forest.

This scaffold removes that coordinate dependence by asking an intrinsic
question for each state:

    how much undirected cycle rank is lost when this state is removed?

For each state, the system derives:

    total graph cycle rank
    cycle rank after state deletion
    cycle-rank loss
    whether the state carries cycle structure

The resulting character is independent of the chosen spanning forest.

Directed motion rules remain distinct undirected edges for cycle-rank
calculation.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Tuple

from .derived_body_candidate import StateCharacterMap
from .derived_boundary_contact import MotionRule
from .derived_fundamental_cycle_character import undirected_cycle_rank
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import validate_motion_graph


StateName = str


@dataclass(frozen=True)
class IntrinsicCycleSignature:
    state: StateName
    total_cycle_rank: int
    deleted_cycle_rank: int
    cycle_rank_loss: int
    carries_cycle_structure: bool

    @property
    def character(self) -> Tuple[int, ...]:
        return tuple(
            int(self.cycle_rank_loss >= threshold)
            for threshold in range(
                1,
                self.total_cycle_rank + 1,
            )
        )


def graph_without_state(
    graph: MotionGraph,
    removed_state: StateName,
) -> MotionGraph:
    validate_motion_graph(graph)

    if removed_state not in graph.states:
        raise ValueError("removed state is not registered")

    remaining_states = tuple(
        state
        for state in graph.states
        if state != removed_state
    )

    remaining_rules = tuple(
        rule
        for rule in graph.rules
        if (
            rule.source_state != removed_state
            and rule.target_state != removed_state
        )
    )

    if not remaining_states:
        raise ValueError(
            "state deletion leaves no motion graph"
        )

    if not remaining_rules:
        return MotionGraph(
            states=remaining_states,
            rules=(
                MotionRule(
                    source_state=remaining_states[0],
                    target_state=remaining_states[0],
                    relation_name=(
                        "__rank_zero_placeholder__"
                    ),
                ),
            ),
        )

    return MotionGraph(
        states=remaining_states,
        rules=remaining_rules,
    )


def cycle_rank_after_state_deletion(
    graph: MotionGraph,
    removed_state: StateName,
) -> int:
    reduced = graph_without_state(
        graph,
        removed_state,
    )

    if (
        len(reduced.rules) == 1
        and reduced.rules[0].relation_name
        == "__rank_zero_placeholder__"
    ):
        return 0

    return undirected_cycle_rank(reduced)


def derive_intrinsic_cycle_signature(
    graph: MotionGraph,
    state: StateName,
) -> IntrinsicCycleSignature:
    validate_motion_graph(graph)

    if state not in graph.states:
        raise ValueError("state is not registered")

    total_rank = undirected_cycle_rank(graph)

    deleted_rank = cycle_rank_after_state_deletion(
        graph,
        state,
    )

    rank_loss = total_rank - deleted_rank

    if rank_loss < 0:
        raise ValueError(
            "state deletion increased cycle rank unexpectedly"
        )

    return IntrinsicCycleSignature(
        state=state,
        total_cycle_rank=total_rank,
        deleted_cycle_rank=deleted_rank,
        cycle_rank_loss=rank_loss,
        carries_cycle_structure=rank_loss > 0,
    )


def derive_intrinsic_cycle_character_field(
    graph: MotionGraph,
) -> StateCharacterMap:
    validate_motion_graph(graph)

    field: StateCharacterMap = {}

    for state in graph.states:
        signature = derive_intrinsic_cycle_signature(
            graph,
            state,
        )

        field[state] = signature.character

    return field


def states_without_intrinsic_cycle_structure(
    graph: MotionGraph,
) -> Tuple[StateName, ...]:
    field = derive_intrinsic_cycle_character_field(
        graph
    )

    return tuple(
        sorted(
            state
            for state, character in field.items()
            if character[0] == 0
        )
    )
