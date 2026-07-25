"""Certified carrier actions for the three quotient systems.

Source:

    Project 41
    project42_quotient_frame_orbit_certificate_004.json

The three order-two carrier permutations tau0, tau1, and tau2 act on
the fixed thirty-element carrier.

Each action induces the certified permutation of the quotient-system
family P0, P1, and P2.

This module records source-backed fixture data only.
It does not derive the permutations or claim global completeness.
"""

from dataclasses import dataclass
from typing import Tuple

from .g60_three_quotient_systems import (
    G60_QUOTIENT_CARRIER,
    G60_QUOTIENT_SYSTEMS,
)
from .selected_equivalence import CanonicalPartition


CarrierPermutation = Tuple[int, ...]
FamilyPermutation = Tuple[int, ...]


@dataclass(frozen=True)
class CertifiedCarrierAction:
    name: str
    carrier_permutation: CarrierPermutation
    family_permutation: FamilyPermutation

    def __post_init__(self) -> None:
        expected_carrier = tuple(
            range(len(G60_QUOTIENT_CARRIER))
        )

        if tuple(sorted(self.carrier_permutation)) != expected_carrier:
            raise ValueError(
                "carrier action must be a permutation"
            )

        expected_family = tuple(
            range(len(G60_QUOTIENT_SYSTEMS))
        )

        if tuple(sorted(self.family_permutation)) != expected_family:
            raise ValueError(
                "family action must be a permutation"
            )

    def image_vertex(
        self,
        vertex: str,
    ) -> str:
        if vertex not in G60_QUOTIENT_CARRIER:
            raise ValueError(
                "vertex is not in the certified carrier"
            )

        return str(
            self.carrier_permutation[int(vertex)]
        )

    def image_partition(
        self,
        partition: CanonicalPartition,
    ) -> CanonicalPartition:
        return tuple(
            sorted(
                tuple(
                    sorted(
                        self.image_vertex(vertex)
                        for vertex in block
                    )
                )
                for block in partition
            )
        )


TAU0 = CertifiedCarrierAction(
    name="tau0",
    carrier_permutation=(
        1, 0, 3, 2, 5, 4, 7, 6, 9, 8,
        11, 10, 13, 12, 15, 14, 17, 16, 19, 18,
        21, 20, 23, 22, 25, 24, 27, 26, 29, 28,
    ),
    family_permutation=(0, 2, 1),
)


TAU1 = CertifiedCarrierAction(
    name="tau1",
    carrier_permutation=(
        11, 28, 25, 12, 19, 26, 23, 14, 17, 20,
        29, 0, 3, 24, 7, 22, 21, 8, 27, 4,
        9, 16, 15, 6, 13, 2, 5, 18, 1, 10,
    ),
    family_permutation=(2, 1, 0),
)


TAU2 = CertifiedCarrierAction(
    name="tau2",
    carrier_permutation=(
        29, 10, 13, 24, 27, 18, 15, 22, 21, 16,
        1, 28, 25, 2, 23, 6, 9, 20, 5, 26,
        17, 8, 7, 14, 3, 12, 19, 4, 11, 0,
    ),
    family_permutation=(1, 0, 2),
)


CERTIFIED_CARRIER_ACTIONS = (
    TAU0,
    TAU1,
    TAU2,
)
