"""Classify the retained aligned G15 cocycle candidate.

This layer verifies:

    support is isomorphic to L(Petersen)
    switching signature length equals cycle rank
    explicit local switching preserves the signature

It classifies the executable signed character only.

It does not establish native G60 origin.
"""

from typing import Dict

from .aligned_g15_cocycle import (
    canonical_edge,
    ingest_aligned_g15_cocycle,
)
from .finite_graph_isomorphism import (
    find_graph_isomorphism,
)
from .graph_switching_classification import (
    graph_switching_signature,
)
from .local_sign_product import LocalSign
from .petersen_line_graph import (
    petersen_line_graph_edges,
    petersen_line_graph_vertices,
)


def switch_graph_signs(
    edges,
    signs,
    switches,
):
    transformed = {}

    for left, right in edges:
        edge = canonical_edge(left, right)

        value = (
            int(switches[left])
            * int(signs[edge])
            * int(switches[right])
        )

        transformed[edge] = LocalSign(value)

    return transformed


def classify_aligned_g15_cocycle() -> Dict[str, object]:
    cocycle = ingest_aligned_g15_cocycle()

    support_mapping = find_graph_isomorphism(
        left_vertices=cocycle.vertices,
        left_edges=cocycle.edges,
        right_vertices=petersen_line_graph_vertices(),
        right_edges=petersen_line_graph_edges(),
    )

    vertex_count = len(cocycle.vertices)
    edge_count = len(cocycle.edges)
    component_count = 1
    cycle_rank = (
        edge_count
        - vertex_count
        + component_count
    )

    root = min(cocycle.vertices)

    signature = graph_switching_signature(
        edges=cocycle.edges,
        signs=cocycle.signs,
        root=root,
    )

    negative_chord_count = sum(
        1
        for _, sign in signature
        if sign is LocalSign.INVERT
    )

    switches = {
        vertex: (
            LocalSign.INVERT
            if int(vertex) % 2
            else LocalSign.PRESERVE
        )
        for vertex in cocycle.vertices
    }

    switched_signs = switch_graph_signs(
        edges=cocycle.edges,
        signs=cocycle.signs,
        switches=switches,
    )

    switched_signature = graph_switching_signature(
        edges=cocycle.edges,
        signs=switched_signs,
        root=root,
    )

    return {
        "source_status": cocycle.source_status,
        "provenance_classification": (
            cocycle.provenance_classification
        ),
        "vertex_count": vertex_count,
        "edge_count": edge_count,
        "component_count": component_count,
        "cycle_rank": cycle_rank,
        "support_isomorphic_to_LP": (
            support_mapping is not None
        ),
        "support_mapping_size": (
            0
            if support_mapping is None
            else len(support_mapping)
        ),
        "switching_signature": signature,
        "switching_signature_length": len(signature),
        "negative_chord_count": negative_chord_count,
        "explicit_switch_count": sum(
            1
            for sign in switches.values()
            if sign is LocalSign.INVERT
        ),
        "switched_signature": switched_signature,
        "switching_invariant": (
            signature == switched_signature
        ),
        "support_mapping": support_mapping,
    }
