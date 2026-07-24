"""Boundary-persistence admissibility for TM-0.

A candidate realization is admissible when it preserves the current
boundary set.

The partitions and adjacency are supplied by the experiment.

This tests boundary persistence as a constraint mechanism.
It does not yet derive the partition itself.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Iterable
from typing import Tuple

from .boundary_partition import Adjacency
from .boundary_partition import Address
from .boundary_partition import AddressClass
from .boundary_partition import CharacterPartition
from .boundary_partition import boundary_addresses


@dataclass(frozen=True)
class BoundaryCandidate:
    address: Address
    resulting_partition: CharacterPartition


@dataclass(frozen=True)
class BoundaryPersistencePartition:
    admissible: Tuple[BoundaryCandidate, ...]
    structured_absence: Tuple[BoundaryCandidate, ...]


def boundary_signature(
    partition: CharacterPartition,
    adjacency: Iterable[Adjacency],
) -> Tuple[Address, ...]:
    return boundary_addresses(partition, adjacency)


def preserves_boundary(
    current: CharacterPartition,
    candidate: BoundaryCandidate,
    adjacency: Iterable[Adjacency],
) -> bool:
    return boundary_signature(
        current,
        adjacency,
    ) == boundary_signature(
        candidate.resulting_partition,
        adjacency,
    )


def partition_by_boundary_persistence(
    current: CharacterPartition,
    candidates: Tuple[BoundaryCandidate, ...],
    adjacency: Iterable[Adjacency],
) -> BoundaryPersistencePartition:
    adjacency_tuple = tuple(adjacency)

    admissible = tuple(
        candidate
        for candidate in candidates
        if preserves_boundary(
            current,
            candidate,
            adjacency_tuple,
        )
    )

    structured_absence = tuple(
        candidate
        for candidate in candidates
        if not preserves_boundary(
            current,
            candidate,
            adjacency_tuple,
        )
    )

    return BoundaryPersistencePartition(
        admissible=admissible,
        structured_absence=structured_absence,
    )


def partition_from_classes(
    classes: Dict[Address, AddressClass],
) -> CharacterPartition:
    return CharacterPartition(classes=dict(classes))
