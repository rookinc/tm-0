import unittest

from tm0.aligned_g15_signed_double_cover import (
    classify_aligned_g15_signed_double_cover,
)


class TestAlignedG15SignedDoubleCover(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = (
            classify_aligned_g15_signed_double_cover()
        )

    def test_source_boundary_is_preserved(self):
        self.assertEqual(
            self.receipt["source_status"],
            "imported_from_aletheos_aligned_cocycle",
        )
        self.assertEqual(
            self.receipt["provenance_classification"],
            "aligned_imported_representative_native_origin_open",
        )

    def test_base_counts_are_correct(self):
        self.assertEqual(
            self.receipt["base_vertex_count"],
            15,
        )
        self.assertEqual(
            self.receipt["base_edge_count"],
            30,
        )

    def test_sign_class_counts_are_preserved(self):
        self.assertEqual(
            self.receipt["parallel_base_edge_count"],
            10,
        )
        self.assertEqual(
            self.receipt["crossed_base_edge_count"],
            20,
        )

    def test_lift_counts_are_correct(self):
        self.assertEqual(
            self.receipt["lift_vertex_count"],
            30,
        )
        self.assertEqual(
            self.receipt["lift_edge_count"],
            60,
        )

    def test_lift_is_quartic(self):
        self.assertEqual(
            self.receipt["degree_profile"],
            (
                4,
            ),
        )

    def test_lift_is_connected(self):
        self.assertEqual(
            self.receipt["component_count"],
            1,
        )
        self.assertEqual(
            self.receipt["component_sizes"],
            (
                30,
            ),
        )

    def test_sheet_swap_has_fifteen_orbits(self):
        self.assertEqual(
            self.receipt["sheet_swap_orbit_count"],
            15,
        )

    def test_sheet_swap_preserves_lift_edges(self):
        self.assertTrue(
            self.receipt["sheet_swap_preserves_edges"]
        )

    def test_explicit_switch_is_nontrivial(self):
        self.assertEqual(
            self.receipt["explicit_switch_count"],
            7,
        )

    def test_switched_signing_produces_isomorphic_lift(self):
        self.assertTrue(
            self.receipt["switched_cover_isomorphic"]
        )
        self.assertEqual(
            self.receipt["switched_cover_mapping_size"],
            30,
        )

    def test_switched_cover_mapping_is_bijection(self):
        mapping = self.receipt["switched_cover_mapping"]

        self.assertIsNotNone(mapping)
        self.assertEqual(
            len(mapping),
            30,
        )
        self.assertEqual(
            len(set(mapping.values())),
            30,
        )


if __name__ == "__main__":
    unittest.main()
