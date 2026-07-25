"""Construct the two-sheet cover of a finite signed simple graph.

For each signed base edge {u, v}:

    PRESERVE
        (u,0) -- (v,0)
        (u,1) -- (v,1)

    INVERT
        (u,0) -- (v,1)
        (u,1) -- (v,0)

The canonical deck involution swaps the two sheets over every base
vertex.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Hashable
from typing import Iterable
from typing import Tuple

from .local_sign_product import LocalSign


BaseVertex = Hashable
BaseEdge = Tuple[BaseVertex, BaseVertex]
LiftVertex = Tuple[BaseVertex, int]
LiftEdge = Tuple[LiftVertex, LiftVertex]


def canonical_base_edge(
    left: BaseVertex,
    right: BaseVertex,
) -> BaseEdge:
    if left == right:
        raise ValueError(
            "signed double cover does not support base loops"
        )

    return (
        (left, right)
        if repr(left) < repr(right)
        else (right, left)
    )


def canonical_lift_edge(
    left: LiftVertex,
    right: LiftVertex,
) -> LiftEdge:
    if left == right:
        raise ValueError(
            "signed double cover does not support lift loops"
        )

    return (
        (left, right)
        if repr(left) < repr(right)
        else (right, left)
    )


@dataclass(frozen=True)
class LiftEdgeRecord:
    base_edge: BaseEdge
    sign: LocalSign
    lift_edge: LiftEdge
    lift_type: str


@dataclass(frozen=True)
class SignedDoubleCover:
    base_vertices: Tuple[BaseVertex, ...]
    base_edges: Tuple[BaseEdge, ...]
    base_signs: Dict[BaseEdge, LocalSign]
    lift_vertices: Tuple[LiftVertex, ...]
    lift_edges: Tuple[LiftEdge, ...]
    edge_records: Tuple[LiftEdgeRecord, ...]

    def sheet_swap(
        self,
        vertex: LiftVertex,
    ) -> LiftVertex:
        base_vertex, sheet = vertex

        if sheet not in (0, 1):
            raise ValueError(
                "lift sheet must be 0 or 1"
            )

        return (
            base_vertex,
            1 - sheet,
        )

    def sheet_swap_orbits(
        self,
    ) -> Tuple[Tuple[LiftVertex, LiftVertex], ...]:
        return tuple(
            (
                (vertex, 0),
                (vertex, 1),
            )
            for vertex in self.base_vertices
        )


def construct_signed_double_cover(
    base_vertices: Iterable[BaseVertex],
    base_edges: Iterable[BaseEdge],
    signs: Dict[BaseEdge, LocalSign],
) -> SignedDoubleCover:
    vertices = tuple(
        sorted(
            set(base_vertices),
            key=repr,
        )
    )

    if not vertices:
        raise ValueError(
            "signed double cover requires base vertices"
        )

    vertex_set = set(vertices)

    edges = tuple(
        sorted(
            {
                canonical_base_edge(left, right)
                for left, right in base_edges
            },
            key=repr,
        )
    )

    edge_set = set(edges)

    for left, right in edges:
        if left not in vertex_set or right not in vertex_set:
            raise ValueError(
                "base edge uses an unregistered vertex"
            )

    canonical_signs = {
        canonical_base_edge(left, right): sign
        for (left, right), sign in signs.items()
    }

    if set(canonical_signs) != edge_set:
        raise ValueError(
            "one sign is required per base edge"
        )

    lift_vertices = tuple(
        (
            vertex,
            sheet,
        )
        for vertex in vertices
        for sheet in (0, 1)
    )

    records = []

    for base_edge in edges:
        left, right = base_edge
        sign = canonical_signs[base_edge]

        if sign is LocalSign.PRESERVE:
            lifted_pairs = (
                (
                    (left, 0),
                    (right, 0),
                ),
                (
                    (left, 1),
                    (right, 1),
                ),
            )
            lift_type = "parallel"

        elif sign is LocalSign.INVERT:
            lifted_pairs = (
                (
                    (left, 0),
                    (right, 1),
                ),
                (
                    (left, 1),
                    (right, 0),
                ),
            )
            lift_type = "crossed"

        else:
            raise ValueError(
                "base sign must be PRESERVE or INVERT"
            )

        for lift_left, lift_right in lifted_pairs:
            records.append(
                LiftEdgeRecord(
                    base_edge=base_edge,
                    sign=sign,
                    lift_edge=canonical_lift_edge(
                        lift_left,
                        lift_right,
                    ),
                    lift_type=lift_type,
                )
            )

    lift_edges = tuple(
        sorted(
            {
                record.lift_edge
                for record in records
            },
            key=repr,
        )
    )

    if len(lift_edges) != len(records):
        raise ValueError(
            "signed lift produced duplicate lift edges"
        )

    return SignedDoubleCover(
        base_vertices=vertices,
        base_edges=edges,
        base_signs=canonical_signs,
        lift_vertices=lift_vertices,
        lift_edges=lift_edges,
        edge_records=tuple(records),
    )
