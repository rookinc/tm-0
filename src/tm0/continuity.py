"""Continuity experiment for TM-0.

A carrier history is represented only by an ordered chain of lawful
internal register states.

No name, identifier, coordinate, timestamp, or Python object identity
is admitted as mechanical structure.

A later history continues an earlier history when the earlier history
is an exact prefix of the later one.
"""

from dataclasses import dataclass
from typing import Tuple

from .carrier_register import InternalRegister


@dataclass(frozen=True)
class ContinuityTrace:
    """An anonymous ordered history of internal register states."""

    states: Tuple[InternalRegister, ...]

    def __post_init__(self) -> None:
        if not self.states:
            raise ValueError("a continuity trace must contain a state")

    @property
    def current(self) -> InternalRegister:
        return self.states[-1]


def begin_null_trace() -> ContinuityTrace:
    """Begin one anonymous carrier history at NULL."""
    return ContinuityTrace(states=(InternalRegister.NULL,))


def extend_trace(
    trace: ContinuityTrace,
    next_state: InternalRegister,
) -> ContinuityTrace:
    """Extend a trace by one non-identity internal realization."""
    if next_state is trace.current:
        raise ValueError(
            "identity transition does not extend continuity: "
            f"{trace.current.value} -> {next_state.value}"
        )

    return ContinuityTrace(states=trace.states + (next_state,))


def continues(
    earlier: ContinuityTrace,
    later: ContinuityTrace,
) -> bool:
    """Return whether later contains earlier as an exact prefix."""
    prefix_length = len(earlier.states)

    return (
        len(later.states) >= prefix_length
        and later.states[:prefix_length] == earlier.states
    )
