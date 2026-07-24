"""Character-conditioned admissibility for TM-0.

This experiment replaces the previous-address constraint with a rule
computed only from current and resulting cycle-space character.

Toy monotone rule:

    a candidate is admissible when it does not reduce
    the number of POLAR cycle bits

Candidates that reduce POLAR count remain addressable as structured
absence.

This is a constraint scaffold, not a universal TM law.
"""

from dataclasses import dataclass
from typing import Tuple

from .character_update import CharacterSignature
from .possibility_frontier import PossibleRealization


@dataclass(frozen=True)
class CharacterConstraintPartition:
    admissible: Tuple[PossibleRealization, ...]
    structured_absence: Tuple[PossibleRealization, ...]


def polar_count(
    signature: CharacterSignature,
) -> int:
    return sum(
        1
        for _, sign in signature
        if int(sign) == -1
    )


def character_admits(
    possibility: PossibleRealization,
) -> bool:
    return (
        polar_count(possibility.after)
        >= polar_count(possibility.before)
    )


def partition_by_character(
    frontier: Tuple[PossibleRealization, ...],
) -> CharacterConstraintPartition:
    admissible = tuple(
        possibility
        for possibility in frontier
        if character_admits(possibility)
    )

    structured_absence = tuple(
        possibility
        for possibility in frontier
        if not character_admits(possibility)
    )

    return CharacterConstraintPartition(
        admissible=admissible,
        structured_absence=structured_absence,
    )


def partition_is_complete(
    frontier: Tuple[PossibleRealization, ...],
    partition: CharacterConstraintPartition,
) -> bool:
    admissible = set(partition.admissible)
    absent = set(partition.structured_absence)

    return (
        not admissible.intersection(absent)
        and admissible.union(absent) == set(frontier)
    )
