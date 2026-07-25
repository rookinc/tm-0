"""Derive minimal body candidates from graph and character structure.

A body candidate is a state region that is:

    nonempty
    connected
    internally character-preserving
    bounded by at least one graph cut

Character is assigned to states.

An internal relation preserves character when its source and target
states carry the same character value.

The search enumerates connected state subsets and returns the minimal
passing candidates.

This is a bounded body-derivation scaffold.
"""

from dataclasses import dataclass
from itertools import combinations
from typing import Dict
from typing import Tuple

from .derived_region_boundary import DerivedRegionBoundary
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import derive_region_boundary
from .derived_region_boundary import region_is_connected
from .derived_region_boundary import validate_motion_graph


StateName = str
CharacterValue = Tuple[int, ...]
StateCharacterMap = Dict[StateName, CharacterValue]
RegionStates = Tuple[StateName, ...]


@dataclass(frozen=True)
class BodyCandidate:
    states: RegionStates
    character: CharacterValue
    boundary: DerivedRegionBoundary


def validate_character_value(
    character: CharacterValue,
) -> CharacterValue:
    if not character:
        raise ValueError("character must not be empty")

    if any(bit not in (0, 1) for bit in character):
        raise ValueError("character must be binary")

    return character


def validate_state_characters(
    graph: MotionGraph,
    state_characters: StateCharacterMap,
) -> StateCharacterMap:
    validate_motion_graph(graph)

    graph_states = set(graph.states)
    character_states = set(state_characters)

    if character_states != graph_states:
        raise ValueError(
            "state character map must cover exactly the graph states"
        )

    for character in state_characters.values():
        validate_character_value(character)

    character_lengths = {
        len(character)
        for character in state_characters.values()
    }

    if len(character_lengths) != 1:
        raise ValueError(
            "all state characters must have equal length"
        )

    return state_characters


def region_character(
    region_states: RegionStates,
    state_characters: StateCharacterMap,
) -> CharacterValue:
    if not region_states:
        raise ValueError("region must contain states")

    characters = {
        state_characters[state]
        for state in region_states
    }

    if len(characters) != 1:
        raise ValueError(
            "region does not carry one preserved character"
        )

    return next(iter(characters))


def internal_relations_preserve_character(
    graph: MotionGraph,
    region_states: RegionStates,
    state_characters: StateCharacterMap,
) -> bool:
    validate_state_characters(
        graph,
        state_characters,
    )

    inside = set(region_states)

    if not inside:
        return False

    if not inside.issubset(set(graph.states)):
        return False

    for rule in graph.rules:
        source_inside = rule.source_state in inside
        target_inside = rule.target_state in inside

        if source_inside and target_inside:
            if (
                state_characters[rule.source_state]
                != state_characters[rule.target_state]
            ):
                return False

    return True


def derive_body_candidate(
    graph: MotionGraph,
    region_states: RegionStates,
    state_characters: StateCharacterMap,
    region_name: str = "body-candidate",
) -> BodyCandidate:
    validate_state_characters(
        graph,
        state_characters,
    )

    if not region_states:
        raise ValueError("region must contain states")

    if len(set(region_states)) != len(region_states):
        raise ValueError("region states must be unique")

    if not region_is_connected(
        graph,
        region_states,
    ):
        raise ValueError("body candidate must be connected")

    if not internal_relations_preserve_character(
        graph,
        region_states,
        state_characters,
    ):
        raise ValueError(
            "body candidate must preserve character internally"
        )

    character = region_character(
        region_states,
        state_characters,
    )

    boundary = derive_region_boundary(
        graph=graph,
        region_name=region_name,
        region_states=region_states,
    )

    if not boundary.boundary_relations:
        raise ValueError(
            "body candidate must have a nonempty boundary cut"
        )

    return BodyCandidate(
        states=boundary.inside_states,
        character=character,
        boundary=boundary,
    )


def enumerate_body_candidates(
    graph: MotionGraph,
    state_characters: StateCharacterMap,
) -> Tuple[BodyCandidate, ...]:
    validate_state_characters(
        graph,
        state_characters,
    )

    candidates = []

    for size in range(1, len(graph.states) + 1):
        for region_states in combinations(
            sorted(graph.states),
            size,
        ):
            try:
                candidate = derive_body_candidate(
                    graph=graph,
                    region_states=region_states,
                    state_characters=state_characters,
                    region_name=(
                        "body[" + ",".join(region_states) + "]"
                    ),
                )
            except ValueError:
                continue

            candidates.append(candidate)

    return tuple(candidates)


def minimal_body_candidates(
    graph: MotionGraph,
    state_characters: StateCharacterMap,
) -> Tuple[BodyCandidate, ...]:
    candidates = enumerate_body_candidates(
        graph,
        state_characters,
    )

    if not candidates:
        return ()

    minimum_size = min(
        len(candidate.states)
        for candidate in candidates
    )

    return tuple(
        candidate
        for candidate in candidates
        if len(candidate.states) == minimum_size
    )
