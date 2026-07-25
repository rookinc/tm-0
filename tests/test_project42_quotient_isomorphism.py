import unittest

from tm0.project42_quotient_isomorphism import (
    certify_project42_quotients_as_petersen_line_graphs,
)


class TestProject42QuotientIsomorphism(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = (
            certify_project42_quotients_as_petersen_line_graphs()
        )

    def test_three_quotients_are_checked(self):
        self.assertEqual(
            self.receipt["quotient_count"],
            3,
        )

    def test_target_is_fifteen_vertex_thirty_edge_graph(self):
        self.assertEqual(
            self.receipt["target_vertex_count"],
            15,
        )
        self.assertEqual(
            self.receipt["target_edge_count"],
            30,
        )

    def test_each_quotient_has_explicit_LP_isomorphism(self):
        self.assertEqual(
            self.receipt["mapping_exists"],
            (
                True,
                True,
                True,
            ),
        )

        self.assertEqual(
            self.receipt["mapping_sizes"],
            (
                15,
                15,
                15,
            ),
        )

        self.assertTrue(
            self.receipt["all_quotients_are_LP"]
        )

    def test_all_three_pairwise_isomorphisms_exist(self):
        self.assertEqual(
            self.receipt["pairwise_mapping_exists"],
            (
                True,
                True,
                True,
            ),
        )

        self.assertTrue(
            self.receipt[
                "all_quotients_pairwise_isomorphic"
            ]
        )

    def test_LP_mappings_are_bijections(self):
        for mapping in self.receipt["mappings"]:
            self.assertIsNotNone(mapping)
            self.assertEqual(
                len(mapping),
                15,
            )
            self.assertEqual(
                len(set(mapping.values())),
                15,
            )

    def test_pairwise_mappings_are_bijections(self):
        for left_index, right_index, mapping in self.receipt[
            "pairwise_mappings"
        ]:
            self.assertLess(
                left_index,
                right_index,
            )
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
