"""Anonymous occurrence ledger for TM-0.

Carrier states remain anonymous and extensionally equal.

Plurality is represented only by the multiplicity of lawful
instantiation occurrences. No names, persistent identifiers,
coordinates, relations, or implementation object identity are
admitted as carrier structure.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple

from .carrier_plurality import AnonymousCarrier, instantiate_null_carrier


@dataclass(frozen=True)
class InstantiationOccurrence:
    """One anonymous realization of a null carrier."""

    result: AnonymousCarrier


def instantiate_occurrence() -> InstantiationOccurrence:
    """Record one lawful null-carrier instantiation."""
    return InstantiationOccurrence(result=instantiate_null_carrier())


def occurrence_ledger(
    occurrences: Iterable[InstantiationOccurrence],
) -> Tuple[InstantiationOccurrence, ...]:
    """Preserve occurrence multiplicity without naming carriers."""
    return tuple(occurrences)


def resulting_carrier_catalogue(
    occurrences: Iterable[InstantiationOccurrence],
) -> Tuple[AnonymousCarrier, ...]:
    """Return distinct resulting carrier descriptions."""
    return tuple(
        sorted(
            {occurrence.result for occurrence in occurrences},
            key=lambda carrier: carrier.register.value,
        )
    )
