"""Switching classification for one connected signed graph.

Two sign assignments are switching-equivalent when their spanning-tree
normal forms have the same chord signs.
"""

from typing import Dict
from typing import Tuple

from .graph_switching_normal_form import Edge
from .graph_switching_normal_form import Vertex
from .graph_switching_normal_form import normalize_signed_graph
from .local_sign_product import LocalSign


def graph_switching_signature(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
) -> Tuple[Tuple[Edge, LocalSign], ...]:
    result = normalize_signed_graph(edges, signs, root)

    return tuple(
        (
            edge,
            result.normalized_signs[edge],
        )
        for edge in result.chord_edges
    )


def graph_switching_equivalent(
    edges: Tuple[Edge, ...],
    source: Dict[Edge, LocalSign],
    target: Dict[Edge, LocalSign],
    root: Vertex,
) -> bool:
    return graph_switching_signature(
        edges,
        source,
        root,
    ) == graph_switching_signature(
        edges,
        target,
        root,
    )
