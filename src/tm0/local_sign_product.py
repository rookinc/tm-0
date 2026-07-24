"""Cycle sign product for TM-0.

Each relation carries one local orientation sign:

PRESERVE = +1
INVERT = -1

The returned registration of a closed cycle is determined by the
product of all local signs.
"""

from dataclasses import dataclass
from enum import IntEnum
from math import prod
from typing import Tuple

from .incidence_equivalence import AnonymousRelation
from .incidence_equivalence import EndpointEquivalence
from .incidence_equivalence import is_closed
from .orientation_registration import RegistrationValue
from .orientation_registration import TraversalReading


class LocalSign(IntEnum):
    INVERT = -1
    PRESERVE = 1


@dataclass(frozen=True)
class SignedReturn:
    relation_count: int
    sign_product: int
    departure: TraversalReading
    returned: TraversalReading
    registration: RegistrationValue


def apply_sign(
    reading: TraversalReading,
    sign: LocalSign,
) -> TraversalReading:
    if sign is LocalSign.PRESERVE:
        return reading

    if reading is TraversalReading.FORWARD:
        return TraversalReading.REVERSED

    return TraversalReading.FORWARD


def traverse_signed_cycle(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
    signs: Tuple[LocalSign, ...],
    departure: TraversalReading = TraversalReading.FORWARD,
) -> SignedReturn:
    if not is_closed(relations, incidence):
        raise ValueError("signed traversal requires a closed relation chain")

    if len(signs) != len(relations):
        raise ValueError("one local sign is required per relation")

    reading = departure

    for sign in signs:
        reading = apply_sign(reading, sign)

    sign_product = prod(int(sign) for sign in signs)

    registration = (
        RegistrationValue.SAME
        if reading is departure
        else RegistrationValue.POLAR
    )

    return SignedReturn(
        relation_count=len(relations),
        sign_product=sign_product,
        departure=departure,
        returned=reading,
        registration=registration,
    )
