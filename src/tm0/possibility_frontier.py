"""Possibility frontier for TM-0.

The current signed graph supplies an address space of possible local
realizations.

Each relation address may be flipped.

A possible realization records:

    the addressed relation
    the current character
    the resulting character

Possibility is the address space of these candidate realizations.
Nothing in this module selects or executes one.
"""

from dataclasses import dataclass
from typing import Dict
from typing import Tuple

from .character_update import CharacterSignature
from .character_update import realize_edge_flip
from .graph_switching_classification import graph_switching_signature
from .graph_switching_normal_form import Edge
from .graph_switching_normal_form import Vertex
from .graph_switching_normal_form import canonical_edge
from .local_sign_product import LocalSign


@dataclass(frozen=True)
class PossibleRealization:
    address: Edge
    before: CharacterSignature
    after: CharacterSignature


def possibility_frontier(
    edges: Tuple[Edge, ...],
    signs: Dict[Edge, LocalSign],
    root: Vertex,
) -> Tuple[PossibleRealization, ...]:
    before = graph_switching_signature(edges, signs, root)
    possibilities = []

    for edge in edges:
        address = canonical_edge(*edge)

        update = realize_edge_flip(
            edges,
            signs,
            root,
            address,
        )

        possibilities.append(
            PossibleRealization(
                address=address,
                before=before,
                after=update.after,
            )
        )

    return tuple(possibilities)


def outcome_classes(
    possibilities: Tuple[PossibleRealization, ...],
) -> Dict[CharacterSignature, Tuple[Edge, ...]]:
    classes = {}

    for possibility in possibilities:
        classes.setdefault(possibility.after, [])
        classes[possibility.after].append(possibility.address)

    return {
        signature: tuple(addresses)
        for signature, addresses in classes.items()
    }
