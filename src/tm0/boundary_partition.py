"""Boundary squeeze for TM-0.

A character-induced classifier partitions possibility into:

ADMISSIBLE
STRUCTURED_ABSENCE

The partition alone creates distinction.

A boundary set requires an additional adjacency relation between
addresses.

This experiment separates:

partition
    which side each address occupies

boundary
    where opposite classifications meet
"""

from dataclasses import dataclass
from enum import Enum
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Tuple


Address = str
Adjacency = Tuple[Address, Address]


class AddressClass(str, Enum):
    ADMISSIBLE = "ADMISSIBLE"
    STRUCTURED_ABSENCE = "STRUCTURED_ABSENCE"


@dataclass(frozen=True)
class CharacterPartition:
    classes: Dict[Address, AddressClass]

    @property
    def admissible(self) -> Tuple[Address, ...]:
        return tuple(
            address
            for address, value in self.classes.items()
            if value is AddressClass.ADMISSIBLE
        )

    @property
    def structured_absence(self) -> Tuple[Address, ...]:
        return tuple(
            address
            for address, value in self.classes.items()
            if value is AddressClass.STRUCTURED_ABSENCE
        )


def classify_possibility(
    addresses: Iterable[Address],
    classifier: Callable[[Address], bool],
) -> CharacterPartition:
    classes = {}

    for address in addresses:
        classes[address] = (
            AddressClass.ADMISSIBLE
            if classifier(address)
            else AddressClass.STRUCTURED_ABSENCE
        )

    return CharacterPartition(classes=classes)


def boundary_addresses(
    partition: CharacterPartition,
    adjacency: Iterable[Adjacency],
) -> Tuple[Address, ...]:
    boundary = set()

    for left, right in adjacency:
        if left not in partition.classes or right not in partition.classes:
            raise ValueError("adjacency address must belong to possibility")

        if partition.classes[left] is not partition.classes[right]:
            boundary.add(left)
            boundary.add(right)

    return tuple(sorted(boundary))
