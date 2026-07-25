import unittest

from tm0.native_g15_cocycle_authentication import (
    authenticate_native_g15_cocycle,
)


class TestNativeG15CocycleAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = authenticate_native_g15_cocycle()

    def test_authentication_passes(self):
        self.assertTrue(
            self.receipt["authentication_pass"]
        )

    def test_claim_is_bounded(self):
        self.assertEqual(
            self.receipt["claim"],
            (
                "retained aligned artifact is an authenticated "
                "representative of the native G60-derived G15 "
                "switching class"
            ),
        )

    def test_source_hashes_are_present(self):
        self.assertEqual(
            len(self.receipt["aligned_source_sha256"]),
            64,
        )
        self.assertEqual(
            len(self.receipt["native_certificate_sha256"]),
            64,
        )

    def test_native_law_is_retained(self):
        self.assertEqual(
            self.receipt["native_bit_law"],
            "native_bit = delta_coordinate_0 xor delta_coordinate_1",
        )

    def test_relabeling_is_bijection(self):
        mapping = self.receipt["graph_relabeling"]

        self.assertEqual(
            len(mapping),
            15,
        )
        self.assertEqual(
            len(set(mapping.values())),
            15,
        )

    def test_switch_assignment_is_complete(self):
        switches = self.receipt["switch_assignment"]

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

    def test_all_thirty_edges_verify(self):
        self.assertEqual(
            self.receipt["tested_edge_count"],
            30,
        )
        self.assertEqual(
            self.receipt["matching_edge_count"],
            30,
        )
        self.assertEqual(
            self.receipt["mismatching_edge_count"],
            0,
        )

        self.assertTrue(
            all(
                row["matches"]
                for row in self.receipt["verification_rows"]
            )
        )

    def test_native_cover_class_is_confirmed(self):
        self.assertTrue(
            self.receipt["native_cover_class_match"]
        )
        self.assertEqual(
            self.receipt["native_cover_matching_classes"],
            (
                "native",
            ),
        )

    def test_one_bit_tamper_is_detected(self):
        tamper = self.receipt["tamper_test"]

        self.assertTrue(
            tamper["tamper_detected"]
        )
        self.assertGreaterEqual(
            tamper["tamper_mismatch_count"],
            1,
        )

    def test_historical_provenance_remains_open(self):
        self.assertFalse(
            self.receipt["historical_writer_identified"]
        )
        self.assertFalse(
            self.receipt[
                "historical_generation_reconstructed"
            ]
        )


if __name__ == "__main__":
    unittest.main()
