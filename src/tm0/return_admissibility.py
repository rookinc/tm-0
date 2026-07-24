"""Return-admissibility experiment for TM-0.

Closure and return are kept distinct.

Closure is an incidence condition:

    final target junction = first source junction

A closed chain admits return.

Return is realized only when the closed chain is traversed and a
return receipt is produced.

No agency, automatic execution, time, geometry, or physical motion is
assumed.
"""

from dataclasses import dataclass
from typing import Tuple

from .incidence_equivalence import (
    AnonymousRelation,
    EndpointEquivalence,
    Port,
    is_closed,
)


@dataclass(frozen=True)
class ReturnReceipt:
    """Receipt for one realized traversal of a closed relation chain."""

    relation_order: Tuple[int, ...]
    departure_port: Port
    return_port: Port

    @property
    def completed(self) -> bool:
        return bool(self.relation_order)


def return_is_admissible(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
) -> bool:
    """Return whether closure makes return a lawful continuation."""
    return is_closed(relations, incidence)


def realize_return(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
) -> ReturnReceipt:
    """Realize one return through a closed composable chain."""
    if not return_is_admissible(relations, incidence):
        raise ValueError("return is not admissible without closure")

    return ReturnReceipt(
        relation_order=tuple(
            relation.index
            for relation in relations
        ),
        departure_port=relations[0].source,
        return_port=relations[-1].target,
    )


def receipt_confirms_return(
    receipt: ReturnReceipt,
    incidence: EndpointEquivalence,
) -> bool:
    """Confirm that the receipt ends at its departure junction."""
    return (
        receipt.completed
        and incidence.equivalent(
            receipt.return_port,
            receipt.departure_port,
        )
    )
