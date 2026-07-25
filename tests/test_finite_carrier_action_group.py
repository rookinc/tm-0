import unittest

from tm0.finite_carrier_action_group import (
    CarrierFamilyAction,
    compose_permutations,
    finite_carrier_action_group,
    inverse_permutation,
)


class TestFiniteCarrierActionGroup(unittest.TestCase):
    def setUp(self):
        self.identity = CarrierFamilyAction(
            name="e",
            carrier_permutation=(0, 1, 2),
            family_permutation=(0, 1, 2),
        )

        self.swap_01 = CarrierFamilyAction(
            name="s01",
            carrier_permutation=(1, 0, 2),
            family_permutation=(1, 0, 2),
        )

        self.swap_12 = CarrierFamilyAction(
            name="s12",
            carrier_permutation=(0, 2, 1),
            family_permutation=(0, 2, 1),
        )

        self.cycle_012 = CarrierFamilyAction(
            name="c012",
            carrier_permutation=(1, 2, 0),
            family_permutation=(1, 2, 0),
        )

        self.cycle_021 = CarrierFamilyAction(
            name="c021",
            carrier_permutation=(2, 0, 1),
            family_permutation=(2, 0, 1),
        )

        self.swap_02 = CarrierFamilyAction(
            name="s02",
            carrier_permutation=(2, 1, 0),
            family_permutation=(2, 1, 0),
        )

        self.group = finite_carrier_action_group(
            (
                self.identity,
                self.swap_01,
                self.swap_12,
                self.cycle_012,
                self.cycle_021,
                self.swap_02,
            )
        )

    def test_permutations_compose(self):
        result = compose_permutations(
            self.swap_01.carrier_permutation,
            self.swap_12.carrier_permutation,
        )

        self.assertEqual(
            result,
            self.cycle_012.carrier_permutation,
        )

    def test_inverse_permutation_is_derived(self):
        self.assertEqual(
            inverse_permutation(
                self.cycle_012.carrier_permutation
            ),
            self.cycle_021.carrier_permutation,
        )

    def test_group_identity_is_derived(self):
        self.assertEqual(
            self.group.identity,
            self.identity,
        )

    def test_group_composition_returns_registered_action(self):
        self.assertEqual(
            self.group.compose(
                self.swap_01,
                self.swap_12,
            ),
            self.cycle_012,
        )

    def test_group_inverse_returns_registered_action(self):
        self.assertEqual(
            self.group.inverse(self.cycle_012),
            self.cycle_021,
        )

    def test_stabilizer_of_p0_is_derived(self):
        self.assertEqual(
            {
                action.name
                for action in self.group.stabilizer(0)
            },
            {
                "e",
                "s12",
            },
        )

    def test_stabilizer_of_p1_is_derived(self):
        self.assertEqual(
            {
                action.name
                for action in self.group.stabilizer(1)
            },
            {
                "e",
                "s02",
            },
        )

    def test_stabilizer_of_p2_is_derived(self):
        self.assertEqual(
            {
                action.name
                for action in self.group.stabilizer(2)
            },
            {
                "e",
                "s01",
            },
        )

    def test_each_involution_belongs_to_one_stabilizer(self):
        memberships = {
            action.name: tuple(
                index
                for index in range(3)
                if action in self.group.stabilizer(index)
            )
            for action in (
                self.swap_01,
                self.swap_12,
                self.swap_02,
            )
        }

        self.assertEqual(
            memberships,
            {
                "s01": (2,),
                "s12": (0,),
                "s02": (1,),
            },
        )

    def test_invalid_system_index_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "system index is outside the family",
        ):
            self.group.stabilizer(3)

    def test_group_requires_identity(self):
        group = finite_carrier_action_group(
            (
                self.swap_01,
                self.swap_12,
            )
        )

        with self.assertRaisesRegex(
            ValueError,
            "exactly one identity",
        ):
            _ = group.identity


if __name__ == "__main__":
    unittest.main()
