import unittest

from tm0.body_region import CharacterState
from tm0.graph_switching_normal_form import canonical_edge
from tm0.local_sign_product import LocalSign
from tm0.minimal_returning_body import minimal_returning_body_size
from tm0.minimal_returning_body import shortest_return_cycle


class TestMinimalReturningBody(unittest.TestCase):
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
                boundary=boundary,
            ),
            "s3": CharacterState(
                name="s3",
                character=(
                    (
                        canonical_edge("a", "d"),
                        LocalSign.INVERT,
                    ),
                ),
                boundary=("a", "b"),
            ),
        }

    def test_one_state_has_no_nonidentity_return(self):
        cycle = shortest_return_cycle(
            {"s0": self.states["s0"]},
            (),
            "s0",
        )

        self.assertIsNone(cycle)

    def test_two_states_can_support_return(self):
        cycle = shortest_return_cycle(
            self.states,
            (
                ("s0", "s1"),
                ("s1", "s0"),
            ),
            "s0",
        )

        self.assertIsNotNone(cycle)
        self.assertEqual(
            cycle.path,
            ("s0", "s1", "s0"),
        )

    def test_two_state_return_preserves_boundary(self):
        cycle = shortest_return_cycle(
            self.states,
            (
                ("s0", "s1"),
                ("s1", "s0"),
            ),
            "s0",
        )

        self.assertEqual(
            cycle.boundary,
            ("b", "c"),
        )

    def test_boundary_change_cannot_complete_same_body_return(self):
        cycle = shortest_return_cycle(
            self.states,
            (
                ("s0", "s3"),
                ("s3", "s0"),
            ),
            "s0",
        )

        self.assertIsNone(cycle)

    def test_three_state_cycle_returns(self):
        cycle = shortest_return_cycle(
            self.states,
            (
                ("s0", "s1"),
                ("s1", "s2"),
                ("s2", "s0"),
            ),
            "s0",
        )

        self.assertIsNotNone(cycle)
        self.assertEqual(
            cycle.path,
            ("s0", "s1", "s2", "s0"),
        )

    def test_minimal_returning_body_size_is_two(self):
        size = minimal_returning_body_size(
            self.states,
            (
                ("s0", "s1"),
                ("s1", "s0"),
                ("s1", "s2"),
                ("s2", "s0"),
            ),
        )

        self.assertEqual(size, 2)

    def test_unknown_seed_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "seed state must exist",
        ):
            shortest_return_cycle(
                self.states,
                (),
                "missing",
            )


if __name__ == "__main__":
    unittest.main()
