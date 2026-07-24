"""Carrier plurality test for TM-0.

The current lawful carrier description contains only an internal
register value. No name, identifier, coordinate, history, relation,
or Python object identity is admitted as ontological structure.

This experiment asks whether two independently instantiated carriers
with the same null registration remain distinguishable under that
description.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple

from .carrier_register import InternalRegister


@dataclass(frozen=True)
class AnonymousCarrier:
    """A carrier described only by its lawful internal register."""

    register: InternalRegister


def instantiate_null_carrier() -> AnonymousCarrier:
    """Instantiate one carrier at the null internal address."""
    return AnonymousCarrier(register=InternalRegister.NULL)


def extensional_catalogue(
    carriers: Iterable[AnonymousCarrier],
) -> Tuple[AnonymousCarrier, ...]:
    """Return the distinct carrier descriptions visible to TM-0.

    Equality is determined only by admitted structural content.
    """
    return tuple(sorted(set(carriers), key=lambda carrier: carrier.register.value))
