import unittest

from tm0.finite_graph_isomorphism import adjacency_map
from tm0.petersen_line_graph import (
    petersen_edges,
    petersen_line_graph_edges,
    petersen_line_graph_vertices,
    petersen_vertices,
)


class TestPetersenLineGraph(unittest.TestCase):
    def test_petersen_has_ten_vertices(self):
        self.assertEqual(
            len(petersen_vertices()),
            10,
        )

    def test_petersen_has_fifteen_edges(self):
        self.assertEqual(
            len(petersen_edges()),
            15,
        )

    def test_petersen_is_cubic(self):
        adjacency = adjacency_map(
            petersen_vertices(),
            petersen_edges(),
        )

        self.assertEqual(
            {
                len(neighbors)
                for neighbors in adjacency.values()
            },
            {
                3,
            },
        )

    def test_line_graph_has_fifteen_vertices(self):
        self.assertEqual(
            len(petersen_line_graph_vertices()),
            15,
        )

    def test_line_graph_has_thirty_edges(self):
        self.assertEqual(
            len(petersen_line_graph_edges()),
            30,
        )

    def test_line_graph_is_quartic(self):
        adjacency = adjacency_map(
            petersen_line_graph_vertices(),
            petersen_line_graph_edges(),
        )

        self.assertEqual(
            {
                len(neighbors)
                for neighbors in adjacency.values()
            },
            {
                4,
            },
        )

    def test_line_graph_vertices_are_petersen_edges(self):
        self.assertEqual(
            petersen_line_graph_vertices(),
            petersen_edges(),
        )

    def test_line_graph_adjacency_means_shared_endpoint(self):
        for left, right in petersen_line_graph_edges():
            self.assertTrue(
                set(left).intersection(right)
            )


if __name__ == "__main__":
    unittest.main()
