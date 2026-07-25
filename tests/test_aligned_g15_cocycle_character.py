import unittest

from tm0.aligned_g15_cocycle_character import (
    classify_aligned_g15_cocycle,
)


class TestAlignedG15CocycleCharacter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = classify_aligned_g15_cocycle()

    def test_source_boundary_is_preserved(self):
        self.assertEqual(
            self.receipt["source_status"],
            "imported_from_aletheos_aligned_cocycle",
        )
        self.assertEqual(
            self.receipt["provenance_classification"],
            "aligned_imported_representative_native_origin_open",
        )

    def test_support_has_g15_counts(self):
        self.assertEqual(
            self.receipt["vertex_count"],
            15,
        )
        self.assertEqual(
            self.receipt["edge_count"],
            30,
        )
        self.assertEqual(
            self.receipt["component_count"],
            1,
        )

    def test_support_is_isomorphic_to_petersen_line_graph(self):
        self.assertTrue(
            self.receipt["support_isomorphic_to_LP"]
        )
        self.assertEqual(
            self.receipt["support_mapping_size"],
            15,
        )

    def test_cycle_rank_is_sixteen(self):
        self.assertEqual(
            self.receipt["cycle_rank"],
            16,
        )

    def test_signature_length_matches_cycle_rank(self):
        self.assertEqual(
            self.receipt["switching_signature_length"],
            self.receipt["cycle_rank"],
        )

    def test_negative_chord_count_is_bounded(self):
        self.assertGreaterEqual(
            self.receipt["negative_chord_count"],
            0,
        )
        self.assertLessEqual(
            self.receipt["negative_chord_count"],
            self.receipt["cycle_rank"],
        )

    def test_explicit_switch_is_nontrivial(self):
        self.assertGreater(
            self.receipt["explicit_switch_count"],
            0,
        )
        self.assertLess(
            self.receipt["explicit_switch_count"],
            self.receipt["vertex_count"],
        )

    def test_switching_signature_is_invariant(self):
        self.assertTrue(
            self.receipt["switching_invariant"]
        )
        self.assertEqual(
            self.receipt["switching_signature"],
            self.receipt["switched_signature"],
        )

    def test_support_mapping_is_bijection(self):
        mapping = self.receipt["support_mapping"]

        self.assertIsNotNone(mapping)
        self.assertEqual(
            len(mapping),
            15,
        )
        self.assertEqual(
            len(set(mapping.values())),
            15,
        )


if __name__ == "__main__":
    unittest.main()
