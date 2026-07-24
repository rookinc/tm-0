"""Relational-position experiment for TM-0.

A situated carrier is described by:

1. its anonymous continuity trace;
2. the anonymous traces in its immediate relational neighborhood.

No names, identifiers, coordinates, timestamps, or implementation
object identity are admitted.

Two identical carrier histories may become distinguishable when their
relational neighborhoods differ.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple

from .continuity import ContinuityTrace


def canonical_neighbors(
    neighbors: Iterable[ContinuityTrace],
) -> Tuple[ContinuityTrace, ...]:
    """Return a deterministic neighborhood multiset representation."""
    return tuple(
        sorted(
            neighbors,
            key=lambda trace: tuple(state.value for state in trace.states),
        )
    )


@dataclass(frozen=True)
class RelationalProfile:
    """An anonymous carrier history viewed through its neighborhood."""

    center: ContinuityTrace
    neighbors: Tuple[ContinuityTrace, ...]

    @classmethod
    def from_parts(
        cls,
        center: ContinuityTrace,
        neighbors: Iterable[ContinuityTrace],
    ) -> "RelationalProfile":
        return cls(
            center=center,
            neighbors=canonical_neighbors(neighbors),
        )

    @property
    def degree(self) -> int:
        return len(self.neighbors)
