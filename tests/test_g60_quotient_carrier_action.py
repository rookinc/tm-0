import unittest

from tm0.g60_quotient_carrier_action import (
    CERTIFIED_CARRIER_ACTIONS,
    TAU0,
    TAU1,
    TAU2,
)
from tm0.g60_three_quotient_systems import (
    G60_QUOTIENT_CARRIER,
    G60_QUOTIENT_SYSTEMS,
)
from tm0.selected_equivalence import canonical_partition


class TestG60QuotientCarrierAction(unittest.TestCase):
    def setUp(self):
        carrier = frozenset(G60_QUOTIENT_CARRIER)

        self.partitions = tuple(
            canonical_partition(
                carrier,
                system.partition,
            )
            for system in G60_QUOTIENT_SYSTEMS
        )

    def test_three_certified_actions_are_registered(self):
        self.assertEqual(
            tuple(
                action.name
                for action in CERTIFIED_CARRIER_ACTIONS
            ),
            (
                "tau0",
                "tau1",
                "tau2",
            ),
        )

    def test_each_carrier_action_is_an_involution(self):
        for action in CERTIFIED_CARRIER_ACTIONS:
            for vertex in G60_QUOTIENT_CARRIER:
                image = action.image_vertex(vertex)
                returned = action.image_vertex(image)

                self.assertEqual(
                    returned,
                    vertex,
                )

    def test_tau0_induces_certified_family_action(self):
        images = tuple(
            TAU0.image_partition(partition)
            for partition in self.partitions
        )

        expected = tuple(
            self.partitions[index]
            for index in TAU0.family_permutation
        )

        self.assertEqual(
            images,
            expected,
        )

    def test_tau1_induces_certified_family_action(self):
        images = tuple(
            TAU1.image_partition(partition)
            for partition in self.partitions
        )

        expected = tuple(
            self.partitions[index]
            for index in TAU1.family_permutation
        )

        self.assertEqual(
            images,
            expected,
        )

    def test_tau2_induces_certified_family_action(self):
        images = tuple(
            TAU2.image_partition(partition)
            for partition in self.partitions
        )

        expected = tuple(
            self.partitions[index]
            for index in TAU2.family_permutation
        )

        self.assertEqual(
            images,
            expected,
        )

    def test_each_action_fixes_its_certified_partition(self):
        fixed_indices = (
            0,
            1,
            2,
        )

        for action, fixed_index in zip(
            CERTIFIED_CARRIER_ACTIONS,
            fixed_indices,
        ):
            self.assertEqual(
                action.image_partition(
                    self.partitions[fixed_index]
                ),
                self.partitions[fixed_index],
            )

    def test_each_action_swaps_other_two_partitions(self):
        for action in CERTIFIED_CARRIER_ACTIONS:
            fixed = {
                index
                for index, target in enumerate(
                    action.family_permutation
                )
                if index == target
            }

            moved = tuple(
                index
                for index in range(3)
                if index not in fixed
            )

            self.assertEqual(
                len(fixed),
                1,
            )
            self.assertEqual(
                len(moved),
                2,
            )
            self.assertEqual(
                action.family_permutation[moved[0]],
                moved[1],
            )
            self.assertEqual(
                action.family_permutation[moved[1]],
                moved[0],
            )

    def test_carrier_vertex_set_is_preserved(self):
        expected = set(G60_QUOTIENT_CARRIER)

        for action in CERTIFIED_CARRIER_ACTIONS:
            image = {
                action.image_vertex(vertex)
                for vertex in G60_QUOTIENT_CARRIER
            }

            self.assertEqual(
                image,
                expected,
            )

    def test_unknown_vertex_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "vertex is not in the certified carrier",
        ):
            TAU0.image_vertex("30")


if __name__ == "__main__":
    unittest.main()
