"""Closure visibility experiment for TM-0.

This experiment compares two rooted directed structures:

1. an open directed path;
2. a closed directed cycle.

The root has the same anonymous local incoming/outgoing profile in both
structures.

Fixture handles are used only by the test apparatus to construct edge
incidence. They are not included in the projected TM-0 local profile
and are not promoted as intrinsic identity.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple

from .continuity import ContinuityTrace
from .directed_relation import DirectedRelationalProfile


Edge = Tuple[str, str]


@dataclass(frozen=True)
class DirectedIncidenceFixture:
    """A finite directed incidence structure used by the apparatus."""

    root: str
    edges: Tuple[Edge, ...]
    trace: ContinuityTrace

    @classmethod
    def from_edges(
        cls,
        root: str,
        edges: Iterable[Edge],
        trace: ContinuityTrace,
    ) -> "DirectedIncidenceFixture":
        return cls(
            root=root,
            edges=tuple(edges),
            trace=trace,
        )

    def incoming_handles(self, handle: str) -> Tuple[str, ...]:
        return tuple(
            source
            for source, target in self.edges
            if target == handle
        )

    def outgoing_handles(self, handle: str) -> Tuple[str, ...]:
        return tuple(
            target
            for source, target in self.edges
            if source == handle
        )

    def local_profile(self) -> DirectedRelationalProfile:
        """Project the root to an anonymous radius-one role profile."""
        incoming = [
            self.trace
            for _ in self.incoming_handles(self.root)
        ]
        outgoing = [
            self.trace
            for _ in self.outgoing_handles(self.root)
        ]

        return DirectedRelationalProfile.from_parts(
            center=self.trace,
            incoming=incoming,
            outgoing=outgoing,
        )

    def root_has_nonempty_return(self) -> bool:
        """Return whether a positive-length directed path returns to root."""
        frontier = list(self.outgoing_handles(self.root))
        visited = set()

        while frontier:
            handle = frontier.pop()

            if handle == self.root:
                return True

            if handle in visited:
                continue

            visited.add(handle)
            frontier.extend(self.outgoing_handles(handle))

        return False
