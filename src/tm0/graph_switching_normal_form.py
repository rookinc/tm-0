"""Switching normal form for a connected signed graph.

A vertex switch changes the sign of every incident edge.

The normalization makes every spanning-tree edge positive.
The remaining chord signs record the independent cycle products.
"""

from collections import deque
from dataclasses import dataclass
from typing import Dict
from typing import Tuple

from .local_sign_product import LocalSign


Vertex = str
Edge = Tuple[Vertex, Vertex]


@dataclass(frozen=True)
class GraphNormalForm:
    tree_edges: Tuple[Edge, ...]
    chord_edges: Tuple[Edge, ...]
    switches: Dict[Vertex, LocalSign]
    normalized_signs: Dict[Edge, LocalSign]


def canonical_edge(left: Vertex, right: Vertex) -> Edge:
    if left == right:
        raise ValueError("loops are not supported")

    return tuple(sorted((left, right)))


def normalize_signed_graph(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
) -> GraphNormalForm:
    canonical_edges = tuple(
        canonical_edge(left, right)
        for left, right in edges
    )

    edge_set = set(canonical_edges)

    if len(edge_set) != len(canonical_edges):
        raise ValueError("duplicate edges are not supported")

    if set(signs) != edge_set:
        raise ValueError("one sign is required per edge")

    adjacency = {}

    for left, right in canonical_edges:
        adjacency.setdefault(left, []).append(right)
        adjacency.setdefault(right, []).append(left)

    if root not in adjacency:
        raise ValueError("root must belong to the graph")

    switches = {root: LocalSign.PRESERVE}
    tree_edges = []
    queue = deque([root])

    while queue:
        parent = queue.popleft()

        for child in sorted(adjacency[parent]):
            if child in switches:
                continue

            edge = canonical_edge(parent, child)
            value = int(switches[parent]) * int(signs[edge])
            switches[child] = LocalSign(value)
            tree_edges.append(edge)
            queue.append(child)

    if set(switches) != set(adjacency):
        raise ValueError("graph must be connected")

    normalized_signs = {}

    for left, right in canonical_edges:
        edge = canonical_edge(left, right)
        value = (
            int(switches[left])
            * int(signs[edge])
            * int(switches[right])
        )
        normalized_signs[edge] = LocalSign(value)

    tree_edge_set = set(tree_edges)
    chord_edges = tuple(
        edge
        for edge in canonical_edges
        if edge not in tree_edge_set
    )

    return GraphNormalForm(
        tree_edges=tuple(tree_edges),
        chord_edges=chord_edges,
        switches=switches,
        normalized_signs=normalized_signs,
    )
