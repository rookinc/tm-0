"""Body region from boundary-preserving character reachability.

A body is represented as the connected component of character states
reachable through boundary-preserving realizations.

This experiment does not yet claim maximality across an infinite state
space. It computes the maximal component inside a supplied finite
transition system.
"""

from collections import deque
from dataclasses import dataclass
from typing import Dict
from typing import Iterable
from typing import Tuple

from .character_update import CharacterSignature


StateName = str
Transition = Tuple[StateName, StateName]


@dataclass(frozen=True)
class CharacterState:
    name: StateName
    character: CharacterSignature
    boundary: Tuple[str, ...]


@dataclass(frozen=True)
class BodyRegion:
    seed: StateName
    members: Tuple[StateName, ...]
    boundary: Tuple[str, ...]


def boundary_preserving_edges(
    states: Dict[StateName, CharacterState],
    transitions: Iterable[Transition],
) -> Tuple[Transition, ...]:
    kept = []

    for left, right in transitions:
        if left not in states or right not in states:
            raise ValueError("transition state must exist")

        if states[left].boundary == states[right].boundary:
            kept.append((left, right))

    return tuple(kept)


def body_region(
    states: Dict[StateName, CharacterState],
    transitions: Iterable[Transition],
    seed: StateName,
) -> BodyRegion:
    if seed not in states:
        raise ValueError("seed state must exist")

    allowed = boundary_preserving_edges(states, transitions)
    adjacency = {name: set() for name in states}

    for left, right in allowed:
        adjacency[left].add(right)
        adjacency[right].add(left)

    visited = {seed}
    queue = deque([seed])

    while queue:
        current = queue.popleft()

        for neighbor in sorted(adjacency[current]):
            if neighbor in visited:
                continue

            visited.add(neighbor)
            queue.append(neighbor)

    return BodyRegion(
        seed=seed,
        members=tuple(sorted(visited)),
        boundary=states[seed].boundary,
    )
