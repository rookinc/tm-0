"""Construct a finite quotient graph from a carrier graph and partition.

The partition determines which carrier vertices are identified.

The quotient graph records:

    quotient vertices
    quotient edges
    carrier-edge to quotient-edge mapping
    covering multiplicity of each quotient edge

The constructor rejects carrier edges whose endpoints lie in the same
equivalence class because the current contract does not admit loops.
"""

from dataclasses import dataclass
from typing import Dict
from typing import FrozenSet
from typing import Iterable
from typing import Tuple


Vertex = str
CarrierEdge = Tuple[Vertex, Vertex]
QuotientVertex = int
QuotientEdge = Tuple[QuotientVertex, QuotientVertex]
Partition = Tuple[Tuple[Vertex, ...], ...]


def canonical_edge(
    left,
    right,
):
    if left == right:
        raise ValueError(
            "graph edge endpoints must be distinct"
        )

    return (
        (left, right)
        if left < right
        else (right, left)
    )


def canonical_carrier_edges(
    edges: Iterable[CarrierEdge],
) -> Tuple[CarrierEdge, ...]:
    return tuple(
        sorted({
            canonical_edge(left, right)
            for left, right in edges
        })
    )


def canonical_partition(
    carrier: FrozenSet[Vertex],
    classes: Iterable[Iterable[Vertex]],
) -> Partition:
    normalized = tuple(
        sorted(
            tuple(sorted(equivalence_class))
            for equivalence_class in classes
        )
    )

    if not normalized:
        raise ValueError(
            "quotient partition must contain classes"
        )

    if any(
        not equivalence_class
        for equivalence_class in normalized
    ):
        raise ValueError(
            "quotient classes must not be empty"
        )

    flattened = tuple(
        vertex
        for equivalence_class in normalized
        for vertex in equivalence_class
    )

    if len(flattened) != len(set(flattened)):
        raise ValueError(
            "quotient classes must be disjoint"
        )

    if frozenset(flattened) != carrier:
        raise ValueError(
            "quotient partition must cover the carrier"
        )

    return normalized


@dataclass(frozen=True)
class QuotientGraph:
    carrier_vertices: FrozenSet[Vertex]
    carrier_edges: Tuple[CarrierEdge, ...]
    partition: Partition
    quotient_vertices: Tuple[QuotientVertex, ...]
    quotient_edges: Tuple[QuotientEdge, ...]
    edge_map: Tuple[
        Tuple[CarrierEdge, QuotientEdge],
        ...,
    ]

    def covering_multiplicities(
        self,
    ) -> Dict[QuotientEdge, int]:
        counts = {
            edge: 0
            for edge in self.quotient_edges
        }

        for _, quotient_edge in self.edge_map:
            counts[quotient_edge] += 1

        return counts


def construct_quotient_graph(
    carrier_vertices: Iterable[Vertex],
    carrier_edges: Iterable[CarrierEdge],
    classes: Iterable[Iterable[Vertex]],
) -> QuotientGraph:
    carrier = frozenset(carrier_vertices)

    if not carrier:
        raise ValueError(
            "carrier must not be empty"
        )

    edges = canonical_carrier_edges(
        carrier_edges
    )

    for left, right in edges:
        if left not in carrier or right not in carrier:
            raise ValueError(
                "carrier edge uses an unregistered vertex"
            )

    partition = canonical_partition(
        carrier,
        classes,
    )

    class_index = {
        vertex: index
        for index, equivalence_class in enumerate(
            partition
        )
        for vertex in equivalence_class
    }

    edge_map = []

    for carrier_edge in edges:
        left, right = carrier_edge

        quotient_left = class_index[left]
        quotient_right = class_index[right]

        if quotient_left == quotient_right:
            raise ValueError(
                "carrier edge collapses to a quotient loop"
            )

        quotient_edge = canonical_edge(
            quotient_left,
            quotient_right,
        )

        edge_map.append(
            (
                carrier_edge,
                quotient_edge,
            )
        )

    quotient_edges = tuple(
        sorted({
            quotient_edge
            for _, quotient_edge in edge_map
        })
    )

    quotient_vertices = tuple(
        range(len(partition))
    )

    return QuotientGraph(
        carrier_vertices=carrier,
        carrier_edges=edges,
        partition=partition,
        quotient_vertices=quotient_vertices,
        quotient_edges=quotient_edges,
        edge_map=tuple(edge_map),
    )
