import unittest

from tm0.finite_graph_isomorphism import (
    adjacency_map,
    find_graph_isomorphism,
    graphs_are_isomorphic,
)


class TestFiniteGraphIsomorphism(unittest.TestCase):
    def test_adjacency_map_is_undirected(self):
        adjacency = adjacency_map(
            vertices=("a", "b", "c"),
            edges=(
                ("a", "b"),
                ("b", "c"),
            ),
        )

        self.assertEqual(
            adjacency,
            {
                "a": frozenset(("b",)),
                "b": frozenset(("a", "c")),
                "c": frozenset(("b",)),
            },
        )

    def test_relabelled_paths_are_isomorphic(self):
        mapping = find_graph_isomorphism(
            left_vertices=(0, 1, 2, 3),
            left_edges=(
                (0, 1),
                (1, 2),
                (2, 3),
            ),
            right_vertices=("a", "b", "c", "d"),
            right_edges=(
                ("a", "c"),
                ("c", "d"),
                ("d", "b"),
            ),
        )

        self.assertIsNotNone(mapping)
        self.assertEqual(
            set(mapping),
            {
                0,
                1,
                2,
                3,
            },
        )
        self.assertEqual(
            set(mapping.values()),
            {
                "a",
                "b",
                "c",
                "d",
            },
        )

    def test_cycle_and_path_are_not_isomorphic(self):
        self.assertFalse(
            graphs_are_isomorphic(
                left_vertices=(0, 1, 2, 3),
                left_edges=(
                    (0, 1),
                    (1, 2),
                    (2, 3),
                    (3, 0),
                ),
                right_vertices=("a", "b", "c", "d"),
                right_edges=(
                    ("a", "b"),
                    ("b", "c"),
                    ("c", "d"),
                ),
            )
        )

    def test_triangles_with_different_labels_are_isomorphic(self):
        self.assertTrue(
            graphs_are_isomorphic(
                left_vertices=(0, 1, 2),
                left_edges=(
                    (0, 1),
                    (1, 2),
                    (2, 0),
                ),
                right_vertices=("x", "y", "z"),
                right_edges=(
                    ("x", "z"),
                    ("z", "y"),
                    ("y", "x"),
                ),
            )
        )

    def test_different_vertex_counts_are_not_isomorphic(self):
        self.assertFalse(
            graphs_are_isomorphic(
                left_vertices=(0, 1),
                left_edges=((0, 1),),
                right_vertices=("a", "b", "c"),
                right_edges=(
                    ("a", "b"),
                    ("b", "c"),
                ),
            )
        )

    def test_different_edge_counts_are_not_isomorphic(self):
        self.assertFalse(
            graphs_are_isomorphic(
                left_vertices=(0, 1, 2),
                left_edges=(
                    (0, 1),
                    (1, 2),
                ),
                right_vertices=("a", "b", "c"),
                right_edges=(
                    ("a", "b"),
                    ("b", "c"),
                    ("c", "a"),
                ),
            )
        )

    def test_loop_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "must not contain loops",
        ):
            adjacency_map(
                vertices=(0, 1),
                edges=((0, 0),),
            )

    def test_unregistered_vertex_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "unregistered vertex",
        ):
            adjacency_map(
                vertices=(0, 1),
                edges=((0, 2),),
            )


if __name__ == "__main__":
    unittest.main()
