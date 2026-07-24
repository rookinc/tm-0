import unittest

from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.possibility_frontier import outcome_classes
from tm0.possibility_frontier import possibility_frontier


class TestPossibilityFrontier(unittest.TestCase):
    def setUp(self):
        self.edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "a"),
            ("c", "d"),
            ("d", "a"),
        )

        self.signs = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

    def test_one_possible_realization_per_edge_address(self):
        frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

        self.assertEqual(len(frontier), len(self.edges))

    def test_every_possibility_preserves_before_character(self):
        frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

        before_values = {
            possibility.before
            for possibility in frontier
        }

        self.assertEqual(len(before_values), 1)

    def test_every_possibility_changes_character(self):
        frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

        for possibility in frontier:
            self.assertNotEqual(
                possibility.before,
                possibility.after,
            )

    def test_addresses_are_canonical_edges(self):
        frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

        addresses = {
            possibility.address
            for possibility in frontier
        }

        expected = {
            canonical_edge(*edge)
            for edge in self.edges
        }

        self.assertEqual(addresses, expected)

    def test_distinct_edge_addresses_can_share_one_outcome(self):
        frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

        classes = outcome_classes(frontier)

        self.assertLessEqual(
            len(classes),
            len(frontier),
        )

    def test_frontier_does_not_select_one_realization(self):
        frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

        self.assertGreater(len(frontier), 1)


if __name__ == "__main__":
    unittest.main()
