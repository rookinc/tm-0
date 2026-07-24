import unittest

from tm0.body_region import CharacterState
from tm0.body_region import body_region
from tm0.body_region import boundary_preserving_edges
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign


class TestBodyRegion(unittest.TestCase):
    def setUp(self):
        same_boundary = ("b", "c")
        moved_boundary = ("a", "b")

        self.states = {
            "s0": CharacterState(
                name="s0",
                character=(
                    (
                        canonical_edge("a", "c"),
                        LocalSign.PRESERVE,
                    ),
                ),
                boundary=same_boundary,
            ),
            "s1": CharacterState(
                name="s1",
                character=(
                    (
                        canonical_edge("a", "c"),
                        LocalSign.INVERT,
                    ),
                ),
                boundary=same_boundary,
            ),
            "s2": CharacterState(
                name="s2",
                character=(
                    (
                        canonical_edge("a", "d"),
                        LocalSign.PRESERVE,
                    ),
                ),
                boundary=same_boundary,
            ),
            "s3": CharacterState(
                name="s3",
                character=(
                    (
                        canonical_edge("a", "d"),
                        LocalSign.INVERT,
                    ),
                ),
                boundary=moved_boundary,
            ),
        }

        self.transitions = (
            ("s0", "s1"),
            ("s1", "s2"),
            ("s2", "s3"),
        )

    def test_boundary_preserving_edges_exclude_boundary_change(self):
        edges = boundary_preserving_edges(
            self.states,
            self.transitions,
        )

        self.assertEqual(
            edges,
            (
                ("s0", "s1"),
                ("s1", "s2"),
            ),
        )

    def test_body_region_contains_connected_same_boundary_states(self):
        region = body_region(
            self.states,
            self.transitions,
            "s0",
        )

        self.assertEqual(
            region.members,
            ("s0", "s1", "s2"),
        )

    def test_boundary_change_is_outside_body_region(self):
        region = body_region(
            self.states,
            self.transitions,
            "s0",
        )

        self.assertNotIn("s3", region.members)

    def test_region_boundary_matches_seed_boundary(self):
        region = body_region(
            self.states,
            self.transitions,
            "s0",
        )

        self.assertEqual(
            region.boundary,
            ("b", "c"),
        )

    def test_different_seed_can_define_different_region(self):
        region = body_region(
            self.states,
            self.transitions,
            "s3",
        )

        self.assertEqual(
            region.members,
            ("s3",),
        )

    def test_unknown_seed_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "seed state must exist",
        ):
            body_region(
                self.states,
                self.transitions,
                "missing",
            )


if __name__ == "__main__":
    unittest.main()
