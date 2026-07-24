import unittest

from tm0.character_constraint import character_admits
from tm0.character_constraint import partition_by_character
from tm0.character_constraint import partition_is_complete
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.possibility_frontier import possibility_frontier


class TestCharacterConstraint(unittest.TestCase):
    def setUp(self):
        self.edges = (
            ("a", "b"),
            ("b", "c"),
            ("c", "a"),
            ("c", "d"),
            ("d", "a"),
        )

    def frontier_from(self, signs):
        return possibility_frontier(
            self.edges,
            signs,
            "a",
        )

    def test_all_preserve_character_admits_every_flip(self):
        signs = {
            canonical_edge("a", "b"): LocalSign.PRESERVE,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        frontier = self.frontier_from(signs)
        partition = partition_by_character(frontier)

        self.assertEqual(
            partition.admissible,
            frontier,
        )

        self.assertEqual(
            partition.structured_absence,
            (),
        )

    def test_character_can_exclude_polar_reduction(self):
        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        frontier = self.frontier_from(signs)
        partition = partition_by_character(frontier)

        self.assertGreater(
            len(partition.structured_absence),
            0,
        )

    def test_absent_candidates_remain_addressable(self):
        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        frontier = self.frontier_from(signs)
        partition = partition_by_character(frontier)

        frontier_addresses = {
            possibility.address
            for possibility in frontier
        }

        absent_addresses = {
            possibility.address
            for possibility in partition.structured_absence
        }

        self.assertTrue(
            absent_addresses.issubset(frontier_addresses)
        )

    def test_partition_is_complete(self):
        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        frontier = self.frontier_from(signs)
        partition = partition_by_character(frontier)

        self.assertTrue(
            partition_is_complete(
                frontier,
                partition,
            )
        )

    def test_admissibility_is_computed_from_character(self):
        signs = {
            canonical_edge("a", "b"): LocalSign.INVERT,
            canonical_edge("b", "c"): LocalSign.PRESERVE,
            canonical_edge("c", "a"): LocalSign.PRESERVE,
            canonical_edge("c", "d"): LocalSign.PRESERVE,
            canonical_edge("d", "a"): LocalSign.PRESERVE,
        }

        frontier = self.frontier_from(signs)

        outcomes = {
            possibility.address: character_admits(possibility)
            for possibility in frontier
        }

        self.assertIn(True, outcomes.values())
        self.assertIn(False, outcomes.values())


if __name__ == "__main__":
    unittest.main()
