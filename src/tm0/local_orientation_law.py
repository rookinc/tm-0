"""Local orientation-law squeeze for TM-0.

The same directed incidence structure may carry either of two local
orientation laws:

PRESERVE
    Traversal retains the incoming orientation.

INVERT
    Traversal exchanges the incoming orientation.

The experiment asks whether direction, incidence, composition, and
closure already select one of these laws.
"""

from dataclasses import dataclass
from enum import Enum
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


class LocalOrientationLaw(str, Enum):
    PRESERVE = "PRESERVE"
    INVERT = "INVERT"


@dataclass(frozen=True)
class LocalLawReturn:
    relation_count: int
    law: LocalOrientationLaw
    departure: TraversalReading
    returned: TraversalReading
    registration: RegistrationValue


def apply_local_law(
    reading: TraversalReading,
    law: LocalOrientationLaw,
) -> TraversalReading:
    if law is LocalOrientationLaw.PRESERVE:
        return reading

    if reading is TraversalReading.FORWARD:
        return TraversalReading.REVERSED

    return TraversalReading.FORWARD


def traverse_with_local_law(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
    law: LocalOrientationLaw,
    departure: TraversalReading = TraversalReading.FORWARD,
) -> LocalLawReturn:
    if not is_closed(relations, incidence):
        raise ValueError(
            "local orientation law requires a closed relation chain"
        )

    reading = departure

    for _ in relations:
        reading = apply_local_law(reading, law)

    registration = (
        RegistrationValue.SAME
        if reading is departure
        else RegistrationValue.POLAR
    )

    return LocalLawReturn(
        relation_count=len(relations),
        law=law,
        departure=departure,
        returned=reading,
        registration=registration,
    )
