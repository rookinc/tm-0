"""Enumerate automorphisms of a small finite simple graph.

The search uses:

    degree compatibility
    adjacency compatibility with the partial mapping
    deterministic backtracking order

No expected group order is used as an input.
"""

from typing import Hashable
from typing import Iterable
from typing import Tuple

from .finite_graph_isomorphism import adjacency_map


Vertex = Hashable
Edge = Tuple[Vertex, Vertex]
Permutation = Tuple[int, ...]


def enumerate_graph_automorphisms(
    vertices: Iterable[Vertex],
    edges: Iterable[Edge],
) -> Tuple[Permutation, ...]:
    ordered_vertices = tuple(vertices)

    if len(ordered_vertices) != len(set(ordered_vertices)):
        raise ValueError(
            "graph vertices must be distinct"
        )

    adjacency = adjacency_map(
        ordered_vertices,
        edges,
    )

    index_of = {
        vertex: index
        for index, vertex in enumerate(ordered_vertices)
    }

    search_order = tuple(
        sorted(
            ordered_vertices,
            key=lambda vertex: (
                -len(adjacency[vertex]),
                repr(vertex),
            ),
        )
    )

    mapping = {}
    used_targets = set()
    results = []

    def descend(depth):
        if depth == len(search_order):
            permutation = tuple(
                index_of[mapping[vertex]]
                for vertex in ordered_vertices
            )

            results.append(permutation)
            return

        source = search_order[depth]
        source_degree = len(adjacency[source])

        for target in ordered_vertices:
            if target in used_targets:
                continue

            if len(adjacency[target]) != source_degree:
                continue

            compatible = True

            for mapped_source, mapped_target in mapping.items():
                source_adjacent = (
                    mapped_source in adjacency[source]
                )
                target_adjacent = (
                    mapped_target in adjacency[target]
                )

                if source_adjacent != target_adjacent:
                    compatible = False
                    break

            if not compatible:
                continue

            mapping[source] = target
            used_targets.add(target)

            descend(depth + 1)

            used_targets.remove(target)
            del mapping[source]

    descend(0)

    return tuple(sorted(set(results)))


def permutation_orbit(
    point: int,
    permutations: Iterable[Permutation],
) -> Tuple[int, ...]:
    return tuple(
        sorted({
            permutation[point]
            for permutation in permutations
        })
    )


def point_stabilizer(
    point: int,
    permutations: Iterable[Permutation],
) -> Tuple[Permutation, ...]:
    return tuple(
        permutation
        for permutation in permutations
        if permutation[point] == point
    )
