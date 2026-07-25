import unittest

from tm0.native_g15_voltage_comparison import (
    compare_aligned_to_native_voltage,
    load_native_voltage_certificate,
)


class TestNativeG15VoltageComparison(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = load_native_voltage_certificate()
        cls.receipt = compare_aligned_to_native_voltage()

    def test_native_certificate_passed(self):
        self.assertTrue(
            self.certificate["audit_pass"]
        )
        self.assertTrue(
            self.receipt["certificate_audit_pass"]
        )

    def test_native_derivation_counts_are_retained(self):
        self.assertEqual(
            self.receipt["native_g60_state_count"],
            60,
        )
        self.assertEqual(
            self.receipt["native_g60_edge_count"],
            120,
        )
        self.assertEqual(
            self.receipt["native_g15_edge_count"],
            30,
        )

    def test_native_bit_law_is_retained(self):
        self.assertEqual(
            self.receipt["native_bit_law"],
            "native_bit = delta_coordinate_0 xor delta_coordinate_1",
        )

    def test_native_and_aligned_bit_counts_agree(self):
        self.assertEqual(
            self.receipt["native_bit_counts"],
            {
                "0": 10,
                "1": 20,
            },
        )
        self.assertEqual(
            self.receipt["aligned_bit_counts"],
            {
                "0": 10,
                "1": 20,
            },
        )

    def test_switching_signed_isomorphism_exists(self):
        self.assertTrue(
            self.receipt[
                "switching_signed_isomorphism_exists"
            ]
        )
        self.assertEqual(
            self.receipt["graph_isomorphism_size"],
            15,
        )
        self.assertEqual(
            self.receipt["switch_assignment_size"],
            15,
        )

    def test_graph_isomorphism_is_bijection(self):
        mapping = self.receipt["graph_isomorphism"]

        self.assertIsNotNone(mapping)
        self.assertEqual(
            len(mapping),
            15,
        )
        self.assertEqual(
            len(set(mapping.values())),
            15,
        )

    def test_switch_assignment_is_nontrivial(self):
        switches = self.receipt["switches"]

        self.assertIsNotNone(switches)
        self.assertEqual(
            len(switches),
            15,
        )
        self.assertEqual(
            self.receipt["switch_count"],
            11,
        )
        self.assertEqual(
            set(switches.values()),
            {
                0,
                1,
            },
        )

    def test_aligned_signing_matches_native_switching_class(self):
        self.assertTrue(
            self.receipt[
                "aligned_matches_g60_derived_native_switching_class"
            ]
        )

    def test_exact_edgewise_identity_is_not_claimed(self):
        self.assertFalse(
            self.receipt["exact_edgewise_identity_claimed"]
        )

    def test_historical_writer_remains_open(self):
        self.assertFalse(
            self.receipt["historical_writer_identified"]
        )


if __name__ == "__main__":
    unittest.main()
