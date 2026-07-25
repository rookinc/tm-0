"""Construct the Petersen graph and its line graph.

The Petersen graph is defined independently using:

    outer cycle: 0-1-2-3-4-0
    inner star: 5-7-9-6-8-5
    spokes: 0-5, 1-6, 2-7, 3-8, 4-9

Its line graph has:

    one vertex for each Petersen edge
    one edge when two Petersen edges share an endpoint
"""

from itertools import combinations
from typing import Tuple


PetersenVertex = int
PetersenEdge = Tuple[PetersenVertex, PetersenVertex]
LineVertex = PetersenEdge
LineEdge = Tuple[LineVertex, LineVertex]


def canonical_edge(
    left,
    right,
):
    if left == right:
        raise ValueError(
            "graph edge endpoints must be distinct"
        )

    return (
        (left, right)
        if left < right
        else (right, left)
    )


def petersen_vertices() -> Tuple[PetersenVertex, ...]:
    return tuple(range(10))


def petersen_edges() -> Tuple[PetersenEdge, ...]:
    outer = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 0),
    )

    inner = (
        (5, 7),
        (7, 9),
        (9, 6),
        (6, 8),
        (8, 5),
    )

    spokes = (
        (0, 5),
        (1, 6),
        (2, 7),
        (3, 8),
        (4, 9),
    )

    return tuple(
        sorted(
            canonical_edge(left, right)
            for left, right in (
                outer
                + inner
                + spokes
            )
        )
    )


def petersen_line_graph_vertices() -> Tuple[
    LineVertex,
    ...,
]:
    return petersen_edges()


def petersen_line_graph_edges() -> Tuple[
    LineEdge,
    ...,
]:
    vertices = petersen_line_graph_vertices()

    edges = []

    for left, right in combinations(vertices, 2):
        if set(left).intersection(right):
            edges.append(
                canonical_edge(left, right)
            )

    return tuple(sorted(edges))
