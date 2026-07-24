import unittest

from tm0.reliability_weighted_witness import WeightedWitness
from tm0.reliability_weighted_witness import reliability_weighted_decision
from tm0.witness_arbitration import WitnessReport
from tm0.witness_reliability import WitnessHistory


class TestReliabilityWeightedWitness(unittest.TestCase):
    def test_equal_weight_is_unresolved(self):
        witnesses = (
            WeightedWitness(
                report=WitnessReport.SAME,
                history=WitnessHistory(
                    confirmed=2,
                    contradicted=1,
                ),
            ),
            WeightedWitness(
                report=WitnessReport.POLAR,
                history=WitnessHistory(
                    confirmed=3,
                    contradicted=2,
                ),
            ),
        )

        decision = reliability_weighted_decision(witnesses)

        self.assertFalse(decision.is_resolved)
        self.assertEqual(decision.same_weight, 1)
        self.assertEqual(decision.polar_weight, 1)

    def test_more_reliable_report_resolves(self):
        witnesses = (
            WeightedWitness(
                report=WitnessReport.SAME,
                history=WitnessHistory(
                    confirmed=5,
                    contradicted=1,
                ),
            ),
            WeightedWitness(
                report=WitnessReport.POLAR,
                history=WitnessHistory(
                    confirmed=2,
                    contradicted=1,
                ),
            ),
        )

        decision = reliability_weighted_decision(witnesses)

        self.assertTrue(decision.is_resolved)
        self.assertEqual(
            decision.resolved,
            WitnessReport.SAME,
        )

    def test_one_reliable_dissent_can_outweigh_two_weak_reports(self):
        witnesses = (
            WeightedWitness(
                report=WitnessReport.POLAR,
                history=WitnessHistory(
                    confirmed=6,
                    contradicted=1,
                ),
            ),
            WeightedWitness(
                report=WitnessReport.SAME,
                history=WitnessHistory(
                    confirmed=1,
                    contradicted=0,
                ),
            ),
            WeightedWitness(
                report=WitnessReport.SAME,
                history=WitnessHistory(
                    confirmed=1,
                    contradicted=0,
                ),
            ),
        )

        decision = reliability_weighted_decision(witnesses)

        self.assertEqual(decision.same_weight, 2)
        self.assertEqual(decision.polar_weight, 5)
        self.assertEqual(
            decision.resolved,
            WitnessReport.POLAR,
        )

    def test_unproven_witness_has_zero_weight(self):
        witness = WeightedWitness(
            report=WitnessReport.SAME,
            history=WitnessHistory(),
        )

        self.assertEqual(witness.weight, 0)

    def test_negative_reliability_counts_against_report(self):
        witnesses = (
            WeightedWitness(
                report=WitnessReport.SAME,
                history=WitnessHistory(
                    confirmed=1,
                    contradicted=3,
                ),
            ),
            WeightedWitness(
                report=WitnessReport.POLAR,
                history=WitnessHistory(
                    confirmed=1,
                    contradicted=0,
                ),
            ),
        )

        decision = reliability_weighted_decision(witnesses)

        self.assertEqual(decision.same_weight, -2)
        self.assertEqual(decision.polar_weight, 1)
        self.assertEqual(
            decision.resolved,
            WitnessReport.POLAR,
        )

    def test_empty_witness_set_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "at least one weighted witness is required",
        ):
            reliability_weighted_decision(())


if __name__ == "__main__":
    unittest.main()
