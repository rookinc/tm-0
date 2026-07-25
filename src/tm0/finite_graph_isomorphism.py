"""Exact isomorphism for small finite simple graphs.

The search is dependency-free and uses:

    vertex-count agreement
    edge-count agreement
    degree partition refinement
    adjacency-consistent backtracking

It returns an explicit vertex bijection when one exists.
"""

from typing import Dict
from typing import Hashable
from typing import Iterable
from typing import Optional
from typing import Tuple


Vertex = Hashable
Edge = Tuple[Vertex, Vertex]


def adjacency_map(
    vertices: Iterable[Vertex],
    edges: Iterable[Edge],
) -> Dict[Vertex, frozenset]:
    vertex_set = frozenset(vertices)

    if not vertex_set:
        raise ValueError("graph must not be empty")

    adjacency = {
        vertex: set()
        for vertex in vertex_set
    }

    seen_edges = set()

    for left, right in edges:
        if left == right:
            raise ValueError("simple graph must not contain loops")

        if left not in vertex_set or right not in vertex_set:
            raise ValueError("edge uses an unregistered vertex")

        edge_key = frozenset((left, right))

        if edge_key in seen_edges:
            continue

        seen_edges.add(edge_key)
        adjacency[left].add(right)
        adjacency[right].add(left)

    return {
        vertex: frozenset(neighbors)
        for vertex, neighbors in adjacency.items()
    }


def find_graph_isomorphism(
    left_vertices: Iterable[Vertex],
    left_edges: Iterable[Edge],
    right_vertices: Iterable[Vertex],
    right_edges: Iterable[Edge],
) -> Optional[Dict[Vertex, Vertex]]:
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

    left_edge_count = sum(
        len(neighbors)
        for neighbors in left_adjacency.values()
    ) // 2

    right_edge_count = sum(
        len(neighbors)
        for neighbors in right_adjacency.values()
    ) // 2

    if left_edge_count != right_edge_count:
        return None

    left_degree_profile = sorted(
        len(neighbors)
        for neighbors in left_adjacency.values()
    )

    right_degree_profile = sorted(
        len(neighbors)
        for neighbors in right_adjacency.values()
    )

    if left_degree_profile != right_degree_profile:
        return None

    right_by_degree = {}

    for vertex, neighbors in right_adjacency.items():
        right_by_degree.setdefault(
            len(neighbors),
            [],
        ).append(vertex)

    mapping = {}
    used_right = set()

    def candidate_vertices(left_vertex):
        degree = len(left_adjacency[left_vertex])

        candidates = []

        for right_vertex in right_by_degree[degree]:
            if right_vertex in used_right:
                continue

            compatible = True

            for mapped_left, mapped_right in mapping.items():
                left_adjacent = (
                    mapped_left
                    in left_adjacency[left_vertex]
                )
                right_adjacent = (
                    mapped_right
                    in right_adjacency[right_vertex]
                )

                if left_adjacent != right_adjacent:
                    compatible = False
                    break

            if compatible:
                candidates.append(right_vertex)

        return candidates

    def choose_next_left():
        unmapped = [
            vertex
            for vertex in left_adjacency
            if vertex not in mapping
        ]

        ranked = []

        for vertex in unmapped:
            candidates = candidate_vertices(vertex)
            mapped_neighbor_count = sum(
                1
                for neighbor in left_adjacency[vertex]
                if neighbor in mapping
            )

            ranked.append(
                (
                    len(candidates),
                    -mapped_neighbor_count,
                    -len(left_adjacency[vertex]),
                    repr(vertex),
                    vertex,
                    candidates,
                )
            )

        ranked.sort(
            key=lambda row: row[:-2]
        )

        return ranked[0][-2], ranked[0][-1]

    def search():
        if len(mapping) == len(left_adjacency):
            return dict(mapping)

        left_vertex, candidates = choose_next_left()

        for right_vertex in candidates:
            mapping[left_vertex] = right_vertex
            used_right.add(right_vertex)

            result = search()

            if result is not None:
                return result

            used_right.remove(right_vertex)
            del mapping[left_vertex]

        return None

    return search()


def graphs_are_isomorphic(
    left_vertices: Iterable[Vertex],
    left_edges: Iterable[Edge],
    right_vertices: Iterable[Vertex],
    right_edges: Iterable[Edge],
) -> bool:
    return find_graph_isomorphism(
        left_vertices,
        left_edges,
        right_vertices,
        right_edges,
    ) is not None
