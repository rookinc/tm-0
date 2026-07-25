"""Certified three-system quotient fixture for the 30-vertex carrier.

Source:

    Project 41
    project42_quotient_frame_orbit_certificate_004.json

The fixture records only the certified carrier and the three explicit
fifteen-pair partitions P0, P1, and P2.

It does not regenerate the partitions.

It does not yet model the S3 action, stabilizers, quotient edges, or
global completeness beyond the certified natural orbit.
"""

from typing import Tuple

from .selected_equivalence import EquivalenceSystem
from .selected_equivalence import SelectedEquivalence
from .selected_equivalence import select_equivalence


CarrierVertex = str
Pair = Tuple[CarrierVertex, CarrierVertex]


G60_QUOTIENT_CARRIER = tuple(
    str(index)
    for index in range(30)
)


P0_BLOCKS: Tuple[Pair, ...] = (
    ("0", "1"),
    ("2", "3"),
    ("4", "5"),
    ("6", "7"),
    ("8", "9"),
    ("10", "11"),
    ("12", "13"),
    ("14", "15"),
    ("16", "17"),
    ("18", "19"),
    ("20", "21"),
    ("22", "23"),
    ("24", "25"),
    ("26", "27"),
    ("28", "29"),
)


P1_BLOCKS: Tuple[Pair, ...] = (
    ("0", "11"),
    ("1", "28"),
    ("2", "25"),
    ("3", "12"),
    ("4", "19"),
    ("5", "26"),
    ("6", "23"),
    ("7", "14"),
    ("8", "17"),
    ("9", "20"),
    ("10", "29"),
    ("13", "24"),
    ("15", "22"),
    ("16", "21"),
    ("18", "27"),
)


P2_BLOCKS: Tuple[Pair, ...] = (
    ("0", "29"),
    ("1", "10"),
    ("2", "13"),
    ("3", "24"),
    ("4", "27"),
    ("5", "18"),
    ("6", "15"),
    ("7", "22"),
    ("8", "21"),
    ("9", "16"),
    ("11", "28"),
    ("12", "25"),
    ("14", "23"),
    ("17", "20"),
    ("19", "26"),
)


G60_QUOTIENT_SYSTEMS = (
    EquivalenceSystem(
        name="P0",
        partition=P0_BLOCKS,
    ),
    EquivalenceSystem(
        name="P1",
        partition=P1_BLOCKS,
    ),
    EquivalenceSystem(
        name="P2",
        partition=P2_BLOCKS,
    ),
)


def select_g60_quotient_system(
    selected_name: str,
) -> SelectedEquivalence:
    """Select one certified quotient system on the fixed carrier."""
    return select_equivalence(
        carrier=G60_QUOTIENT_CARRIER,
        systems=G60_QUOTIENT_SYSTEMS,
        selected_name=selected_name,
    )
