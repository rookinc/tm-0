"""Select one lawful equivalence relation over a fixed carrier.

This scaffold represents:

    one finite carrier
    multiple registered equivalence systems
    one selected system

Each system is encoded canonically as a partition of the carrier.

Selection does not mutate the carrier or remove the unselected systems.

This is a candidate implementation for Experiments 054 and 055.
It does not yet model symmetry groups, stabilizers, or quotient graphs.
"""

from dataclasses import dataclass
from typing import FrozenSet
from typing import Iterable
from typing import Tuple


CarrierElement = str
EquivalenceClass = Tuple[CarrierElement, ...]
CanonicalPartition = Tuple[EquivalenceClass, ...]


def canonical_partition(
    carrier: FrozenSet[CarrierElement],
    classes: Iterable[Iterable[CarrierElement]],
) -> CanonicalPartition:
    """Validate and canonicalize one partition of the carrier."""
    normalized = tuple(
        sorted(
            tuple(sorted(equivalence_class))
            for equivalence_class in classes
        )
    )

    if not normalized:
        raise ValueError(
            "equivalence partition must contain classes"
        )

    if any(
        not equivalence_class
        for equivalence_class in normalized
    ):
        raise ValueError(
            "equivalence classes must not be empty"
        )

    flattened = tuple(
        element
        for equivalence_class in normalized
        for element in equivalence_class
    )

    if len(flattened) != len(set(flattened)):
        raise ValueError(
            "equivalence classes must be disjoint"
        )

    if frozenset(flattened) != carrier:
        raise ValueError(
            "equivalence partition must cover the carrier"
        )

    return normalized


@dataclass(frozen=True)
class EquivalenceSystem:
    name: str
    partition: CanonicalPartition

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError(
                "equivalence system name must not be empty"
            )


@dataclass(frozen=True)
class SelectedEquivalence:
    carrier: FrozenSet[CarrierElement]
    systems: Tuple[EquivalenceSystem, ...]
    selected_name: str

    def __post_init__(self) -> None:
        if not self.carrier:
            raise ValueError(
                "carrier must not be empty"
            )

        if len(self.systems) < 2:
            raise ValueError(
                "at least two equivalence systems are required"
            )

        names = tuple(
            system.name
            for system in self.systems
        )

        if len(names) != len(set(names)):
            raise ValueError(
                "equivalence system names must be unique"
            )

        partitions = tuple(
            system.partition
            for system in self.systems
        )

        if len(partitions) != len(set(partitions)):
            raise ValueError(
                "equivalence systems must be distinct"
            )

        for system in self.systems:
            canonical_partition(
                self.carrier,
                system.partition,
            )

        if self.selected_name not in names:
            raise ValueError(
                "selected equivalence system is not registered"
            )

    @property
    def selected(self) -> EquivalenceSystem:
        for system in self.systems:
            if system.name == self.selected_name:
                return system

        raise RuntimeError(
            "registered selected system was not found"
        )

    @property
    def alternatives(self) -> Tuple[EquivalenceSystem, ...]:
        return tuple(
            system
            for system in self.systems
            if system.name != self.selected_name
        )

    def classes(self) -> CanonicalPartition:
        return self.selected.partition


def select_equivalence(
    carrier: Iterable[CarrierElement],
    systems: Iterable[EquivalenceSystem],
    selected_name: str,
) -> SelectedEquivalence:
    """Bind one selected system while retaining all lawful alternatives."""
    frozen_carrier = frozenset(carrier)

    canonical_systems = tuple(
        sorted(
            (
                EquivalenceSystem(
                    name=system.name,
                    partition=canonical_partition(
                        frozen_carrier,
                        system.partition,
                    ),
                )
                for system in systems
            ),
            key=lambda system: system.name,
        )
    )

    return SelectedEquivalence(
        carrier=frozen_carrier,
        systems=canonical_systems,
        selected_name=selected_name,
    )
