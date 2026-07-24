"""Minimal thalion candidate search for TM-0.

A thalion candidate is a finite body region with:

1. one persistent boundary;
2. at least two distinct character states;
3. at least one boundary-preserving transition;
4. nontrivial character variation.

This experiment searches supplied finite systems for the smallest
candidate by number of states.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Tuple

from .body_region import CharacterState
from .body_region import Transition
from .body_region import body_region


@dataclass(frozen=True)
class ThalionCandidate:
    seed: str
    members: Tuple[str, ...]
    boundary: Tuple[str, ...]
    character_count: int


def candidate_from_seed(
    states: Dict[str, CharacterState],
    transitions: Iterable[Transition],
    seed: str,
) -> Optional[ThalionCandidate]:
    region = body_region(
        states,
        transitions,
        seed,
    )

    characters = {
        states[name].character
        for name in region.members
    }

    if len(region.members) < 2:
        return None

    if len(characters) < 2:
        return None

    return ThalionCandidate(
        seed=seed,
        members=region.members,
        boundary=region.boundary,
        character_count=len(characters),
    )


def minimal_thalion_candidate(
    states: Dict[str, CharacterState],
    transitions: Iterable[Transition],
) -> Optional[ThalionCandidate]:
    candidates = []

    for seed in states:
        candidate = candidate_from_seed(
            states,
            transitions,
            seed,
        )

        if candidate is not None:
            candidates.append(candidate)

    if not candidates:
        return None

    return min(
        candidates,
        key=lambda candidate: (
            len(candidate.members),
            candidate.members,
        ),
    )
