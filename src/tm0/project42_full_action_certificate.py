"""Load the retained Project 42 full carrier-action certificate.

The certificate contains:

    one 30-vertex carrier
    one natural three-partition orbit
    720 carrier automorphisms
    the induced family permutation for every automorphism

This module derives:

    the finite carrier-action group
    the partition-action kernel
    selected-system stabilizers

The certified target counts are not used as construction inputs.
"""

from json import loads
from pathlib import Path
from typing import Tuple

from .finite_carrier_action_group import (
    CarrierFamilyAction,
    FiniteCarrierActionGroup,
    finite_carrier_action_group,
)


CERTIFICATE_PATH = (
    Path(__file__).resolve().parents[2]
    / "sources"
    / "project42"
    / "project42_full_carrier_action_certificate_031.json"
)


def load_certificate() -> dict:
    """Load the retained Project 42 certificate."""
    return loads(
        CERTIFICATE_PATH.read_text(
            encoding="utf-8"
        )
    )


def load_project42_action_group() -> FiniteCarrierActionGroup:
    """Construct the full action group from certificate rows."""
    certificate = load_certificate()

    actions = tuple(
        CarrierFamilyAction(
            name=f"aut_{row['index']:03d}",
            carrier_permutation=tuple(
                row["carrier_permutation"]
            ),
            family_permutation=tuple(
                row["family_permutation"]
            ),
        )
        for row in certificate["automorphisms"]
    )

    return finite_carrier_action_group(
        actions
    )


def partition_action_kernel(
    group: FiniteCarrierActionGroup,
) -> Tuple[CarrierFamilyAction, ...]:
    """Derive actions acting trivially on the partition family."""
    identity = tuple(
        range(group.family_size)
    )

    return tuple(
        action
        for action in group.actions
        if action.family_permutation == identity
    )


def selected_system_stabilizers(
    group: FiniteCarrierActionGroup,
) -> Tuple[
    Tuple[CarrierFamilyAction, ...],
    ...,
]:
    """Derive the stabilizer of every registered family member."""
    return tuple(
        group.stabilizer(system_index)
        for system_index in range(
            group.family_size
        )
    )


def partition_action_image(
    group: FiniteCarrierActionGroup,
) -> Tuple[Tuple[int, ...], ...]:
    """Derive the distinct induced family permutations."""
    return tuple(
        sorted({
            action.family_permutation
            for action in group.actions
        })
    )
