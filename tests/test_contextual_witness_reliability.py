import unittest

from tm0.contextual_witness_reliability import contextual_reliability
from tm0.contextual_witness_reliability import empty_contextual_history
from tm0.contextual_witness_reliability import evaluate_in_context
from tm0.contextual_witness_reliability import history_for_context
from tm0.witness_arbitration import WitnessReport


class TestContextualWitnessReliability(unittest.TestCase):
    def test_unknown_context_starts_unearned(self):
        history = empty_contextual_history()

        self.assertEqual(
            contextual_reliability(history, "same-boundary"),
            0,
        )

    def test_confirmation_updates_only_one_context(self):
        history = empty_contextual_history()

        updated = evaluate_in_context(
            history,
            "same-boundary",
            WitnessReport.SAME,
            WitnessReport.SAME,
        )

        self.assertEqual(
            contextual_reliability(
                updated,
                "same-boundary",
            ),
            1,
        )

        self.assertEqual(
            contextual_reliability(
                updated,
                "changed-boundary",
            ),
            0,
        )

    def test_contradiction_updates_only_one_context(self):
        history = empty_contextual_history()

        updated = evaluate_in_context(
            history,
            "changed-boundary",
            WitnessReport.SAME,
            WitnessReport.POLAR,
        )

        self.assertEqual(
            contextual_reliability(
                updated,
                "changed-boundary",
            ),
            -1,
        )

        self.assertEqual(
            contextual_reliability(
                updated,
                "same-boundary",
            ),
            0,
        )

    def test_same_witness_can_differ_by_context(self):
        history = empty_contextual_history()

        history = evaluate_in_context(
            history,
            "same-boundary",
            WitnessReport.SAME,
            WitnessReport.SAME,
        )

        history = evaluate_in_context(
            history,
            "same-boundary",
            WitnessReport.POLAR,
            WitnessReport.POLAR,
        )

        history = evaluate_in_context(
            history,
            "changed-boundary",
            WitnessReport.SAME,
            WitnessReport.POLAR,
        )

        self.assertEqual(
            contextual_reliability(
                history,
                "same-boundary",
            ),
            2,
        )

        self.assertEqual(
            contextual_reliability(
                history,
                "changed-boundary",
            ),
            -1,
        )

    def test_context_history_is_accumulated(self):
        history = empty_contextual_history()

        history = evaluate_in_context(
            history,
            "same-boundary",
            WitnessReport.SAME,
            WitnessReport.SAME,
        )

        history = evaluate_in_context(
            history,
            "same-boundary",
            WitnessReport.POLAR,
            WitnessReport.SAME,
        )

        context = history_for_context(
            history,
            "same-boundary",
        )

        self.assertEqual(context.confirmed, 1)
        self.assertEqual(context.contradicted, 1)
        self.assertEqual(context.net_reliability, 0)


if __name__ == "__main__":
    unittest.main()
