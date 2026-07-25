"""Certify the Project 42 quotient graphs as L(Petersen).

The quotient graphs are derived from the carrier and selected
equivalence systems.

The Petersen line graph is constructed independently.

The finite graph isomorphism search produces explicit bijections.
No Project 42 quotient edge set is used to construct L(Petersen).
"""

from typing import Dict
from typing import Tuple

from .finite_graph_isomorphism import (
    find_graph_isomorphism,
)
from .petersen_line_graph import (
    petersen_line_graph_edges,
    petersen_line_graph_vertices,
)
from .project42_quotient_graphs import (
    construct_project42_quotient_graphs,
)


def certify_project42_quotients_as_petersen_line_graphs() -> Dict[
    str,
    object,
]:
    quotients = construct_project42_quotient_graphs()

    target_vertices = petersen_line_graph_vertices()
    target_edges = petersen_line_graph_edges()

    mappings = tuple(
        find_graph_isomorphism(
            left_vertices=quotient.quotient_vertices,
            left_edges=quotient.quotient_edges,
            right_vertices=target_vertices,
            right_edges=target_edges,
        )
        for quotient in quotients
    )

    mapping_exists = tuple(
        mapping is not None
        for mapping in mappings
    )

    mapping_sizes = tuple(
        0 if mapping is None else len(mapping)
        for mapping in mappings
    )

    pairwise_mappings = []

    for left_index in range(len(quotients)):
        for right_index in range(
            left_index + 1,
            len(quotients),
        ):
            left = quotients[left_index]
            right = quotients[right_index]

            mapping = find_graph_isomorphism(
                left_vertices=left.quotient_vertices,
                left_edges=left.quotient_edges,
                right_vertices=right.quotient_vertices,
                right_edges=right.quotient_edges,
            )

            pairwise_mappings.append(
                (
                    left_index,
                    right_index,
                    mapping,
                )
            )

    pairwise_mapping_exists = tuple(
        mapping is not None
        for _, _, mapping in pairwise_mappings
    )

    return {
        "quotient_count": len(quotients),
        "target_vertex_count": len(target_vertices),
        "target_edge_count": len(target_edges),
        "mapping_exists": mapping_exists,
        "mapping_sizes": mapping_sizes,
        "all_quotients_are_LP": all(mapping_exists),
        "pairwise_mapping_exists": pairwise_mapping_exists,
        "all_quotients_pairwise_isomorphic": all(
            pairwise_mapping_exists
        ),
        "mappings": mappings,
        "pairwise_mappings": tuple(pairwise_mappings),
    }
