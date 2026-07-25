import unittest

from tm0.project42_quotient_graphs import (
    construct_project42_quotient_graphs,
    project42_carrier_edges,
    project42_carrier_vertices,
    project42_partitions,
)
from tm0.quotient_graph import canonical_carrier_edges


class TestProject42QuotientGraphs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.carrier_vertices = (
            project42_carrier_vertices()
        )
        cls.carrier_edges = project42_carrier_edges()
        cls.partitions = project42_partitions()
        cls.quotients = (
            construct_project42_quotient_graphs()
        )

    def test_carrier_has_thirty_vertices(self):
        self.assertEqual(
            len(self.carrier_vertices),
            30,
        )

    def test_carrier_has_sixty_edges(self):
        self.assertEqual(
            len(self.carrier_edges),
            60,
        )

    def test_three_partitions_are_loaded(self):
        self.assertEqual(
            len(self.partitions),
            3,
        )

    def test_each_partition_has_fifteen_classes(self):
        self.assertEqual(
            tuple(
                len(partition)
                for partition in self.partitions
            ),
            (
                15,
                15,
                15,
            ),
        )

    def test_each_class_has_two_vertices(self):
        for partition in self.partitions:
            self.assertTrue(
                all(
                    len(block) == 2
                    for block in partition
                )
            )

    def test_three_quotient_graphs_are_constructed(self):
        self.assertEqual(
            len(self.quotients),
            3,
        )

    def test_each_quotient_has_fifteen_vertices(self):
        self.assertEqual(
            tuple(
                len(quotient.quotient_vertices)
                for quotient in self.quotients
            ),
            (
                15,
                15,
                15,
            ),
        )

    def test_each_quotient_has_thirty_edges(self):
        self.assertEqual(
            tuple(
                len(quotient.quotient_edges)
                for quotient in self.quotients
            ),
            (
                30,
                30,
                30,
            ),
        )

    def test_every_carrier_edge_is_mapped(self):
        self.assertEqual(
            tuple(
                len(quotient.edge_map)
                for quotient in self.quotients
            ),
            (
                60,
                60,
                60,
            ),
        )

    def test_no_quotient_contains_loops(self):
        for quotient in self.quotients:
            self.assertTrue(
                all(
                    left != right
                    for left, right
                    in quotient.quotient_edges
                )
            )

    def test_every_quotient_edge_has_multiplicity_two(self):
        for quotient in self.quotients:
            multiplicities = (
                quotient.covering_multiplicities()
            )

            self.assertEqual(
                set(multiplicities.values()),
                {
                    2,
                },
            )
            self.assertEqual(
                len(multiplicities),
                30,
            )

    def test_quotient_construction_preserves_carrier(self):
        expected_vertices = frozenset(
            self.carrier_vertices
        )
        expected_edges = canonical_carrier_edges(
            self.carrier_edges
        )

        for quotient in self.quotients:
            self.assertEqual(
                quotient.carrier_vertices,
                expected_vertices,
            )
            self.assertEqual(
                quotient.carrier_edges,
                expected_edges,
            )


if __name__ == "__main__":
    unittest.main()
