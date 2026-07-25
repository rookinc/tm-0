import unittest

from tm0.historical_g30_identification import (
    identify_historical_g30,
    load_historical_g30_source,
    load_historical_g60_label_bundle,
)


class TestHistoricalG30Identification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.historical = load_historical_g30_source()
        cls.bundle = load_historical_g60_label_bundle()
        cls.receipt = identify_historical_g30()

    def test_historical_source_is_complete(self):
        self.assertEqual(
            self.receipt["historical_source_status"],
            "complete",
        )
        self.assertTrue(
            self.receipt["historical_source_isomorphic"]
        )

    def test_historical_reconstruction_is_retained(self):
        self.assertEqual(
            self.receipt["historical_reconstruction"],
            (
                "hyperxi_lab/scripts/load_thalean_graph.py "
                "followed by antipode quotient G60 -> G30"
            ),
        )

    def test_old_to_current_map_is_complete(self):
        self.assertEqual(
            self.receipt["old_to_current_map_count"],
            60,
        )

    def test_both_partitions_have_thirty_classes(self):
        self.assertEqual(
            self.receipt["historical_class_count"],
            30,
        )
        self.assertEqual(
            self.receipt["derived_kernel_class_count"],
            30,
        )

    def test_both_partitions_have_two_state_classes(self):
        self.assertEqual(
            self.receipt["historical_class_size_profile"],
            (
                2,
            ),
        )
        self.assertEqual(
            self.receipt["derived_class_size_profile"],
            (
                2,
            ),
        )

    def test_partitions_match_exactly(self):
        self.assertTrue(
            self.receipt["exact_partition_match"]
        )
        self.assertEqual(
            self.receipt["historical_only_count"],
            0,
        )
        self.assertEqual(
            self.receipt["derived_only_count"],
            0,
        )
        self.assertEqual(
            self.receipt["historical_only"],
            (),
        )
        self.assertEqual(
            self.receipt["derived_only"],
            (),
        )

    def test_historical_g30_is_native_kernel_quotient(self):
        self.assertTrue(
            self.receipt[
                "historical_g30_is_native_parity_kernel_quotient"
            ]
        )

    def test_intrinsic_identification_is_explicit(self):
        self.assertEqual(
            self.receipt["intrinsic_identification"],
            (
                "historical antipode quotient equals "
                "G60 / ker(chi), chi(x,y)=x xor y"
            ),
        )

    def test_partition_rows_are_identical(self):
        self.assertEqual(
            self.receipt["historical_classes_current"],
            self.receipt["derived_kernel_classes"],
        )


if __name__ == "__main__":
    unittest.main()
