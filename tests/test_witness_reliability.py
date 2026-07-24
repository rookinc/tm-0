import unittest

from tm0.witness_arbitration import WitnessReport
from tm0.witness_reliability import WitnessHistory
from tm0.witness_reliability import compare_histories
from tm0.witness_reliability import evaluate_report


class TestWitnessReliability(unittest.TestCase):
    def test_agreement_adds_confirmation(self):
        result = evaluate_report(
            WitnessHistory(),
            WitnessReport.SAME,
            WitnessReport.SAME,
        )

        self.assertTrue(result.agreed)
        self.assertEqual(result.history.confirmed, 1)
        self.assertEqual(result.history.contradicted, 0)
        self.assertEqual(result.history.net_reliability, 1)

    def test_disagreement_adds_contradiction(self):
        result = evaluate_report(
            WitnessHistory(),
            WitnessReport.SAME,
            WitnessReport.POLAR,
        )

        self.assertFalse(result.agreed)
        self.assertEqual(result.history.confirmed, 0)
        self.assertEqual(result.history.contradicted, 1)
        self.assertEqual(result.history.net_reliability, -1)

    def test_history_accumulates_across_receipts(self):
        history = WitnessHistory()

        first = evaluate_report(
            history,
            WitnessReport.SAME,
            WitnessReport.SAME,
        )

        second = evaluate_report(
            first.history,
            WitnessReport.POLAR,
            WitnessReport.POLAR,
        )

        third = evaluate_report(
            second.history,
            WitnessReport.SAME,
            WitnessReport.POLAR,
        )

        self.assertEqual(third.history.confirmed, 2)
        self.assertEqual(third.history.contradicted, 1)
        self.assertEqual(third.history.total, 3)
        self.assertEqual(third.history.net_reliability, 1)

    def test_more_reliable_history_compares_higher(self):
        left = WitnessHistory(
            confirmed=3,
            contradicted=1,
        )

        right = WitnessHistory(
            confirmed=1,
            contradicted=2,
        )

        self.assertEqual(
            compare_histories(left, right),
            1,
        )

    def test_equal_net_reliability_compares_equal(self):
        left = WitnessHistory(
            confirmed=3,
            contradicted=1,
        )

        right = WitnessHistory(
            confirmed=4,
            contradicted=2,
        )

        self.assertEqual(
            compare_histories(left, right),
            0,
        )

    def test_reliability_is_not_present_without_receipts(self):
        history = WitnessHistory()

        self.assertEqual(history.total, 0)
        self.assertEqual(history.net_reliability, 0)


if __name__ == "__main__":
    unittest.main()
