"""Derive the native thirty-state intermediate quotient from G60.

The retained source supplies only:

    native G60 vertices and edges
    native G15 fiber labels
    native V4 coordinates

TM-0 derives the order-two kernel orbits of:

    chi(x, y) = x xor y

Within each G15 fiber, adding (1, 1) pairs:

    (0,0) with (1,1)
    (0,1) with (1,0)

The resulting quotient is then compared with the independently retained
native cover class.

No expected G30 edge set is used as a construction input.
"""

import json
from collections import deque
from itertools import combinations
from pathlib import Path
from typing import Dict

from .finite_graph_isomorphism import (
    adjacency_map,
    find_graph_isomorphism,
)
from .petersen_line_graph import (
    petersen_line_graph_edges,
    petersen_line_graph_vertices,
)
from .project42_invariant_cover_square import (
    load_cover_square_certificate,
)
from .quotient_graph import construct_quotient_graph


SOURCE_PATH = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "project42"
    / "project42_native_g60_v4_source_certificate_034.json"
)


def load_native_g60_v4_source() -> dict:
    return json.loads(SOURCE_PATH.read_text())


def parity(coordinate) -> int:
    return int(coordinate[0]) ^ int(coordinate[1])


def triangle_count(vertices, edges) -> int:
    adjacency = adjacency_map(vertices, edges)
    count = 0

    for left, middle, right in combinations(vertices, 3):
        if (
            middle in adjacency[left]
            and right in adjacency[left]
            and right in adjacency[middle]
        ):
            count += 1

    return count


def component_sizes(vertices, edges):
    adjacency = adjacency_map(vertices, edges)
    unseen = set(vertices)
    sizes = []

    while unseen:
        root = min(unseen)
        queue = deque([root])
        seen = {root}
        unseen.remove(root)

        while queue:
            vertex = queue.popleft()

            for neighbor in adjacency[vertex]:
                if neighbor in seen:
                    continue

                seen.add(neighbor)
                unseen.remove(neighbor)
                queue.append(neighbor)

        sizes.append(len(seen))

    return tuple(sorted(sizes))


def derive_native_g30_intermediate_quotient() -> Dict[str, object]:
    source = load_native_g60_v4_source()

    if not source["audit_pass"]:
        raise ValueError(
            "native G60 V4 source certificate did not pass"
        )

    state_rows = source["state_rows"]

    state_to_base = {
        int(row["g60_state"]): int(row["g15_state"])
        for row in state_rows
    }

    state_to_coordinate = {
        int(row["g60_state"]): tuple(
            int(value)
            for value in row["v4_coordinate"]
        )
        for row in state_rows
    }

    g60_vertices = tuple(
        sorted(state_to_base)
    )

    g60_edges = tuple(
        tuple(edge)
        for edge in source["g60_edges"]
    )

    orbit_members = {}

    for state in g60_vertices:
        key = (
            state_to_base[state],
            parity(state_to_coordinate[state]),
        )

        orbit_members.setdefault(key, []).append(state)

    kernel_classes = tuple(
        tuple(sorted(members))
        for _, members in sorted(orbit_members.items())
    )

    g30 = construct_quotient_graph(
        carrier_vertices=g60_vertices,
        carrier_edges=g60_edges,
        classes=kernel_classes,
    )

    orbit_index_to_base = {
        orbit_index: state_to_base[members[0]]
        for orbit_index, members in enumerate(g30.partition)
    }

    residual_classes = []

    for base in sorted(set(state_to_base.values())):
        residual_class = tuple(
            sorted(
                orbit_index
                for orbit_index, orbit_base
                in orbit_index_to_base.items()
                if orbit_base == base
            )
        )

        residual_classes.append(residual_class)

    g15_residual = construct_quotient_graph(
        carrier_vertices=g30.quotient_vertices,
        carrier_edges=g30.quotient_edges,
        classes=tuple(residual_classes),
    )

    direct_state_to_g15 = dict(state_to_base)

    composite_state_to_g15 = {}

    for orbit_index, members in enumerate(g30.partition):
        residual_index = next(
            index
            for index, residual_class
            in enumerate(g15_residual.partition)
            if orbit_index in residual_class
        )

        for state in members:
            composite_state_to_g15[state] = residual_index

    quotient_square_commutes = all(
        direct_state_to_g15[state]
        == composite_state_to_g15[state]
        for state in g60_vertices
    )

    g30_adjacency = adjacency_map(
        g30.quotient_vertices,
        g30.quotient_edges,
    )

    g30_degree_profile = tuple(
        sorted({
            len(neighbors)
            for neighbors in g30_adjacency.values()
        })
    )

    cover_square = load_cover_square_certificate()

    native_class = next(
        row
        for row in cover_square["classes"]
        if row["class_id"] == "native"
    )

    native_mapping = find_graph_isomorphism(
        left_vertices=g30.quotient_vertices,
        left_edges=g30.quotient_edges,
        right_vertices=tuple(
            range(native_class["cover_vertex_count"])
        ),
        right_edges=tuple(
            tuple(edge)
            for edge in native_class["cover_edges"]
        ),
    )

    residual_lp_mapping = find_graph_isomorphism(
        left_vertices=g15_residual.quotient_vertices,
        left_edges=g15_residual.quotient_edges,
        right_vertices=petersen_line_graph_vertices(),
        right_edges=petersen_line_graph_edges(),
    )

    return {
        "source_certificate_id": source["certificate_id"],
        "source_audit_pass": source["audit_pass"],
        "g60_vertex_count": len(g60_vertices),
        "g60_edge_count": len(g60_edges),
        "kernel_orbit_count": len(kernel_classes),
        "kernel_orbit_size_profile": tuple(
            sorted({
                len(members)
                for members in kernel_classes
            })
        ),
        "g30_vertex_count": len(g30.quotient_vertices),
        "g30_edge_count": len(g30.quotient_edges),
        "g60_to_g30_edge_multiplicity_profile": tuple(
            sorted(set(
                g30.covering_multiplicities().values()
            ))
        ),
        "g30_degree_profile": g30_degree_profile,
        "g30_component_sizes": component_sizes(
            g30.quotient_vertices,
            g30.quotient_edges,
        ),
        "g30_triangle_count": triangle_count(
            g30.quotient_vertices,
            g30.quotient_edges,
        ),
        "native_cover_isomorphic": native_mapping is not None,
        "native_cover_mapping_size": (
            0 if native_mapping is None else len(native_mapping)
        ),
        "native_cover_mapping": native_mapping,
        "residual_class_count": len(residual_classes),
        "residual_class_size_profile": tuple(
            sorted({
                len(residual_class)
                for residual_class in residual_classes
            })
        ),
        "g15_vertex_count": len(
            g15_residual.quotient_vertices
        ),
        "g15_edge_count": len(
            g15_residual.quotient_edges
        ),
        "g30_to_g15_edge_multiplicity_profile": tuple(
            sorted(set(
                g15_residual.covering_multiplicities().values()
            ))
        ),
        "residual_isomorphic_to_LP": (
            residual_lp_mapping is not None
        ),
        "residual_LP_mapping_size": (
            0
            if residual_lp_mapping is None
            else len(residual_lp_mapping)
        ),
        "quotient_square_commutes": quotient_square_commutes,
        "kernel_classes": g30.partition,
        "g30_edges": g30.quotient_edges,
        "residual_classes": g15_residual.partition,
        "g15_edges": g15_residual.quotient_edges,
    }
