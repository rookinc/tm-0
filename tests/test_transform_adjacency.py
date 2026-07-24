import unittest

from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.transform_adjacency import differing_bits
from tm0.transform_adjacency import minimally_transformable


class TestTransformAdjacency(unittest.TestCase):
    def setUp(self):
        self.first = (
            (
                canonical_edge("a", "c"),
                LocalSign.PRESERVE,
            ),
            (
                canonical_edge("a", "d"),
                LocalSign.PRESERVE,
            ),
        )

    def test_identical_character_is_not_adjacent(self):
        self.assertFalse(
            minimally_transformable(
                self.first,
                self.first,
            )
        )

    def test_one_bit_difference_is_adjacent(self):
        second = (
            (
                canonical_edge("a", "c"),
                LocalSign.INVERT,
            ),
            (
                canonical_edge("a", "d"),
                LocalSign.PRESERVE,
            ),
        )

        self.assertTrue(
            minimally_transformable(
                self.first,
                second,
            )
        )

        self.assertEqual(
            differing_bits(
                self.first,
                second,
            ),
            (
                canonical_edge("a", "c"),
            ),
        )

    def test_two_bit_difference_is_not_minimal(self):
        second = (
            (
                canonical_edge("a", "c"),
                LocalSign.INVERT,
            ),
            (
                canonical_edge("a", "d"),
                LocalSign.INVERT,
            ),
        )

        self.assertFalse(
            minimally_transformable(
                self.first,
                second,
            )
        )

        self.assertEqual(
            len(
                differing_bits(
                    self.first,
                    second,
                )
            ),
            2,
        )

    def test_address_mismatch_is_rejected(self):
        second = (
            (
                canonical_edge("a", "c"),
                LocalSign.PRESERVE,
            ),
            (
                canonical_edge("b", "d"),
                LocalSign.PRESERVE,
            ),
        )

        with self.assertRaisesRegex(
            ValueError,
            "character signatures must use the same addresses",
        ):
            differing_bits(
                self.first,
                second,
            )


if __name__ == "__main__":
    unittest.main()
