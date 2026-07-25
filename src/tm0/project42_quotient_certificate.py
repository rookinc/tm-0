"""Certify the three derived Project 42 quotient graphs.

Construction and certification are kept separate:

    project42_quotient_graphs
        derives quotient graphs from carrier edges and partitions

    project42_quotient_certificate
        compares those derived graphs against the retained
        Project 42 quotient-frame certificate

The retained quotient edge sets are certification targets only.
They are not used as construction inputs.
"""

import json
from pathlib import Path
from typing import Dict
from typing import Tuple

from .project42_quotient_graphs import (
    construct_project42_quotient_graphs,
)


CERTIFICATE_PATH = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "project42"
    / "project42_quotient_frame_orbit_certificate_004.json"
)


def load_quotient_certificate() -> dict:
    return json.loads(
        CERTIFICATE_PATH.read_text()
    )


def canonical_edge(
    left: int,
    right: int,
) -> Tuple[int, int]:
    if left == right:
        raise ValueError(
            "certificate quotient edge must not be a loop"
        )

    return (
        (left, right)
        if left < right
        else (right, left)
    )


def expected_quotient_edges() -> Tuple[
    Tuple[Tuple[int, int], ...],
    ...,
]:
    certificate = load_quotient_certificate()

    expected = []

    for row in certificate["partitions"]:
        source_blocks = tuple(
            tuple(sorted(str(vertex) for vertex in block))
            for block in row["blocks"]
        )

        canonical_blocks = tuple(sorted(source_blocks))

        canonical_index = {
            block: index
            for index, block in enumerate(canonical_blocks)
        }

        source_to_canonical = {
            source_index: canonical_index[block]
            for source_index, block in enumerate(source_blocks)
        }

        relabeled_edges = tuple(
            sorted(
                canonical_edge(
                    source_to_canonical[left],
                    source_to_canonical[right],
                )
                for left, right in row["quotient_edges"]
            )
        )

        expected.append(relabeled_edges)

    return tuple(expected)


def certify_project42_quotient_graphs() -> Dict[str, object]:
    certificate = load_quotient_certificate()
    quotients = construct_project42_quotient_graphs()
    expected_edges = expected_quotient_edges()

    derived_edges = tuple(
        quotient.quotient_edges
        for quotient in quotients
    )

    edge_matches = tuple(
        derived == expected
        for derived, expected in zip(
            derived_edges,
            expected_edges,
        )
    )

    vertex_counts = tuple(
        len(quotient.quotient_vertices)
        for quotient in quotients
    )

    edge_counts = tuple(
        len(quotient.quotient_edges)
        for quotient in quotients
    )

    multiplicity_profiles = tuple(
        tuple(
            sorted(
                quotient.covering_multiplicities().values()
            )
        )
        for quotient in quotients
    )

    return {
        "certificate_id": certificate["certificate_id"],
        "source_audit_pass": certificate["audit_pass"],
        "quotient_count": len(quotients),
        "vertex_counts": vertex_counts,
        "edge_counts": edge_counts,
        "edge_matches": edge_matches,
        "all_edge_sets_match": all(edge_matches),
        "multiplicity_profiles": multiplicity_profiles,
        "all_multiplicities_are_two": all(
            all(value == 2 for value in profile)
            for profile in multiplicity_profiles
        ),
    }
