"""Anonymous endpoint-incidence experiment for TM-0.

Relations carry only local source and target ports.

Incidence is represented by equivalence between ports belonging to
different relations.

No carrier names, vertex names, coordinates, timestamps, or persistent
carrier identifiers are admitted.

Closure occurs when:

1. each target port composes with the next source port; and
2. the final target port is equivalent to the first source port.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple


Port = Tuple[int, str]
PortEquality = Tuple[Port, Port]


@dataclass(frozen=True)
class AnonymousRelation:
    """One directed relation with relation-local endpoint positions."""

    index: int

    @property
    def source(self) -> Port:
        return (self.index, "source")

    @property
    def target(self) -> Port:
        return (self.index, "target")


class EndpointEquivalence:
    """Finite equivalence relation over relation-local ports."""

    def __init__(self, equalities: Iterable[PortEquality]) -> None:
        self._parent: dict[Port, Port] = {}

        for left, right in equalities:
            self._union(left, right)

    def _find(self, port: Port) -> Port:
        self._parent.setdefault(port, port)

        parent = self._parent[port]

        if parent != port:
            self._parent[port] = self._find(parent)

        return self._parent[port]

    def _union(self, left: Port, right: Port) -> None:
        left_root = self._find(left)
        right_root = self._find(right)

        if left_root != right_root:
            self._parent[right_root] = left_root

    def equivalent(self, left: Port, right: Port) -> bool:
        """Return whether two endpoint positions share one junction."""
        return self._find(left) == self._find(right)


def anonymous_relations(count: int) -> Tuple[AnonymousRelation, ...]:
    """Construct an ordered sequence of anonymous directed relations."""
    if count < 1:
        raise ValueError("at least one relation is required")

    return tuple(AnonymousRelation(index=index) for index in range(count))


def composition_equalities(
    relations: Tuple[AnonymousRelation, ...],
) -> Tuple[PortEquality, ...]:
    """Return endpoint equalities required for sequential composition."""
    return tuple(
        (relations[index].target, relations[index + 1].source)
        for index in range(len(relations) - 1)
    )


def is_composable(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
) -> bool:
    """Return whether every adjacent pair composes."""
    return all(
        incidence.equivalent(
            relations[index].target,
            relations[index + 1].source,
        )
        for index in range(len(relations) - 1)
    )


def is_closed(
    relations: Tuple[AnonymousRelation, ...],
    incidence: EndpointEquivalence,
) -> bool:
    """Return whether a composable sequence returns to its first port."""
    return (
        is_composable(relations, incidence)
        and incidence.equivalent(
            relations[-1].target,
            relations[0].source,
        )
    )
