"""Authenticate the retained aligned G15 cocycle mathematically.

Authentication combines:

    retained source hashes
    independent G60-derived native voltage
    explicit graph relabeling
    explicit local switching gauge
    complete edgewise verification
    unique native cover-class membership
    one-bit tamper detection

This authenticates mathematical content.

It does not identify the historical writer.
"""

import hashlib
from typing import Dict

from .aligned_g15_cocycle import (
    SOURCE_PATH as ALIGNED_SOURCE_PATH,
    ingest_aligned_g15_cocycle,
)
from .native_g15_voltage_comparison import (
    CERTIFICATE_PATH as NATIVE_CERTIFICATE_PATH,
    canonical_edge,
    compare_aligned_to_native_voltage,
    load_native_voltage_certificate,
)
from .project42_invariant_cover_square import (
    classify_aligned_lift_in_cover_square,
)


def sha256_file(path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(65536),
            b"",
        ):
            digest.update(chunk)

    return digest.hexdigest()


def authenticate_native_g15_cocycle() -> Dict[str, object]:
    aligned = ingest_aligned_g15_cocycle()
    native_certificate = load_native_voltage_certificate()
    comparison = compare_aligned_to_native_voltage()
    cover_class = classify_aligned_lift_in_cover_square()

    mapping = comparison["graph_isomorphism"]
    switches = comparison["switches"]

    if mapping is None or switches is None:
        raise ValueError(
            "native switching-class witness is unavailable"
        )

    native_bits = {
        canonical_edge(*row["g15_edge"]): int(
            row["native_bit"]
        )
        for row in native_certificate["edge_rows"]
    }

    verification_rows = []

    for edge in aligned.edges:
        left, right = edge
        aligned_bit = int(aligned.cocycle_bits[edge])

        transported_edge = canonical_edge(
            mapping[left],
            mapping[right],
        )

        transported_bit = (
            aligned_bit
            ^ switches[left]
            ^ switches[right]
        )

        native_bit = native_bits[transported_edge]
        matches = transported_bit == native_bit

        verification_rows.append(
            {
                "aligned_edge": edge,
                "aligned_bit": aligned_bit,
                "left_switch": switches[left],
                "right_switch": switches[right],
                "transported_edge": transported_edge,
                "transported_bit": transported_bit,
                "native_bit": native_bit,
                "matches": matches,
            }
        )

    matching_edge_count = sum(
        1
        for row in verification_rows
        if row["matches"]
    )

    mismatching_edge_count = (
        len(verification_rows)
        - matching_edge_count
    )

    tampered_rows = [
        dict(row)
        for row in verification_rows
    ]

    tampered_rows[0]["aligned_bit"] ^= 1
    tampered_rows[0]["transported_bit"] ^= 1
    tampered_rows[0]["matches"] = (
        tampered_rows[0]["transported_bit"]
        == tampered_rows[0]["native_bit"]
    )

    tamper_mismatch_count = sum(
        1
        for row in tampered_rows
        if not row["matches"]
    )

    authentication_pass = all(
        (
            native_certificate["audit_pass"],
            comparison[
                "aligned_matches_g60_derived_native_switching_class"
            ],
            cover_class["aligned_lift_is_native_class"],
            len(verification_rows) == 30,
            matching_edge_count == 30,
            mismatching_edge_count == 0,
            tamper_mismatch_count >= 1,
        )
    )

    return {
        "authentication_id": (
            "native_g15_cocycle_authentication_001"
        ),
        "authentication_pass": authentication_pass,
        "claim": (
            "retained aligned artifact is an authenticated "
            "representative of the native G60-derived G15 "
            "switching class"
        ),
        "aligned_source_path": str(ALIGNED_SOURCE_PATH),
        "aligned_source_status": aligned.source_status,
        "aligned_source_sha256": sha256_file(
            ALIGNED_SOURCE_PATH
        ),
        "native_certificate_path": str(
            NATIVE_CERTIFICATE_PATH
        ),
        "native_certificate_id": (
            native_certificate["certificate_id"]
        ),
        "native_certificate_sha256": sha256_file(
            NATIVE_CERTIFICATE_PATH
        ),
        "native_bit_law": native_certificate[
            "native_bit_law"
        ],
        "graph_relabeling": mapping,
        "switch_assignment": switches,
        "switch_count": sum(switches.values()),
        "tested_edge_count": len(verification_rows),
        "matching_edge_count": matching_edge_count,
        "mismatching_edge_count": mismatching_edge_count,
        "verification_rows": tuple(verification_rows),
        "native_cover_class_match": (
            cover_class["aligned_lift_is_native_class"]
        ),
        "native_cover_matching_classes": (
            cover_class["matching_classes"]
        ),
        "tamper_test": {
            "tampered_edge": tampered_rows[0][
                "aligned_edge"
            ],
            "tamper_mismatch_count": (
                tamper_mismatch_count
            ),
            "tamper_detected": (
                tamper_mismatch_count >= 1
            ),
        },
        "historical_writer_identified": False,
        "historical_generation_reconstructed": False,
        "boundary": (
            "Mathematical content is authenticated against an "
            "independent native G60 derivation. Historical writer "
            "identity and exact original generation path remain open."
        ),
    }
