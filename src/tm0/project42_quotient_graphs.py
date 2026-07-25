"""Derive the three Project 42 quotient graphs.

The retained full-action certificate supplies:

    the thirty-vertex carrier graph
    the natural three-partition orbit

This module constructs each quotient graph using the generic,
dependency-free quotient constructor.

The quotient graphs are derived from carrier edges and partitions.
Their edge sets are not supplied as construction inputs.
"""

from typing import Tuple

from .project42_full_action_certificate import (
    load_certificate,
)
from .quotient_graph import (
    QuotientGraph,
    construct_quotient_graph,
)


def project42_carrier_vertices() -> Tuple[str, ...]:
    certificate = load_certificate()
    vertex_count = certificate["carrier"]["vertex_count"]

    return tuple(
        str(index)
        for index in range(vertex_count)
    )


def project42_carrier_edges() -> Tuple[
    Tuple[str, str],
    ...,
]:
    certificate = load_certificate()

    return tuple(
        (
            str(left),
            str(right),
        )
        for left, right in certificate["carrier"]["edges"]
    )


def project42_partitions() -> Tuple[
    Tuple[Tuple[str, ...], ...],
    ...,
]:
    certificate = load_certificate()

    return tuple(
        tuple(
            tuple(
                str(vertex)
                for vertex in block
            )
            for block in partition
        )
        for partition in certificate["partition_orbit"]
    )


def construct_project42_quotient_graphs() -> Tuple[
    QuotientGraph,
    ...,
]:
    carrier_vertices = project42_carrier_vertices()
    carrier_edges = project42_carrier_edges()

    return tuple(
        construct_quotient_graph(
            carrier_vertices=carrier_vertices,
            carrier_edges=carrier_edges,
            classes=partition,
        )
        for partition in project42_partitions()
    )
