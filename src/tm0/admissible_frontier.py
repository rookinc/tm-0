"""Admissible possibility frontier for TM-0.

The full possibility frontier contains every addressed local edge-sign
flip.

A minimal non-backtracking constraint excludes the edge used by the
most recent realization.

The excluded address remains inside possibility as structured absence.

This is a toy constraint scaffold, not a proposed universal law.
"""

from dataclasses import dataclass
from typing import Optional
from typing import Tuple

from .graph_switching_normal_form import Edge
from .graph_switching_normal_form import canonical_edge
from .possibility_frontier import PossibleRealization


@dataclass(frozen=True)
class AdmissiblePartition:
    admissible: Tuple[PossibleRealization, ...]
    structured_absence: Tuple[PossibleRealization, ...]


def partition_frontier(
    frontier: Tuple[PossibleRealization, ...],
    previous_address: Optional[Edge],
) -> AdmissiblePartition:
    if previous_address is None:
        return AdmissiblePartition(
            admissible=frontier,
            structured_absence=(),
        )

    blocked = canonical_edge(*previous_address)

    admissible = tuple(
        possibility
        for possibility in frontier
        if possibility.address != blocked
    )

    structured_absence = tuple(
        possibility
        for possibility in frontier
        if possibility.address == blocked
    )

    return AdmissiblePartition(
        admissible=admissible,
        structured_absence=structured_absence,
    )


def partition_is_complete(
    frontier: Tuple[PossibleRealization, ...],
    partition: AdmissiblePartition,
) -> bool:
    combined = partition.admissible + partition.structured_absence

    return (
        len(combined) == len(frontier)
        and set(combined) == set(frontier)
        and not (
            set(partition.admissible)
            & set(partition.structured_absence)
        )
    )
