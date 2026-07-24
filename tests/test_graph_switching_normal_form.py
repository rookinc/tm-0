import unittest

from tm0.graph_switching_normal_form import canonical_edge
from tm0.graph_switching_normal_form import normalize_signed_graph
from tm0.local_sign_product import LocalSign


class TestGraphSwitchingNormalForm(unittest.TestCase):
    def test_tree_edges_normalize_to_preserve(self):
        edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "d"),
        )

        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.INVERT,
        }

        result = normalize_signed_graph(edges, signs, root="a")

        for edge in result.tree_edges:
            self.assertEqual(
                result.normalized_signs[edge],
                LocalSign.PRESERVE,
            )

    def test_one_cycle_leaves_one_chord_sign(self):
        edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "a"),
        )

        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
        }

        result = normalize_signed_graph(edges, signs, root="a")

        self.assertEqual(len(result.tree_edges), 2)
        self.assertEqual(len(result.chord_edges), 1)

        chord = result.chord_edges[0]

        self.assertEqual(
            result.normalized_signs[chord],
            LocalSign.INVERT,
        )

    def test_two_independent_cycles_leave_two_chord_signs(self):
        edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "a"),
            ("c", "d"),
            ("d", "a"),
        )

        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.INVERT,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        result = normalize_signed_graph(edges, signs, root="a")

        self.assertEqual(len(result.tree_edges), 3)
        self.assertEqual(len(result.chord_edges), 2)

    def test_cycle_rank_matches_chord_count(self):
        edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "a"),
            ("c", "d"),
            ("d", "a"),
        )

        signs = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        result = normalize_signed_graph(edges, signs, root="a")

        vertex_count = 4
        edge_count = 5
        cycle_rank = edge_count - vertex_count + 1

        self.assertEqual(
            len(result.chord_edges),
            cycle_rank,
        )

    def test_disconnected_graph_is_rejected(self):
        edges = (
            ("a", "b"),
            ("c", "d"),
        )

        signs = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
        }

        with self.assertRaisesRegex(
            ValueError,
            "graph must be connected",
        ):
            normalize_signed_graph(edges, signs, root="a")

    def test_missing_sign_is_rejected(self):
        edges = (
            ("a", "b"),
            ("b", "c"),
        )

        signs = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
        }

        with self.assertRaisesRegex(
            ValueError,
            "one sign is required per edge",
        ):
            normalize_signed_graph(edges, signs, root="a")


if __name__ == "__main__":
    unittest.main()
