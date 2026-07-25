"""Construct and classify the aligned G15 signed double cover.

This module:

    ingests the retained aligned G15 signing
    constructs its two-sheet signed double cover
    verifies the canonical sheet swap
    verifies switching-equivalent signings produce isomorphic lifts

Cover-square membership is classified separately in:

    project42_invariant_cover_square

This module does not establish native G60 origin.
"""

from collections import deque
from typing import Dict

from .aligned_g15_cocycle import ingest_aligned_g15_cocycle
from .aligned_g15_cocycle_character import switch_graph_signs
from .finite_graph_isomorphism import (
    adjacency_map,
    find_graph_isomorphism,
)
from .local_sign_product import LocalSign
from .signed_double_cover import construct_signed_double_cover


def classify_aligned_g15_signed_double_cover() -> Dict[str, object]:
    cocycle = ingest_aligned_g15_cocycle()

    cover = construct_signed_double_cover(
        base_vertices=cocycle.vertices,
        base_edges=cocycle.edges,
        signs=cocycle.signs,
    )

    lift_adjacency = adjacency_map(
        cover.lift_vertices,
        cover.lift_edges,
    )

    degree_profile = tuple(
        sorted({
            len(neighbors)
            for neighbors in lift_adjacency.values()
        })
    )

    unseen = set(cover.lift_vertices)
    component_sizes = []

    while unseen:
        root = min(unseen, key=repr)
        queue = deque([root])
        seen = {root}
        unseen.remove(root)

        while queue:
            vertex = queue.popleft()

            for neighbor in lift_adjacency[vertex]:
                if neighbor in seen:
                    continue

                seen.add(neighbor)
                unseen.remove(neighbor)
                queue.append(neighbor)

        component_sizes.append(len(seen))

    component_sizes = tuple(sorted(component_sizes))
    lift_edge_set = set(cover.lift_edges)

    sheet_swap_preserves_edges = all(
        tuple(
            sorted(
                (
                    cover.sheet_swap(left),
                    cover.sheet_swap(right),
                ),
                key=repr,
            )
        )
        in lift_edge_set
        for left, right in cover.lift_edges
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

    switched_cover = construct_signed_double_cover(
        base_vertices=cocycle.vertices,
        base_edges=cocycle.edges,
        signs=switched_signs,
    )

    switched_cover_mapping = find_graph_isomorphism(
        left_vertices=cover.lift_vertices,
        left_edges=cover.lift_edges,
        right_vertices=switched_cover.lift_vertices,
        right_edges=switched_cover.lift_edges,
    )

    parallel_base_edge_count = sum(
        1
        for sign in cocycle.signs.values()
        if sign is LocalSign.PRESERVE
    )

    crossed_base_edge_count = sum(
        1
        for sign in cocycle.signs.values()
        if sign is LocalSign.INVERT
    )

    explicit_switch_count = sum(
        1
        for sign in switches.values()
        if sign is LocalSign.INVERT
    )

    return {
        "source_status": cocycle.source_status,
        "provenance_classification": (
            cocycle.provenance_classification
        ),
        "base_vertex_count": len(cover.base_vertices),
        "base_edge_count": len(cover.base_edges),
        "parallel_base_edge_count": parallel_base_edge_count,
        "crossed_base_edge_count": crossed_base_edge_count,
        "lift_vertex_count": len(cover.lift_vertices),
        "lift_edge_count": len(cover.lift_edges),
        "degree_profile": degree_profile,
        "component_count": len(component_sizes),
        "component_sizes": component_sizes,
        "sheet_swap_orbit_count": len(
            cover.sheet_swap_orbits()
        ),
        "sheet_swap_preserves_edges": (
            sheet_swap_preserves_edges
        ),
        "explicit_switch_count": explicit_switch_count,
        "switched_cover_isomorphic": (
            switched_cover_mapping is not None
        ),
        "switched_cover_mapping_size": (
            0
            if switched_cover_mapping is None
            else len(switched_cover_mapping)
        ),
        "switched_cover_mapping": switched_cover_mapping,
    }
