"""Character-blind quotient of the TM-0 addressed register.

This experiment forgets which non-null character is present.

ABSENT
    No carrier is present.

NULL
    A carrier is present with null registration.

CHARACTERIZED
    A carrier is present with some non-null registration.

The quotient tests whether named A/B polarity is required for the
current carrier/null distinction.
"""

from dataclasses import dataclass
from enum import Enum

from .register import AddressedState


class QuotientState(str, Enum):
    ABSENT = "ABSENT"
    NULL = "NULL"
    CHARACTERIZED = "CHARACTERIZED"


@dataclass(frozen=True)
class QuotientRealization:
    before: QuotientState
    after: QuotientState

    @property
    def changed(self) -> bool:
        return self.before != self.after


def forget_polarity(state: AddressedState) -> QuotientState:
    """Forget whether a characterized registration is A or B."""
    if state is AddressedState.ABSENT:
        return QuotientState.ABSENT
    if state is AddressedState.NULL:
        return QuotientState.NULL
    return QuotientState.CHARACTERIZED


def realize_quotient(
    before: QuotientState,
    after: QuotientState,
) -> QuotientRealization:
    """Admit only non-identity transitions in the quotient."""
    event = QuotientRealization(before=before, after=after)

    if not event.changed:
        raise ValueError(
            "identity transition is not a quotient realization: "
            f"{before.value} -> {after.value}"
        )

    return event
