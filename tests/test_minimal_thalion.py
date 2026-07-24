import unittest

from tm0.body_region import CharacterState
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.minimal_thalion import candidate_from_seed
from tm0.minimal_thalion import minimal_thalion_candidate


class TestMinimalThalion(unittest.TestCase):
    def setUp(self):
        boundary = ("b", "c")

        self.states = {
            "s0": CharacterState(
                name="s0",
                character=(
                    (
                        canonical_edge("a", "c"),
                        LocalSign.PRESERVE,
                    ),
                ),
                boundary=boundary,
            ),
            "s1": CharacterState(
                name="s1",
                character=(
                    (
                        canonical_edge("a", "c"),
                        LocalSign.INVERT,
                    ),
                ),
                boundary=boundary,
            ),
            "s2": CharacterState(
                name="s2",
                character=(
                    (
                        canonical_edge("a", "d"),
                        LocalSign.PRESERVE,
                    ),
                ),
                boundary=("a", "b"),
            ),
        }

    def test_single_state_is_not_a_candidate(self):
        candidate = candidate_from_seed(
            self.states,
            (),
            "s0",
        )

        self.assertIsNone(candidate)

    def test_two_states_with_same_boundary_and_different_character_qualify(self):
        candidate = candidate_from_seed(
            self.states,
            (("s0", "s1"),),
            "s0",
        )

        self.assertIsNotNone(candidate)
        self.assertEqual(
            candidate.members,
            ("s0", "s1"),
        )
        self.assertEqual(
            candidate.character_count,
            2,
        )

    def test_boundary_change_does_not_join_candidate(self):
        candidate = candidate_from_seed(
            self.states,
            (
                ("s0", "s1"),
                ("s1", "s2"),
            ),
            "s0",
        )

        self.assertIsNotNone(candidate)
        self.assertEqual(
            candidate.members,
            ("s0", "s1"),
        )

    def test_same_character_does_not_qualify(self):
        same_states = {
            "x0": self.states["s0"],
            "x1": CharacterState(
                name="x1",
                character=self.states["s0"].character,
                boundary=self.states["s0"].boundary,
            ),
        }

        candidate = candidate_from_seed(
            same_states,
            (("x0", "x1"),),
            "x0",
        )

        self.assertIsNone(candidate)

    def test_minimal_candidate_has_two_states(self):
        candidate = minimal_thalion_candidate(
            self.states,
            (
                ("s0", "s1"),
                ("s1", "s2"),
            ),
        )

        self.assertIsNotNone(candidate)
        self.assertEqual(
            len(candidate.members),
            2,
        )

    def test_no_candidate_returns_none(self):
        candidate = minimal_thalion_candidate(
            {"s0": self.states["s0"]},
            (),
        )

        self.assertIsNone(candidate)


if __name__ == "__main__":
    unittest.main()
