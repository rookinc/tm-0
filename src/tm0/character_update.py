"""Cycle-space character updates for TM-0.

A local realization flips the sign of one relation while preserving
the graph incidence structure.

The cycle-space signature is measured before and after the flip.

A flipped chord changes one fundamental-cycle bit.

A flipped tree edge may change several fundamental-cycle bits because
it participates in several fundamental cycles.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Tuple

from .graph_switching_classification import graph_switching_signature
from .graph_switching_normal_form import Edge
from .graph_switching_normal_form import Vertex
from .graph_switching_normal_form import canonical_edge
from .local_sign_product import LocalSign


CharacterSignature = Tuple[Tuple[Edge, LocalSign], ...]


@dataclass(frozen=True)
class CharacterUpdate:
    flipped_edge: Edge
    before: CharacterSignature
    after: CharacterSignature
    changed_bits: Tuple[Edge, ...]


def flip_sign(sign: LocalSign) -> LocalSign:
    return LocalSign(-int(sign))


def realize_edge_flip(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
    edge: Edge,
) -> CharacterUpdate:
    selected = canonical_edge(*edge)

    if selected not in signs:
        raise ValueError("flipped edge must belong to the signed graph")

    before = graph_switching_signature(edges, signs, root)

    updated = dict(signs)
    updated[selected] = flip_sign(updated[selected])

    after = graph_switching_signature(edges, updated, root)

    before_map = dict(before)
    after_map = dict(after)

    changed_bits = tuple(
        chord
        for chord in before_map
        if before_map[chord] != after_map[chord]
    )

    return CharacterUpdate(
        flipped_edge=selected,
        before=before,
        after=after,
        changed_bits=changed_bits,
    )
