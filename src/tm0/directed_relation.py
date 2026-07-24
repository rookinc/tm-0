"""Directed relational-role experiment for TM-0.

A directed relational profile contains:

1. an anonymous center continuity trace;
2. anonymous incoming neighbor traces;
3. anonymous outgoing neighbor traces.

No names, identifiers, coordinates, timestamps, intrinsic A/B labels,
or implementation object identity are admitted.

Direction introduces source and target roles without assuming polarity
as an internal carrier value.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple

from .continuity import ContinuityTrace


def canonical_traces(
    traces: Iterable[ContinuityTrace],
) -> Tuple[ContinuityTrace, ...]:
    """Return a deterministic multiset representation."""
    return tuple(
        sorted(
            traces,
            key=lambda trace: tuple(state.value for state in trace.states),
        )
    )


@dataclass(frozen=True)
class DirectedRelationalProfile:
    """An anonymous continuity trace viewed through directed relations."""

    center: ContinuityTrace
    incoming: Tuple[ContinuityTrace, ...]
    outgoing: Tuple[ContinuityTrace, ...]

    @classmethod
    def from_parts(
        cls,
        center: ContinuityTrace,
        incoming: Iterable[ContinuityTrace],
        outgoing: Iterable[ContinuityTrace],
    ) -> "DirectedRelationalProfile":
        return cls(
            center=center,
            incoming=canonical_traces(incoming),
            outgoing=canonical_traces(outgoing),
        )

    @property
    def indegree(self) -> int:
        return len(self.incoming)

    @property
    def outdegree(self) -> int:
        return len(self.outgoing)

    @property
    def undirected_shadow(self) -> Tuple[ContinuityTrace, ...]:
        """Forget direction while preserving neighbor multiplicity."""
        return canonical_traces(self.incoming + self.outgoing)
