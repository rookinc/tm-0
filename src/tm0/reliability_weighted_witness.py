"""Reliability-weighted witness arbitration for TM-0.

Each witness contributes the net reliability earned from prior closure
history.

The report with greater total reliability weight resolves the current
disagreement.

Equal total weight remains unresolved.

This is a bounded arbitration scaffold.
"""

from dataclasses import dataclass
from typing import Optional
from typing import Tuple

from .witness_arbitration import WitnessReport
from .witness_reliability import WitnessHistory


@dataclass(frozen=True)
class WeightedWitness:
    report: WitnessReport
    history: WitnessHistory

    @property
    def weight(self) -> int:
        return self.history.net_reliability


@dataclass(frozen=True)
class WeightedDecision:
    witnesses: Tuple[WeightedWitness, ...]
    same_weight: int
    polar_weight: int
    resolved: Optional[WitnessReport]

    @property
    def is_resolved(self) -> bool:
        return self.resolved is not None


def reliability_weighted_decision(
    witnesses: Tuple[WeightedWitness, ...],
) -> WeightedDecision:
    if not witnesses:
        raise ValueError("at least one weighted witness is required")

    same_weight = sum(
        witness.weight
        for witness in witnesses
        if witness.report is WitnessReport.SAME
    )

    polar_weight = sum(
        witness.weight
        for witness in witnesses
        if witness.report is WitnessReport.POLAR
    )

    if same_weight == polar_weight:
        resolved = None
    elif same_weight > polar_weight:
        resolved = WitnessReport.SAME
    else:
        resolved = WitnessReport.POLAR

    return WeightedDecision(
        witnesses=witnesses,
        same_weight=same_weight,
        polar_weight=polar_weight,
        resolved=resolved,
    )
