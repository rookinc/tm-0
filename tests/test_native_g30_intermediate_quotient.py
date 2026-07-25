import unittest

from tm0.native_g30_intermediate_quotient import (
    derive_native_g30_intermediate_quotient,
    load_native_g60_v4_source,
)


class TestNativeG30IntermediateQuotient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = load_native_g60_v4_source()
        cls.receipt = derive_native_g30_intermediate_quotient()

    def test_source_certificate_passed(self):
        self.assertTrue(
            self.source["audit_pass"]
        )
        self.assertTrue(
            self.receipt["source_audit_pass"]
        )

    def test_native_g60_counts_are_retained(self):
        self.assertEqual(
            self.receipt["g60_vertex_count"],
            60,
        )
        self.assertEqual(
            self.receipt["g60_edge_count"],
            120,
        )

    def test_kernel_has_thirty_two_state_orbits(self):
        self.assertEqual(
            self.receipt["kernel_orbit_count"],
            30,
        )
        self.assertEqual(
            self.receipt["kernel_orbit_size_profile"],
            (
                2,
            ),
        )

    def test_g30_counts_are_correct(self):
        self.assertEqual(
            self.receipt["g30_vertex_count"],
            30,
        )
        self.assertEqual(
            self.receipt["g30_edge_count"],
            60,
        )

    def test_two_g60_edges_lie_above_each_g30_edge(self):
        self.assertEqual(
            self.receipt[
                "g60_to_g30_edge_multiplicity_profile"
            ],
            (
                2,
            ),
        )

    def test_g30_is_connected_quartic(self):
        self.assertEqual(
            self.receipt["g30_degree_profile"],
            (
                4,
            ),
        )
        self.assertEqual(
            self.receipt["g30_component_sizes"],
            (
                30,
            ),
        )

    def test_g30_has_twenty_triangles(self):
        self.assertEqual(
            self.receipt["g30_triangle_count"],
            20,
        )

    def test_g30_is_native_cover_class(self):
        self.assertTrue(
            self.receipt["native_cover_isomorphic"]
        )
        self.assertEqual(
            self.receipt["native_cover_mapping_size"],
            30,
        )

    def test_native_cover_mapping_is_bijection(self):
        mapping = self.receipt["native_cover_mapping"]

        self.assertIsNotNone(mapping)
        self.assertEqual(
            len(mapping),
            30,
        )
        self.assertEqual(
            len(set(mapping.values())),
            30,
        )

    def test_residual_classes_are_fifteen_pairs(self):
        self.assertEqual(
            self.receipt["residual_class_count"],
            15,
        )
        self.assertEqual(
            self.receipt["residual_class_size_profile"],
            (
                2,
            ),
        )

    def test_residual_quotient_has_g15_counts(self):
        self.assertEqual(
            self.receipt["g15_vertex_count"],
            15,
        )
        self.assertEqual(
            self.receipt["g15_edge_count"],
            30,
        )

    def test_two_g30_edges_lie_above_each_g15_edge(self):
        self.assertEqual(
            self.receipt[
                "g30_to_g15_edge_multiplicity_profile"
            ],
            (
                2,
            ),
        )

    def test_residual_quotient_is_LP(self):
        self.assertTrue(
            self.receipt["residual_isomorphic_to_LP"]
        )
        self.assertEqual(
            self.receipt["residual_LP_mapping_size"],
            15,
        )

    def test_quotient_square_commutes(self):
        self.assertTrue(
            self.receipt["quotient_square_commutes"]
        )


if __name__ == "__main__":
    unittest.main()
