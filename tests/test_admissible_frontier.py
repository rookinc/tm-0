import unittest

from tm0.admissible_frontier import partition_frontier
from tm0.admissible_frontier import partition_is_complete
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.possibility_frontier import possibility_frontier


class TestAdmissibleFrontier(unittest.TestCase):
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

        self.frontier = possibility_frontier(
            self.edges,
            self.signs,
            "a",
        )

    def test_no_previous_address_blocks_nothing(self):
        partition = partition_frontier(
            self.frontier,
            None,
        )

        self.assertEqual(
            partition.admissible,
            self.frontier,
        )

        self.assertEqual(
            partition.structured_absence,
            (),
        )

    def test_previous_address_is_structured_absence(self):
        blocked = canonical_edge("a", "b")

        partition = partition_frontier(
            self.frontier,
            blocked,
        )

        self.assertEqual(
            len(partition.structured_absence),
            1,
        )

        self.assertEqual(
            partition.structured_absence[0].address,
            blocked,
        )

    def test_blocked_address_remains_in_possibility(self):
        blocked = canonical_edge("a", "b")

        partition = partition_frontier(
            self.frontier,
            blocked,
        )

        all_addresses = {
            possibility.address
            for possibility in self.frontier
        }

        absent_addresses = {
            possibility.address
            for possibility in partition.structured_absence
        }

        self.assertTrue(
            absent_addresses.issubset(all_addresses)
        )

    def test_admissible_and_absent_are_disjoint(self):
        blocked = canonical_edge("a", "b")

        partition = partition_frontier(
            self.frontier,
            blocked,
        )

        admissible = set(partition.admissible)
        absent = set(partition.structured_absence)

        self.assertFalse(admissible & absent)

    def test_partition_is_complete(self):
        blocked = canonical_edge("a", "b")

        partition = partition_frontier(
            self.frontier,
            blocked,
        )

        self.assertTrue(
            partition_is_complete(
                self.frontier,
                partition,
            )
        )

    def test_one_address_is_excluded(self):
        blocked = canonical_edge("a", "b")

        partition = partition_frontier(
            self.frontier,
            blocked,
        )

        self.assertEqual(
            len(partition.admissible),
            len(self.frontier) - 1,
        )


if __name__ == "__main__":
    unittest.main()
