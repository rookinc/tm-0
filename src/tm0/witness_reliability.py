"""Witness reliability from later closure receipts.

A witness report is compared with a later closure receipt.

Agreement adds one confirmed report.

Disagreement adds one contradicted report.

Reliability is not assumed in advance.
It is represented by the accumulated record.
"""

from dataclasses import dataclass

from .witness_arbitration import WitnessReport


@dataclass(frozen=True)
class WitnessHistory:
    confirmed: int = 0
    contradicted: int = 0

    @property
    def total(self) -> int:
        return self.confirmed + self.contradicted

    @property
    def net_reliability(self) -> int:
        return self.confirmed - self.contradicted


@dataclass(frozen=True)
class WitnessEvaluation:
    report: WitnessReport
    closure_receipt: WitnessReport
    agreed: bool
    history: WitnessHistory


def evaluate_report(
    history: WitnessHistory,
    report: WitnessReport,
    closure_receipt: WitnessReport,
) -> WitnessEvaluation:
    agreed = report is closure_receipt

    updated = WitnessHistory(
        confirmed=history.confirmed + int(agreed),
        contradicted=history.contradicted + int(not agreed),
    )

    return WitnessEvaluation(
        report=report,
        closure_receipt=closure_receipt,
        agreed=agreed,
        history=updated,
    )


def compare_histories(
    left: WitnessHistory,
    right: WitnessHistory,
) -> int:
    if left.net_reliability < right.net_reliability:
        return -1

    if left.net_reliability > right.net_reliability:
        return 1

    return 0
