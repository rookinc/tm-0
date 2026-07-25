import unittest

from tm0.project42_quotient_certificate import (
    certify_project42_quotient_graphs,
    expected_quotient_edges,
    load_quotient_certificate,
)


class TestProject42QuotientCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = load_quotient_certificate()
        cls.expected_edges = expected_quotient_edges()
        cls.receipt = certify_project42_quotient_graphs()

    def test_source_certificate_passed(self):
        self.assertTrue(
            self.certificate["audit_pass"]
        )

    def test_three_expected_quotient_edge_sets_loaded(self):
        self.assertEqual(
            len(self.expected_edges),
            3,
        )

    def test_each_expected_quotient_has_thirty_edges(self):
        self.assertEqual(
            tuple(
                len(edges)
                for edges in self.expected_edges
            ),
            (
                30,
                30,
                30,
            ),
        )

    def test_three_derived_quotients_are_certified(self):
        self.assertEqual(
            self.receipt["quotient_count"],
            3,
        )

    def test_vertex_counts_are_certified(self):
        self.assertEqual(
            self.receipt["vertex_counts"],
            (
                15,
                15,
                15,
            ),
        )

    def test_edge_counts_are_certified(self):
        self.assertEqual(
            self.receipt["edge_counts"],
            (
                30,
                30,
                30,
            ),
        )

    def test_all_derived_edge_sets_match_certificate(self):
        self.assertEqual(
            self.receipt["edge_matches"],
            (
                True,
                True,
                True,
            ),
        )
        self.assertTrue(
            self.receipt["all_edge_sets_match"]
        )

    def test_every_covering_multiplicity_is_two(self):
        self.assertTrue(
            self.receipt[
                "all_multiplicities_are_two"
            ]
        )

        for profile in self.receipt[
            "multiplicity_profiles"
        ]:
            self.assertEqual(
                len(profile),
                30,
            )
            self.assertEqual(
                set(profile),
                {
                    2,
                },
            )


if __name__ == "__main__":
    unittest.main()
