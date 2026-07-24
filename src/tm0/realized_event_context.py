"""Derive witness context from a realized event record.

A realized event records:

    source state
    target state
    traversed relation
    boundary contacts
    cycle residue

The boundary signature and binary character are derived from that
record before constructing the witness context.

This is a bounded execution-derived context scaffold.
"""

from dataclasses import dataclass
from typing import Tuple

from .derived_witness_context import WitnessContext
from .derived_witness_context import derive_witness_context


StateName = str
RelationName = str
BoundaryContact = str
BoundaryContacts = Tuple[BoundaryContact, ...]
CycleResidue = Tuple[int, ...]


@dataclass(frozen=True)
class RealizedEvent:
    source_state: StateName
    target_state: StateName
    traversed_relation: RelationName
    boundary_contacts: BoundaryContacts
    cycle_residue: CycleResidue


def validate_realized_event(
    event: RealizedEvent,
) -> RealizedEvent:
    if not event.source_state:
        raise ValueError("source state must not be empty")

    if not event.target_state:
        raise ValueError("target state must not be empty")

    if not event.traversed_relation:
        raise ValueError("traversed relation must not be empty")

    if not event.boundary_contacts:
        raise ValueError("boundary contacts must not be empty")

    if any(not contact for contact in event.boundary_contacts):
        raise ValueError("boundary contacts must not contain empty values")

    if len(set(event.boundary_contacts)) != len(
        event.boundary_contacts
    ):
        raise ValueError("boundary contacts must be unique")

    if not event.cycle_residue:
        raise ValueError("cycle residue must not be empty")

    if any(bit not in (0, 1) for bit in event.cycle_residue):
        raise ValueError("cycle residue must be binary")

    return event


def derive_boundary_signature(
    event: RealizedEvent,
) -> Tuple[str, ...]:
    validate_realized_event(event)

    transition = (
        f"transition:{event.source_state}"
        f"->{event.target_state}"
    )

    relation = f"relation:{event.traversed_relation}"

    contacts = tuple(
        f"contact:{contact}"
        for contact in event.boundary_contacts
    )

    return (
        transition,
        relation,
        *contacts,
    )


def derive_event_character(
    event: RealizedEvent,
) -> Tuple[int, ...]:
    validate_realized_event(event)

    changed_state = int(
        event.source_state != event.target_state
    )

    crossed_boundary = int(
        bool(event.boundary_contacts)
    )

    return (
        changed_state,
        crossed_boundary,
        *event.cycle_residue,
    )


def derive_context_from_realized_event(
    event: RealizedEvent,
) -> WitnessContext:
    return derive_witness_context(
        boundary_signature=derive_boundary_signature(event),
        character=derive_event_character(event),
    )
