"""Orientation-registration experiment for TM-0.

A realized return receipt confirms that a traversal came home.

The receipt alone does not contain A/B polarity.

Polarity appears only when two readings of the completed traversal are
compared and found to have opposite orientation.

This experiment does not assume that return automatically reverses
orientation. It tests that claim.
"""

from dataclasses import dataclass
from enum import Enum

from .return_admissibility import ReturnReceipt


class TraversalReading(str, Enum):
    FORWARD = "FORWARD"
    REVERSED = "REVERSED"


class RegistrationValue(str, Enum):
    NULL = "NULL"
    SAME = "SAME"
    POLAR = "POLAR"


@dataclass(frozen=True)
class OrientedReturn:
    """One completed return receipt with one traversal reading."""

    receipt: ReturnReceipt
    reading: TraversalReading


@dataclass(frozen=True)
class OrientationRegistration:
    """Comparison result for two readings of one completed return."""

    departure: TraversalReading
    returned: TraversalReading
    value: RegistrationValue


def unregistered_return(
    receipt: ReturnReceipt,
) -> RegistrationValue:
    """A return receipt alone carries no orientation comparison."""
    if not receipt.completed:
        raise ValueError("return receipt is incomplete")

    return RegistrationValue.NULL


def compare_orientations(
    departure: OrientedReturn,
    returned: OrientedReturn,
) -> OrientationRegistration:
    """Compare two readings of the same completed return."""
    if departure.receipt != returned.receipt:
        raise ValueError(
            "orientation comparison requires the same return receipt"
        )

    if departure.reading is returned.reading:
        value = RegistrationValue.SAME
    else:
        value = RegistrationValue.POLAR

    return OrientationRegistration(
        departure=departure.reading,
        returned=returned.reading,
        value=value,
    )
