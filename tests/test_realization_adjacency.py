import unittest

from tm0.graph_switching_classification import graph_switching_signature
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.realization_adjacency import compare_adjacency_notions
from tm0.realization_adjacency import reachable_character_states


class TestRealizationAdjacency(unittest.TestCase):
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

    def test_one_reachable_state_per_edge_address(self):
        reachable = reachable_character_states(
            self.edges,
            self.signs,
            "a",
        )

        self.assertEqual(len(reachable), len(self.edges))

    def test_chord_flip_is_character_and_realization_adjacent(self):
        reachable = reachable_character_states(
            self.edges,
            self.signs,
            "a",
        )

        target = reachable[canonical_edge("b", "c")]

        character_adjacent, realization_adjacent = (
            compare_adjacency_notions(
                self.edges,
                self.signs,
                "a",
                target,
            )
        )

        self.assertTrue(character_adjacent)
        self.assertTrue(realization_adjacent)

    def test_tree_edge_flip_can_be_reachable_without_one_bit_distance(self):
        reachable = reachable_character_states(
            self.edges,
            self.signs,
            "a",
        )

        target = reachable[canonical_edge("a", "c")]

        character_adjacent, realization_adjacent = (
            compare_adjacency_notions(
                self.edges,
                self.signs,
                "a",
                target,
            )
        )

        self.assertFalse(character_adjacent)
        self.assertTrue(realization_adjacent)

    def test_current_state_is_not_realization_adjacent_to_itself(self):
        current = graph_switching_signature(
            self.edges,
            self.signs,
            "a",
        )

        character_adjacent, realization_adjacent = (
            compare_adjacency_notions(
                self.edges,
                self.signs,
                "a",
                current,
            )
        )

        self.assertFalse(character_adjacent)
        self.assertFalse(realization_adjacent)


if __name__ == "__main__":
    unittest.main()
