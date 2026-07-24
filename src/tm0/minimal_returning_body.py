"""Minimal returning body candidate for TM-0.

A returning body region must contain a positive-length closed transition
path that remains inside one boundary class.

This experiment compares:

one state
    no non-identity return

two states
    possible return through s0 -> s1 -> s0

three states
    possible return, but not required for minimality
"""

from collections import deque
from dataclasses import dataclass
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Tuple

from .body_region import CharacterState
from .body_region import Transition
from .body_region import boundary_preserving_edges


@dataclass(frozen=True)
class ReturnCycle:
    seed: str
    path: Tuple[str, ...]
    boundary: Tuple[str, ...]


def shortest_return_cycle(
    states: Dict[str, CharacterState],
    transitions: Iterable[Transition],
    seed: str,
) -> Optional[ReturnCycle]:
    if seed not in states:
        raise ValueError("seed state must exist")

    allowed = boundary_preserving_edges(
        states,
        transitions,
    )

    adjacency = {name: [] for name in states}

    for left, right in allowed:
        adjacency[left].append(right)

    queue = deque(
        (neighbor, (seed, neighbor))
        for neighbor in adjacency[seed]
    )

    while queue:
        current, path = queue.popleft()

        if current == seed and len(path) > 1:
            return ReturnCycle(
                seed=seed,
                path=path,
                boundary=states[seed].boundary,
            )

        for neighbor in adjacency[current]:
            if neighbor in path[1:-1]:
                continue

            queue.append(
                (
                    neighbor,
                    path + (neighbor,),
                )
            )

    return None


def minimal_returning_body_size(
    states: Dict[str, CharacterState],
    transitions: Iterable[Transition],
) -> Optional[int]:
    sizes = []

    for seed in states:
        cycle = shortest_return_cycle(
            states,
            transitions,
            seed,
        )

        if cycle is not None:
            sizes.append(
                len(set(cycle.path[:-1]))
            )

    if not sizes:
        return None

    return min(sizes)
