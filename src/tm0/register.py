"""Minimal addressed-state experiment for TM-0.

Possibility is represented by an address space containing three
currently distinguishable states:

ABSENT
    No carrier is present.

NULL
    A carrier is present with null registration.

A or B
    A carrier is present with characterized registration.

This module does not model character, history, agency, geometry,
graphs, probability, or physical motion.
"""

from dataclasses import dataclass
from enum import Enum


class AddressedState(str, Enum):
    ABSENT = "ABSENT"
    NULL = "NULL"
    A = "A"
    B = "B"


@dataclass(frozen=True)
class Realization:
    before: AddressedState
    after: AddressedState

    @property
    def changed(self) -> bool:
        return self.before != self.after


def realize(
    before: AddressedState,
    after: AddressedState,
) -> Realization:
    """Return a non-identity addressed-state realization.

    A realization changes the addressed state. A transition may create
    a carrier while leaving its register null, as in ABSENT -> NULL.
    """
    event = Realization(before=before, after=after)

    if not event.changed:
        raise ValueError(
            f"identity transition is not a realization: {before.value} -> {after.value}"
        )

    return event
