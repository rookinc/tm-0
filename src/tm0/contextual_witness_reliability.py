"""Context-indexed witness reliability for TM-0.

A witness may earn different reliability histories in different
character or boundary contexts.

Reliability is stored per context rather than as one global scalar.
"""

from dataclasses import dataclass
from typing import Dict

from .witness_arbitration import WitnessReport
from .witness_reliability import WitnessHistory
from .witness_reliability import evaluate_report


ContextName = str


@dataclass(frozen=True)
class ContextualWitnessHistory:
    histories: Dict[ContextName, WitnessHistory]


def empty_contextual_history() -> ContextualWitnessHistory:
    return ContextualWitnessHistory(histories={})


def history_for_context(
    contextual: ContextualWitnessHistory,
    context: ContextName,
) -> WitnessHistory:
    return contextual.histories.get(
        context,
        WitnessHistory(),
    )


def evaluate_in_context(
    contextual: ContextualWitnessHistory,
    context: ContextName,
    report: WitnessReport,
    closure_receipt: WitnessReport,
) -> ContextualWitnessHistory:
    current = history_for_context(
        contextual,
        context,
    )

    evaluation = evaluate_report(
        current,
        report,
        closure_receipt,
    )

    updated = dict(contextual.histories)
    updated[context] = evaluation.history

    return ContextualWitnessHistory(
        histories=updated,
    )


def contextual_reliability(
    contextual: ContextualWitnessHistory,
    context: ContextName,
) -> int:
    return history_for_context(
        contextual,
        context,
    ).net_reliability
