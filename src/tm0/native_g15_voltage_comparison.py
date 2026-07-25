"""Compare the aligned G15 signing with the G60-derived native voltage.

The native certificate derives its Z2 voltage independently from:

    native G60 edge lifts
    native V4 fiber coordinates
    translation-delta parity

The aligned signing need not equal that voltage edge-for-edge after a
graph relabeling. A transported representative may also differ by local
vertex switching.

This module therefore searches for:

    one unsigned G15 graph isomorphism
    one vertex-switch assignment

such that every transported aligned edge bit equals the native bit.
"""

import json
from pathlib import Path
from typing import Dict
from typing import Optional
from typing import Tuple

from .aligned_g15_cocycle import ingest_aligned_g15_cocycle
from .finite_graph_isomorphism import adjacency_map


CERTIFICATE_PATH = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "project42"
    / "project42_native_voltage_derivation_certificate_033.json"
)


def load_native_voltage_certificate() -> dict:
    return json.loads(
        CERTIFICATE_PATH.read_text()
    )


def canonical_edge(left, right):
    if left == right:
        raise ValueError("signed graph does not admit loops")

    return (
        (left, right)
        if repr(left) < repr(right)
        else (right, left)
    )


def solve_switches_for_mapping(
    left_vertices,
    left_edges,
    left_bits,
    right_bits,
    mapping,
) -> Optional[Dict[object, int]]:
    adjacency = adjacency_map(
        left_vertices,
        left_edges,
    )

    switches = {}

    for root in left_vertices:
        if root in switches:
            continue

        switches[root] = 0
        stack = [root]

        while stack:
            left = stack.pop()

            for right in adjacency[left]:
                left_edge = canonical_edge(left, right)
                mapped_edge = canonical_edge(
                    mapping[left],
                    mapping[right],
                )

                required_right_switch = (
                    switches[left]
                    ^ left_bits[left_edge]
                    ^ right_bits[mapped_edge]
                )

                if right in switches:
                    if switches[right] != required_right_switch:
                        return None
                    continue

                switches[right] = required_right_switch
                stack.append(right)

    return switches


def find_switching_signed_isomorphism(
    left_vertices,
    left_edges,
    left_bits,
    right_vertices,
    right_edges,
    right_bits,
) -> Optional[Tuple[Dict[object, object], Dict[object, int]]]:
    left_adjacency = adjacency_map(
        left_vertices,
        left_edges,
    )
    right_adjacency = adjacency_map(
        right_vertices,
        right_edges,
    )

    if len(left_adjacency) != len(right_adjacency):
        return None

    if len(left_edges) != len(right_edges):
        return None

    mapping = {}
    used_right = set()

    def candidates(left_vertex):
        degree = len(left_adjacency[left_vertex])
        result = []

        for right_vertex in right_adjacency:
            if right_vertex in used_right:
                continue

            if len(right_adjacency[right_vertex]) != degree:
                continue

            compatible = True

            for mapped_left, mapped_right in mapping.items():
                left_is_adjacent = (
                    mapped_left
                    in left_adjacency[left_vertex]
                )
                right_is_adjacent = (
                    mapped_right
                    in right_adjacency[right_vertex]
                )

                if left_is_adjacent != right_is_adjacent:
                    compatible = False
                    break

            if compatible:
                result.append(right_vertex)

        return result

    def choose_next():
        unmapped = [
            vertex
            for vertex in left_adjacency
            if vertex not in mapping
        ]

        ranked = []

        for vertex in unmapped:
            options = candidates(vertex)
            mapped_neighbor_count = sum(
                1
                for neighbor in left_adjacency[vertex]
                if neighbor in mapping
            )

            ranked.append(
                (
                    len(options),
                    -mapped_neighbor_count,
                    repr(vertex),
                    vertex,
                    options,
                )
            )

        ranked.sort(
            key=lambda row: row[:-2]
        )

        return ranked[0][-2], ranked[0][-1]

    def search():
        if len(mapping) == len(left_adjacency):
            switches = solve_switches_for_mapping(
                left_vertices=left_vertices,
                left_edges=left_edges,
                left_bits=left_bits,
                right_bits=right_bits,
                mapping=mapping,
            )

            if switches is None:
                return None

            return (
                dict(mapping),
                switches,
            )

        left_vertex, options = choose_next()

        for right_vertex in options:
            mapping[left_vertex] = right_vertex
            used_right.add(right_vertex)

            result = search()

            if result is not None:
                return result

            used_right.remove(right_vertex)
            del mapping[left_vertex]

        return None

    return search()


def compare_aligned_to_native_voltage() -> Dict[str, object]:
    certificate = load_native_voltage_certificate()

    if not certificate["audit_pass"]:
        raise ValueError(
            "native voltage derivation certificate did not pass"
        )

    aligned = ingest_aligned_g15_cocycle()

    native_edges = tuple(
        tuple(row["g15_edge"])
        for row in certificate["edge_rows"]
    )

    native_bits = {
        canonical_edge(*row["g15_edge"]): int(
            row["native_bit"]
        )
        for row in certificate["edge_rows"]
    }

    native_vertices = tuple(
        sorted({
            vertex
            for edge in native_edges
            for vertex in edge
        })
    )

    aligned_bits = {
        canonical_edge(*edge): int(bit)
        for edge, bit in aligned.cocycle_bits.items()
    }

    result = find_switching_signed_isomorphism(
        left_vertices=aligned.vertices,
        left_edges=aligned.edges,
        left_bits=aligned_bits,
        right_vertices=native_vertices,
        right_edges=native_edges,
        right_bits=native_bits,
    )

    if result is None:
        mapping = None
        switches = None
    else:
        mapping, switches = result

    switch_count = (
        0
        if switches is None
        else sum(switches.values())
    )

    return {
        "certificate_id": certificate["certificate_id"],
        "certificate_audit_pass": certificate["audit_pass"],
        "native_bit_law": certificate["native_bit_law"],
        "native_g60_state_count": certificate["g60_state_count"],
        "native_g60_edge_count": certificate["g60_edge_count"],
        "native_g15_edge_count": certificate["g15_edge_count"],
        "native_bit_counts": certificate["bit_counts"],
        "aligned_bit_counts": {
            str(bit): count
            for bit, count in sorted(
                aligned.bit_counts.items()
            )
        },
        "switching_signed_isomorphism_exists": (
            result is not None
        ),
        "graph_isomorphism_size": (
            0
            if mapping is None
            else len(mapping)
        ),
        "switch_assignment_size": (
            0
            if switches is None
            else len(switches)
        ),
        "switch_count": switch_count,
        "graph_isomorphism": mapping,
        "switches": switches,
        "aligned_matches_g60_derived_native_switching_class": (
            result is not None
        ),
        "exact_edgewise_identity_claimed": False,
        "historical_writer_identified": False,
    }
