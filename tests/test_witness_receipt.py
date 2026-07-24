import unittest

from tm0.witness_arbitration import WitnessReport
from tm0.witness_receipt import WitnessReceipt
from tm0.witness_receipt import decide_from_independent_receipts
from tm0.witness_receipt import independent_receipts


class TestWitnessReceipt(unittest.TestCase):
    def test_duplicate_source_is_not_independent(self):
        first = WitnessReceipt(
            report=WitnessReport.SAME,
            source_occurrence="o1",
            observation_path=("p1",),
        )

        duplicate = WitnessReceipt(
            report=WitnessReport.SAME,
            source_occurrence="o1",
            observation_path=("p2",),
        )

        result = independent_receipts(
            (first, duplicate)
        )

        self.assertEqual(result, (first,))

    def test_duplicate_path_is_not_independent(self):
        first = WitnessReceipt(
            report=WitnessReport.SAME,
            source_occurrence="o1",
            observation_path=("p1",),
        )

        duplicate = WitnessReceipt(
            report=WitnessReport.SAME,
            source_occurrence="o2",
            observation_path=("p1",),
        )

        result = independent_receipts(
            (first, duplicate)
        )

        self.assertEqual(result, (first,))

    def test_two_independent_conflicting_receipts_are_unresolved(self):
        first = WitnessReceipt(
            report=WitnessReport.SAME,
            source_occurrence="o1",
            observation_path=("p1",),
        )

        second = WitnessReceipt(
            report=WitnessReport.POLAR,
            source_occurrence="o2",
            observation_path=("p2",),
        )

        decision = decide_from_independent_receipts(
            (first, second)
        )

        self.assertFalse(decision.is_resolved)
        self.assertEqual(decision.independent_count, 2)

    def test_three_independent_receipts_can_resolve(self):
        receipts = (
            WitnessReceipt(
                report=WitnessReport.SAME,
                source_occurrence="o1",
                observation_path=("p1",),
            ),
            WitnessReceipt(
                report=WitnessReport.SAME,
                source_occurrence="o2",
                observation_path=("p2",),
            ),
            WitnessReceipt(
                report=WitnessReport.POLAR,
                source_occurrence="o3",
                observation_path=("p3",),
            ),
        )

        decision = decide_from_independent_receipts(receipts)

        self.assertTrue(decision.is_resolved)
        self.assertEqual(decision.independent_count, 3)
        self.assertEqual(
            decision.resolved,
            WitnessReport.SAME,
        )

    def test_duplicate_vote_does_not_break_tie(self):
        receipts = (
            WitnessReceipt(
                report=WitnessReport.SAME,
                source_occurrence="o1",
                observation_path=("p1",),
            ),
            WitnessReceipt(
                report=WitnessReport.POLAR,
                source_occurrence="o2",
                observation_path=("p2",),
            ),
            WitnessReceipt(
                report=WitnessReport.SAME,
                source_occurrence="o1",
                observation_path=("p3",),
            ),
        )

        decision = decide_from_independent_receipts(receipts)

        self.assertFalse(decision.is_resolved)
        self.assertEqual(decision.independent_count, 2)


if __name__ == "__main__":
    unittest.main()
