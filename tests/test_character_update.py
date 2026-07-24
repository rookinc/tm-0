import unittest

from tm0.character_update import realize_edge_flip
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign


class TestCharacterUpdate(unittest.TestCase):
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

    def test_chord_flip_changes_one_character_bit(self):
        result = realize_edge_flip(
            self.edges,
            self.signs,
            "a",
            canonical_edge("b", "c"),
        )

        self.assertEqual(len(result.changed_bits), 1)

    def test_tree_edge_flip_can_change_multiple_bits(self):
        result = realize_edge_flip(
            self.edges,
            self.signs,
            "a",
            canonical_edge("a", "c"),
        )

        self.assertGreaterEqual(len(result.changed_bits), 1)

    def test_incidence_structure_is_not_changed(self):
        result = realize_edge_flip(
            self.edges,
            self.signs,
            "a",
            canonical_edge("b", "c"),
        )

        self.assertEqual(
            tuple(edge for edge, _ in result.before),
            tuple(edge for edge, _ in result.after),
        )

    def test_character_changes_after_edge_flip(self):
        result = realize_edge_flip(
            self.edges,
            self.signs,
            "a",
            canonical_edge("b", "c"),
        )

        self.assertNotEqual(result.before, result.after)

    def test_unknown_edge_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "flipped edge must belong to the signed graph",
        ):
            realize_edge_flip(
                self.edges,
                self.signs,
                "a",
                ("x", "y"),
            )


if __name__ == "__main__":
    unittest.main()
