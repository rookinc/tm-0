import unittest

from tm0.witness_arbitration import WitnessReport
from tm0.witness_arbitration import strict_majority_decision
from tm0.witness_arbitration import unanimous_decision


class TestWitnessArbitration(unittest.TestCase):
    def test_one_report_resolves_trivially(self):
        decision = unanimous_decision(
            (WitnessReport.SAME,)
        )

        self.assertTrue(decision.is_resolved)
        self.assertEqual(
            decision.resolved,
            WitnessReport.SAME,
        )

    def test_two_equal_reports_reach_consensus(self):
        decision = unanimous_decision(
            (
                WitnessReport.POLAR,
                WitnessReport.POLAR,
            )
        )

        self.assertTrue(decision.is_resolved)
        self.assertEqual(
            decision.resolved,
            WitnessReport.POLAR,
        )

    def test_two_conflicting_reports_are_unresolved(self):
        decision = strict_majority_decision(
            (
                WitnessReport.SAME,
                WitnessReport.POLAR,
            )
        )

        self.assertFalse(decision.is_resolved)
        self.assertIsNone(decision.resolved)

    def test_three_reports_can_resolve_same(self):
        decision = strict_majority_decision(
            (
                WitnessReport.SAME,
                WitnessReport.SAME,
                WitnessReport.POLAR,
            )
        )

        self.assertTrue(decision.is_resolved)
        self.assertEqual(
            decision.resolved,
            WitnessReport.SAME,
        )

    def test_three_reports_can_resolve_polar(self):
        decision = strict_majority_decision(
            (
                WitnessReport.POLAR,
                WitnessReport.POLAR,
                WitnessReport.SAME,
            )
        )

        self.assertTrue(decision.is_resolved)
        self.assertEqual(
            decision.resolved,
            WitnessReport.POLAR,
        )

    def test_unanimity_rejects_any_disagreement(self):
        decision = unanimous_decision(
            (
                WitnessReport.SAME,
                WitnessReport.SAME,
                WitnessReport.POLAR,
            )
        )

        self.assertFalse(decision.is_resolved)

    def test_empty_reports_are_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "at least one witness report is required",
        ):
            strict_majority_decision(())


if __name__ == "__main__":
    unittest.main()
