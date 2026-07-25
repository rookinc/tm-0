"""Derive thalion candidates from nontrivial returning bodies.

A thalion candidate is a body candidate that:

    contains at least two states
    contains an internal directed return path
    preserves one character
    has a nonempty boundary cut

Internal return means there exists a directed cycle using only states
and relations internal to the candidate body.

This is a bounded thalion-derivation scaffold.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Set
from typing import Tuple

from .derived_body_candidate import BodyCandidate
from .derived_body_candidate import StateCharacterMap
from .derived_body_candidate import enumerate_body_candidates
from .derived_region_boundary import MotionGraph
from .derived_region_boundary import validate_motion_graph


StateName = str
RelationName = str


@dataclass(frozen=True)
class ThalionCandidate:
    body: BodyCandidate
    return_path_states: Tuple[StateName, ...]
    return_path_relations: Tuple[RelationName, ...]

    @property
    def states(self) -> Tuple[StateName, ...]:
        return self.body.states

    @property
    def character(self) -> Tuple[int, ...]:
        return self.body.character


def internal_rules_for_body(
    graph: MotionGraph,
    body: BodyCandidate,
):
    validate_motion_graph(graph)

    inside = set(body.states)

    return tuple(
        rule
        for rule in graph.rules
        if (
            rule.source_state in inside
            and rule.target_state in inside
        )
    )


def find_internal_return_path(
    graph: MotionGraph,
    body: BodyCandidate,
) -> Tuple[
    Tuple[StateName, ...],
    Tuple[RelationName, ...],
]:
    rules = internal_rules_for_body(
        graph,
        body,
    )

    if not rules:
        raise ValueError(
            "body has no internal relations"
        )

    adjacency: Dict[
        StateName,
        Tuple[Tuple[StateName, RelationName], ...],
    ] = {}

    for state in body.states:
        adjacency[state] = tuple(
            (
                rule.target_state,
                rule.relation_name,
            )
            for rule in rules
            if rule.source_state == state
        )

    def search_from(
        start: StateName,
    ):
        frontier = [
            (
                start,
                (start,),
                (),
                frozenset(),
            )
        ]

        while frontier:
            (
                current,
                state_path,
                relation_path,
                used_relations,
            ) = frontier.pop()

            for target, relation in adjacency[current]:
                if relation in used_relations:
                    continue

                next_state_path = (
                    *state_path,
                    target,
                )

                next_relation_path = (
                    *relation_path,
                    relation,
                )

                if target == start:
                    return (
                        next_state_path,
                        next_relation_path,
                    )

                if target in state_path:
                    continue

                frontier.append(
                    (
                        target,
                        next_state_path,
                        next_relation_path,
                        used_relations | {relation},
                    )
                )

        return None

    for start in body.states:
        result = search_from(start)

        if result is not None:
            return result

    raise ValueError(
        "body has no internal directed return path"
    )


def derive_thalion_candidate(
    graph: MotionGraph,
    body: BodyCandidate,
) -> ThalionCandidate:
    if len(body.states) < 2:
        raise ValueError(
            "thalion candidate must contain at least two states"
        )

    (
        return_path_states,
        return_path_relations,
    ) = find_internal_return_path(
        graph,
        body,
    )

    return ThalionCandidate(
        body=body,
        return_path_states=return_path_states,
        return_path_relations=return_path_relations,
    )


def enumerate_thalion_candidates(
    graph: MotionGraph,
    state_characters: StateCharacterMap,
) -> Tuple[ThalionCandidate, ...]:
    bodies = enumerate_body_candidates(
        graph,
        state_characters,
    )

    candidates = []

    for body in bodies:
        try:
            candidate = derive_thalion_candidate(
                graph,
                body,
            )
        except ValueError:
            continue

        candidates.append(candidate)

    return tuple(candidates)


def minimal_thalion_candidates(
    graph: MotionGraph,
    state_characters: StateCharacterMap,
) -> Tuple[ThalionCandidate, ...]:
    candidates = enumerate_thalion_candidates(
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
