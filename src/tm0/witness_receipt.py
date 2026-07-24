"""Witness receipts with provenance for TM-0.

A witness receipt contains:

    report
    source occurrence
    observation path

Receipts are independent when they do not share the same source
occurrence or the same observation path.

This is a bounded provenance model.
It does not yet establish truth or reliability.
"""

from dataclasses import dataclass
from typing import Optional
from typing import Tuple

from .witness_arbitration import WitnessReport


@dataclass(frozen=True)
class WitnessReceipt:
    report: WitnessReport
    source_occurrence: str
    observation_path: Tuple[str, ...]


@dataclass(frozen=True)
class ReceiptDecision:
    receipts: Tuple[WitnessReceipt, ...]
    resolved: Optional[WitnessReport]
    independent_count: int

    @property
    def is_resolved(self) -> bool:
        return self.resolved is not None


def independent_receipts(
    receipts: Tuple[WitnessReceipt, ...],
) -> Tuple[WitnessReceipt, ...]:
    independent = []
    seen_sources = set()
    seen_paths = set()

    for receipt in receipts:
        if receipt.source_occurrence in seen_sources:
            continue

        if receipt.observation_path in seen_paths:
            continue

        independent.append(receipt)
        seen_sources.add(receipt.source_occurrence)
        seen_paths.add(receipt.observation_path)

    return tuple(independent)


def decide_from_independent_receipts(
    receipts: Tuple[WitnessReceipt, ...],
) -> ReceiptDecision:
    independent = independent_receipts(receipts)

    same_count = sum(
        1
        for receipt in independent
        if receipt.report is WitnessReport.SAME
    )

    polar_count = sum(
        1
        for receipt in independent
        if receipt.report is WitnessReport.POLAR
    )

    if same_count == polar_count:
        resolved = None
    elif same_count > polar_count:
        resolved = WitnessReport.SAME
    else:
        resolved = WitnessReport.POLAR

    return ReceiptDecision(
        receipts=receipts,
        resolved=resolved,
        independent_count=len(independent),
    )
