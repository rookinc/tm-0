"""Ingest the retained aligned G15 Z2 cocycle candidate.

The retained source is an imported, support-aligned representative.
This module validates and converts it into TM-0 local signs.

It does not claim native derivation from G60.
"""

import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import Tuple

from .local_sign_product import LocalSign


Vertex = str
Edge = Tuple[Vertex, Vertex]


SOURCE_PATH = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "g15"
    / "transport_cocycle_edges.json"
)


@dataclass(frozen=True)
class AlignedG15Cocycle:
    source_name: str
    source_status: str
    base_graph: str
    source_graph: str
    source_artifact: str
    provenance_classification: str
    vertices: Tuple[Vertex, ...]
    edges: Tuple[Edge, ...]
    signs: Dict[Edge, LocalSign]
    cocycle_bits: Dict[Edge, int]
    directed_record_count: int
    directed_records_per_edge: Dict[Edge, int]
    bit_counts: Dict[int, int]
    sign_counts: Dict[int, int]


def canonical_edge(
    left: Vertex,
    right: Vertex,
) -> Edge:
    if left == right:
        raise ValueError(
            "aligned G15 cocycle does not admit loops"
        )

    return (
        (left, right)
        if left < right
        else (right, left)
    )


def load_source() -> dict:
    return json.loads(SOURCE_PATH.read_text())


def bit_to_local_sign(bit: int) -> LocalSign:
    if bit == 0:
        return LocalSign.PRESERVE

    if bit == 1:
        return LocalSign.INVERT

    raise ValueError(
        "cocycle bit must be 0 or 1"
    )


def ingest_aligned_g15_cocycle() -> AlignedG15Cocycle:
    source = load_source()

    if source.get("base_graph") != "G15":
        raise ValueError(
            "aligned cocycle source base graph must be G15"
        )

    if source.get("source_graph") != "G15":
        raise ValueError(
            "aligned cocycle source graph must be G15"
        )

    records = source.get("edge_records")

    if not isinstance(records, list) or not records:
        raise ValueError(
            "aligned cocycle source requires edge records"
        )

    grouped = {}

    for record in records:
        left = str(record["u"])
        right = str(record["v"])
        edge = canonical_edge(left, right)

        bit = int(record["cocycle_bit"])
        epsilon = int(record["epsilon"])
        sign = bit_to_local_sign(bit)

        if epsilon != int(sign):
            raise ValueError(
                "cocycle bit and epsilon disagree"
            )

        if tuple(
            sorted(
                str(vertex)
                for vertex in record["source_edge"]
            )
        ) != edge:
            raise ValueError(
                "directed record source edge disagrees with endpoints"
            )

        grouped.setdefault(edge, []).append(
            (
                left,
                right,
                bit,
                epsilon,
            )
        )

    edges = tuple(sorted(grouped))
    signs = {}
    cocycle_bits = {}
    directed_records_per_edge = {}

    for edge in edges:
        edge_records = grouped[edge]
        directed_records_per_edge[edge] = len(edge_records)

        if len(edge_records) != 2:
            raise ValueError(
                "each undirected edge requires two directed records"
            )

        orientations = {
            (left, right)
            for left, right, _, _ in edge_records
        }

        expected_orientations = {
            edge,
            (edge[1], edge[0]),
        }

        if orientations != expected_orientations:
            raise ValueError(
                "opposite directed records are required"
            )

        bits = {
            bit
            for _, _, bit, _ in edge_records
        }

        epsilons = {
            epsilon
            for _, _, _, epsilon in edge_records
        }

        if len(bits) != 1 or len(epsilons) != 1:
            raise ValueError(
                "opposite directed records must agree"
            )

        bit = next(iter(bits))
        epsilon = next(iter(epsilons))
        sign = bit_to_local_sign(bit)

        if epsilon != int(sign):
            raise ValueError(
                "paired cocycle bit and epsilon disagree"
            )

        cocycle_bits[edge] = bit
        signs[edge] = sign

    vertices = tuple(
        sorted({
            vertex
            for edge in edges
            for vertex in edge
        })
    )

    bit_counts = dict(
        sorted(
            Counter(cocycle_bits.values()).items()
        )
    )

    sign_counts = dict(
        sorted(
            Counter(
                int(sign)
                for sign in signs.values()
            ).items()
        )
    )

    return AlignedG15Cocycle(
        source_name=source["name"],
        source_status=source["status"],
        base_graph=source["base_graph"],
        source_graph=source["source_graph"],
        source_artifact=source["source_artifact"],
        provenance_classification=(
            "aligned_imported_representative_native_origin_open"
        ),
        vertices=vertices,
        edges=edges,
        signs=signs,
        cocycle_bits=cocycle_bits,
        directed_record_count=len(records),
        directed_records_per_edge=directed_records_per_edge,
        bit_counts=bit_counts,
        sign_counts=sign_counts,
    )
