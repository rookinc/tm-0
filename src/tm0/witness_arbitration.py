"""Minimal witness arbitration for TM-0.

Witnesses report one of two non-null registrations:

SAME
POLAR

Equal reports produce consensus.

Two conflicting reports remain unresolved because neither witness has
earned priority.

Three reports may resolve by strict majority.

This is a bounded arbitration model, not a universal witness theorem.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from typing import Tuple


class WitnessReport(str, Enum):
    SAME = "SAME"
    POLAR = "POLAR"


@dataclass(frozen=True)
class WitnessDecision:
    reports: Tuple[WitnessReport, ...]
    resolved: Optional[WitnessReport]

    @property
    def is_resolved(self) -> bool:
        return self.resolved is not None


def unanimous_decision(
    reports: Tuple[WitnessReport, ...],
) -> WitnessDecision:
    if not reports:
        raise ValueError("at least one witness report is required")

    first = reports[0]

    resolved = (
        first
        if all(report is first for report in reports)
        else None
    )

    return WitnessDecision(
        reports=reports,
        resolved=resolved,
    )


def strict_majority_decision(
    reports: Tuple[WitnessReport, ...],
) -> WitnessDecision:
    if not reports:
        raise ValueError("at least one witness report is required")

    same_count = reports.count(WitnessReport.SAME)
    polar_count = reports.count(WitnessReport.POLAR)

    if same_count == polar_count:
        resolved = None
    elif same_count > polar_count:
        resolved = WitnessReport.SAME
    else:
        resolved = WitnessReport.POLAR

    return WitnessDecision(
        reports=reports,
        resolved=resolved,
    )
