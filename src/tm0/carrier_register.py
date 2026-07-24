"""Carrier-separated register model for TM-0.

Possibility is the internal address space of an existing carrier.

The internal register contains only:

NULL
    The carrier exists with no non-null character.

CHARACTERIZED
    The carrier exists with non-null character.

Carrier absence is represented by None, outside the internal register.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class InternalRegister(str, Enum):
    NULL = "NULL"
    CHARACTERIZED = "CHARACTERIZED"


@dataclass(frozen=True)
class Carrier:
    register: InternalRegister


@dataclass(frozen=True)
class CarrierRealization:
    before: Optional[Carrier]
    after: Optional[Carrier]

    @property
    def changed(self) -> bool:
        return self.before != self.after


def instantiate_carrier() -> CarrierRealization:
    """Instantiate a carrier at its null internal address."""
    return CarrierRealization(
        before=None,
        after=Carrier(register=InternalRegister.NULL),
    )


def realize_register(
    before: Carrier,
    after: Carrier,
) -> CarrierRealization:
    """Admit a non-identity transition between internal addresses."""
    event = CarrierRealization(before=before, after=after)

    if not event.changed:
        raise ValueError(
            "identity transition is not an internal realization: "
            f"{before.register.value} -> {after.register.value}"
        )

    return event
