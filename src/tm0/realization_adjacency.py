"""Adjacency induced by reachable local realizations.

Character adjacency uses one-bit difference.

Realization adjacency uses one actual local edge-sign flip.

The two notions need not agree when one edge participates in several
independent cycles.
"""

from typing import Dict
from typing import Tuple

from .character_update import CharacterSignature
from .character_update import realize_edge_flip
from .graph_switching_classification import graph_switching_signature
from .graph_switching_normal_form import Edge
from .graph_switching_normal_form import Vertex
from .graph_switching_normal_form import canonical_edge
from .local_sign_product import LocalSign
from .transform_adjacency import minimally_transformable


def reachable_character_states(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
) -> Dict[Edge, CharacterSignature]:
    reachable = {}

    for edge in edges:
        address = canonical_edge(*edge)
        update = realize_edge_flip(
            edges,
            signs,
            root,
            address,
        )
        reachable[address] = update.after

    return reachable


def realization_adjacent(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
    target: CharacterSignature,
) -> bool:
    reachable = reachable_character_states(
        edges,
        signs,
        root,
    )

    return target in reachable.values()


def compare_adjacency_notions(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
    target: CharacterSignature,
) -> Tuple[bool, bool]:
    current = graph_switching_signature(
        edges,
        signs,
        root,
    )

    return (
        minimally_transformable(current, target),
        realization_adjacent(
            edges,
            signs,
            root,
            target,
        ),
    )
