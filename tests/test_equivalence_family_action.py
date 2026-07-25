import unittest

from tm0.equivalence_family_action import (
    EquivalenceFamilyAction,
    act_on_selection,
)
from tm0.g60_three_quotient_systems import (
    select_g60_quotient_system,
)


class TestEquivalenceFamilyAction(unittest.TestCase):
    def setUp(self):
        self.names = (
            "P0",
            "P1",
            "P2",
        )

        self.actions = (
            (0, 1, 2),
            (0, 2, 1),
            (1, 0, 2),
            (1, 2, 0),
            (2, 0, 1),
            (2, 1, 0),
        )

    def test_all_six_certified_actions_are_valid(self):
        realized = tuple(
            EquivalenceFamilyAction(
                names=self.names,
                permutation=permutation,
            )
            for permutation in self.actions
        )

        self.assertEqual(
            len(realized),
            6,
        )

    def test_actions_are_distinct(self):
        realized = {
            EquivalenceFamilyAction(
                names=self.names,
                permutation=permutation,
            )
            for permutation in self.actions
        }

        self.assertEqual(
            len(realized),
            6,
        )

    def test_action_image_has_order_six(self):
        images = {
            action.permutation
            for action in (
                EquivalenceFamilyAction(
                    names=self.names,
                    permutation=permutation,
                )
                for permutation in self.actions
            )
        }

        self.assertEqual(
            len(images),
            6,
        )

    def test_action_is_transitive(self):
        images_of_p0 = {
            EquivalenceFamilyAction(
                names=self.names,
                permutation=permutation,
            ).image_name("P0")
            for permutation in self.actions
        }

        self.assertEqual(
            images_of_p0,
            {
                "P0",
                "P1",
                "P2",
            },
        )

    def test_each_involution_fixes_one_system(self):
        involutions = (
            (0, 2, 1),
            (2, 1, 0),
            (1, 0, 2),
        )

        fixed_sets = tuple(
            EquivalenceFamilyAction(
                names=self.names,
                permutation=permutation,
            ).fixed_names()
            for permutation in involutions
        )

        self.assertEqual(
            fixed_sets,
            (
                ("P0",),
                ("P1",),
                ("P2",),
            ),
        )

    def test_each_involution_swaps_other_two_systems(self):
        action = EquivalenceFamilyAction(
            names=self.names,
            permutation=(0, 2, 1),
        )

        self.assertEqual(
            action.image_name("P1"),
            "P2",
        )
        self.assertEqual(
            action.image_name("P2"),
            "P1",
        )

    def test_action_moves_selected_system(self):
        selection = select_g60_quotient_system("P0")

        action = EquivalenceFamilyAction(
            names=self.names,
            permutation=(1, 2, 0),
        )

        moved = act_on_selection(
            selection,
            action,
        )

        self.assertEqual(
            moved.selected_name,
            "P1",
        )

    def test_action_preserves_carrier(self):
        selection = select_g60_quotient_system("P0")

        action = EquivalenceFamilyAction(
            names=self.names,
            permutation=(1, 2, 0),
        )

        moved = act_on_selection(
            selection,
            action,
        )

        self.assertEqual(
            moved.carrier,
            selection.carrier,
        )

    def test_action_preserves_registered_family(self):
        selection = select_g60_quotient_system("P0")

        action = EquivalenceFamilyAction(
            names=self.names,
            permutation=(1, 2, 0),
        )

        moved = act_on_selection(
            selection,
            action,
        )

        self.assertEqual(
            moved.systems,
            selection.systems,
        )

    def test_identity_preserves_selected_system(self):
        selection = select_g60_quotient_system("P2")

        identity = EquivalenceFamilyAction(
            names=self.names,
            permutation=(0, 1, 2),
        )

        moved = act_on_selection(
            selection,
            identity,
        )

        self.assertEqual(
            moved.selected_name,
            "P2",
        )

    def test_invalid_permutation_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "family action must be a permutation",
        ):
            EquivalenceFamilyAction(
                names=self.names,
                permutation=(0, 0, 2),
            )

    def test_action_domain_must_match_registered_systems(self):
        selection = select_g60_quotient_system("P0")

        action = EquivalenceFamilyAction(
            names=(
                "P0",
                "P1",
                "PX",
            ),
            permutation=(0, 1, 2),
        )

        with self.assertRaisesRegex(
            ValueError,
            "action domain must match registered systems",
        ):
            act_on_selection(
                selection,
                action,
            )


if __name__ == "__main__":
    unittest.main()
