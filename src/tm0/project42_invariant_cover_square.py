"""Classify the aligned G15 lift inside the Project 42 cover square.

The retained certificate contains four G15 double-cover classes:

    zero
    native
    alternative
    all_one

TM-0 independently constructs the aligned G15 signed lift, then compares
it by exact graph isomorphism against every certified class.

This establishes cover-class membership only.

It does not establish strict native cocycle provenance.
"""

import json
from pathlib import Path
from typing import Dict

from .aligned_g15_cocycle import ingest_aligned_g15_cocycle
from .finite_graph_isomorphism import find_graph_isomorphism
from .signed_double_cover import construct_signed_double_cover


CERTIFICATE_PATH = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "project42"
    / "project42_invariant_cover_square_certificate_032.json"
)


def load_cover_square_certificate() -> dict:
    return json.loads(
        CERTIFICATE_PATH.read_text()
    )


def classify_aligned_lift_in_cover_square() -> Dict[str, object]:
    certificate = load_cover_square_certificate()

    if not certificate["audit_pass"]:
        raise ValueError(
            "Project 42 cover-square certificate did not pass"
        )

    cocycle = ingest_aligned_g15_cocycle()

    aligned_cover = construct_signed_double_cover(
        base_vertices=cocycle.vertices,
        base_edges=cocycle.edges,
        signs=cocycle.signs,
    )

    class_results = []

    for row in certificate["classes"]:
        class_vertices = tuple(range(row["cover_vertex_count"]))
        class_edges = tuple(
            tuple(edge)
            for edge in row["cover_edges"]
        )

        mapping = find_graph_isomorphism(
            left_vertices=aligned_cover.lift_vertices,
            left_edges=aligned_cover.lift_edges,
            right_vertices=class_vertices,
            right_edges=class_edges,
        )

        class_results.append(
            {
                "class_id": row["class_id"],
                "triangle_count": row["triangle_count"],
                "component_sizes": tuple(
                    row["component_sizes"]
                ),
                "isomorphic": mapping is not None,
                "mapping_size": (
                    0
                    if mapping is None
                    else len(mapping)
                ),
                "mapping": mapping,
            }
        )

    matching_classes = tuple(
        row["class_id"]
        for row in class_results
        if row["isomorphic"]
    )

    return {
        "certificate_id": certificate["certificate_id"],
        "certificate_audit_pass": certificate["audit_pass"],
        "source_status": cocycle.source_status,
        "provenance_classification": (
            cocycle.provenance_classification
        ),
        "aligned_lift_vertex_count": len(
            aligned_cover.lift_vertices
        ),
        "aligned_lift_edge_count": len(
            aligned_cover.lift_edges
        ),
        "class_results": tuple(class_results),
        "matching_classes": matching_classes,
        "unique_matching_class": (
            matching_classes[0]
            if len(matching_classes) == 1
            else None
        ),
        "aligned_lift_is_native_class": (
            matching_classes == ("native",)
        ),
        "native_origin_proved": False,
    }
