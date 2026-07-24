"""Closure-parity orientation experiment for TM-0.

Assume one uniform local inversion at every traversed relation.

This experiment asks whether the returned orientation is determined
by the parity of the closed relation chain.

No special global half-flip is inserted.
"""

from dataclasses import dataclass
from typing import Tuple

from .incidence_equivalence import (
    AnonymousRelation,
    EndpointEquivalence,
    is_closed,
)
from .orientation_registration import (
    RegistrationValue,
    TraversalReading,
)


@dataclass(frozen=True)
class ParityReturn:
    relation_count: int
    departure: TraversalReading
    returned: TraversalReading
    registration: RegistrationValue


def invert(
    reading: TraversalReading,
) -> TraversalReading:
    if reading is TraversalReading.FORWARD:
        return TraversalReading.REVERSED

    return TraversalReading.FORWARD


def traverse_with_local_inversion(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
    departure: TraversalReading = TraversalReading.FORWARD,
) -> ParityReturn:
    if not is_closed(relations, incidence):
        raise ValueError(
            "parity return requires a closed relation chain"
        )

    reading = departure

    for _ in relations:
        reading = invert(reading)

    registration = (
        RegistrationValue.SAME
        if reading is departure
        else RegistrationValue.POLAR
    )

    return ParityReturn(
        relation_count=len(relations),
        departure=departure,
        returned=reading,
        registration=registration,
    )
