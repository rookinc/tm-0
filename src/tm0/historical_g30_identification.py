"""Identify the historical G30 with the native parity-kernel quotient.

The retained historical artifact records thirty two-state classes from:

    hyperxi_lab graph loading
    followed by the historical antipode quotient G60 -> G30

Those classes use an older G60 labeling.

The retained generator bundle supplies the complete old-to-current
vertex relabeling.

TM-0 independently derives the thirty kernel orbits of:

    chi(x, y) = x xor y

This module transports the historical classes into current labels and
compares the two partitions exactly.

No graph fingerprint or isomorphism is used for the final identity.
"""

import json
from pathlib import Path
from typing import Dict

from .native_g30_intermediate_quotient import (
    derive_native_g30_intermediate_quotient,
)


SOURCE_ROOT = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "historical_g30"
)

HISTORICAL_PATH = (
    SOURCE_ROOT
    / "phase2b_z2_lift_reconstructed_g30_isomorphism.json"
)

BUNDLE_PATH = (
    SOURCE_ROOT
    / "g60_native_generator_input_bundle_001.v1.json"
)


def load_historical_g30_source() -> dict:
    return json.loads(HISTORICAL_PATH.read_text())


def load_historical_g60_label_bundle() -> dict:
    return json.loads(BUNDLE_PATH.read_text())


def canonical_partition(classes):
    return tuple(
        sorted(
            tuple(sorted(int(state) for state in group))
            for group in classes
        )
    )


def identify_historical_g30() -> Dict[str, object]:
    historical = load_historical_g30_source()
    bundle = load_historical_g60_label_bundle()
    derived = derive_native_g30_intermediate_quotient()

    old_to_current = {
        int(old): int(current)
        for old, current
        in bundle["old_to_current_vertex_map"].items()
    }

    historical_classes_old = canonical_partition(
        historical["reconstructed_g30_classes_from_g60"]
    )

    historical_classes_current = canonical_partition(
        tuple(
            tuple(
                old_to_current[state]
                for state in group
            )
            for group in historical_classes_old
        )
    )

    derived_kernel_classes = canonical_partition(
        derived["kernel_classes"]
    )

    historical_set = set(historical_classes_current)
    derived_set = set(derived_kernel_classes)

    historical_only = tuple(
        sorted(historical_set - derived_set)
    )

    derived_only = tuple(
        sorted(derived_set - historical_set)
    )

    exact_partition_match = (
        historical_classes_current
        == derived_kernel_classes
    )

    return {
        "historical_source_status": historical["status"],
        "historical_source_isomorphic": historical["isomorphic"],
        "historical_reconstruction": (
            historical["historical_reconstruction"]
        ),
        "historical_boundary": historical["boundary"],
        "old_to_current_map_count": len(old_to_current),
        "historical_class_count": len(
            historical_classes_current
        ),
        "derived_kernel_class_count": len(
            derived_kernel_classes
        ),
        "historical_class_size_profile": tuple(
            sorted({
                len(group)
                for group in historical_classes_current
            })
        ),
        "derived_class_size_profile": tuple(
            sorted({
                len(group)
                for group in derived_kernel_classes
            })
        ),
        "exact_partition_match": exact_partition_match,
        "historical_only_count": len(historical_only),
        "derived_only_count": len(derived_only),
        "historical_only": historical_only,
        "derived_only": derived_only,
        "historical_classes_current": (
            historical_classes_current
        ),
        "derived_kernel_classes": derived_kernel_classes,
        "historical_g30_is_native_parity_kernel_quotient": (
            exact_partition_match
        ),
        "intrinsic_identification": (
            "historical antipode quotient equals "
            "G60 / ker(chi), chi(x,y)=x xor y"
        ),
    }
