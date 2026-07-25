import unittest

from tm0.quotient_graph import (
    canonical_carrier_edges,
    construct_quotient_graph,
)


class TestQuotientGraph(unittest.TestCase):
    def setUp(self):
        self.carrier_vertices = (
            "A",
            "B",
            "C",
            "D",
        )

        self.carrier_edges = (
            ("A", "C"),
            ("A", "D"),
            ("B", "C"),
            ("B", "D"),
        )

        self.partition = (
            ("A", "B"),
            ("C", "D"),
        )

    def test_carrier_edges_are_canonicalized(self):
        edges = canonical_carrier_edges(
            (
                ("D", "A"),
                ("A", "D"),
                ("C", "B"),
            )
        )

        self.assertEqual(
            edges,
            (
                ("A", "D"),
                ("B", "C"),
            ),
        )

    def test_partition_derives_two_quotient_vertices(self):
        quotient = construct_quotient_graph(
            self.carrier_vertices,
            self.carrier_edges,
            self.partition,
        )

        self.assertEqual(
            quotient.quotient_vertices,
            (
                0,
                1,
            ),
        )

    def test_parallel_carrier_edges_collapse_to_one_edge(self):
        quotient = construct_quotient_graph(
            self.carrier_vertices,
            self.carrier_edges,
            self.partition,
        )

        self.assertEqual(
            quotient.quotient_edges,
            (
                (0, 1),
            ),
        )

    def test_every_carrier_edge_is_recorded(self):
        quotient = construct_quotient_graph(
            self.carrier_vertices,
            self.carrier_edges,
            self.partition,
        )

        self.assertEqual(
            len(quotient.edge_map),
            4,
        )

    def test_covering_multiplicity_is_derived(self):
        quotient = construct_quotient_graph(
            self.carrier_vertices,
            self.carrier_edges,
            self.partition,
        )

        self.assertEqual(
            quotient.covering_multiplicities(),
            {
                (0, 1): 4,
            },
        )

    def test_carrier_is_not_mutated(self):
        quotient = construct_quotient_graph(
            self.carrier_vertices,
            self.carrier_edges,
            self.partition,
        )

        self.assertEqual(
            quotient.carrier_vertices,
            frozenset(self.carrier_vertices),
        )
        self.assertEqual(
            quotient.partition,
            (
                ("A", "B"),
                ("C", "D"),
            ),
        )

    def test_partition_must_cover_carrier(self):
        with self.assertRaisesRegex(
            ValueError,
            "must cover the carrier",
        ):
            construct_quotient_graph(
                self.carrier_vertices,
                self.carrier_edges,
                (
                    ("A", "B"),
                    ("C",),
                ),
            )

    def test_partition_classes_must_be_disjoint(self):
        with self.assertRaisesRegex(
            ValueError,
            "must be disjoint",
        ):
            construct_quotient_graph(
                self.carrier_vertices,
                self.carrier_edges,
                (
                    ("A", "B"),
                    ("B", "C", "D"),
                ),
            )

    def test_unregistered_edge_vertex_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "unregistered vertex",
        ):
            construct_quotient_graph(
                self.carrier_vertices,
                (
                    ("A", "X"),
                ),
                self.partition,
            )

    def test_internal_carrier_edge_is_rejected_as_loop(self):
        with self.assertRaisesRegex(
            ValueError,
            "collapses to a quotient loop",
        ):
            construct_quotient_graph(
                self.carrier_vertices,
                (
                    ("A", "B"),
                    ("A", "C"),
                ),
                self.partition,
            )


if __name__ == "__main__":
    unittest.main()
