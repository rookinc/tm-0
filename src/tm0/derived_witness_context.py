"""Derive witness context from boundary and character data.

The context label is not supplied as a free descriptive name.

It is constructed from:

    a normalized boundary signature
    a normalized binary character

This is a bounded structural context scaffold.
"""

from dataclasses import dataclass
from typing import Tuple


BoundarySignature = Tuple[str, ...]
Character = Tuple[int, ...]


@dataclass(frozen=True)
class WitnessContext:
    boundary_signature: BoundarySignature
    character: Character

    @property
    def key(self) -> str:
        boundary_part = ",".join(self.boundary_signature)
        character_part = "".join(str(bit) for bit in self.character)

        return (
            f"boundary[{boundary_part}]"
            f"|character[{character_part}]"
        )


def normalize_boundary_signature(
    boundary_signature: BoundarySignature,
) -> BoundarySignature:
    if not boundary_signature:
        raise ValueError("boundary signature must not be empty")

    if any(not item for item in boundary_signature):
        raise ValueError("boundary signature entries must not be empty")

    if len(set(boundary_signature)) != len(boundary_signature):
        raise ValueError("boundary signature entries must be unique")

    return tuple(sorted(boundary_signature))


def normalize_character(
    character: Character,
) -> Character:
    if not character:
        raise ValueError("character must not be empty")

    if any(bit not in (0, 1) for bit in character):
        raise ValueError("character entries must be binary")

    return tuple(character)


def derive_witness_context(
    boundary_signature: BoundarySignature,
    character: Character,
) -> WitnessContext:
    return WitnessContext(
        boundary_signature=normalize_boundary_signature(
            boundary_signature,
        ),
        character=normalize_character(
            character,
        ),
    )
