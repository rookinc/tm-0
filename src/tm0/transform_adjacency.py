"""Adjacency derived from minimal character transformability.

Two character signatures are adjacent when exactly one cycle-space bit
differs.

No external topology is supplied.
"""

from typing import Tuple

from .character_update import CharacterSignature


def differing_bits(
    left: CharacterSignature,
    right: CharacterSignature,
) -> Tuple[tuple[str, str], ...]:
    left_map = dict(left)
    right_map = dict(right)

    if tuple(left_map) != tuple(right_map):
        raise ValueError("character signatures must use the same addresses")

    return tuple(
        address
        for address in left_map
        if left_map[address] != right_map[address]
    )


def minimally_transformable(
    left: CharacterSignature,
    right: CharacterSignature,
) -> bool:
    return len(differing_bits(left, right)) == 1
