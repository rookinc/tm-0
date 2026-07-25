import unittest

from tm0.g60_three_quotient_systems import (
    G60_QUOTIENT_CARRIER,
    G60_QUOTIENT_SYSTEMS,
    P0_BLOCKS,
    P1_BLOCKS,
    P2_BLOCKS,
    select_g60_quotient_system,
)


class TestG60ThreeQuotientSystems(unittest.TestCase):
    def test_carrier_has_thirty_vertices(self):
        self.assertEqual(
            len(G60_QUOTIENT_CARRIER),
            30,
        )
        self.assertEqual(
            len(set(G60_QUOTIENT_CARRIER)),
            30,
        )

    def test_three_systems_are_registered(self):
        self.assertEqual(
            tuple(
                system.name
                for system in G60_QUOTIENT_SYSTEMS
            ),
            (
                "P0",
                "P1",
                "P2",
            ),
        )

    def test_each_system_has_fifteen_pairs(self):
        for system in G60_QUOTIENT_SYSTEMS:
            self.assertEqual(
                len(system.partition),
                15,
            )
            self.assertTrue(
                all(
                    len(block) == 2
                    for block in system.partition
                )
            )

    def test_each_system_partitions_the_same_carrier(self):
        expected = set(G60_QUOTIENT_CARRIER)

        for system in G60_QUOTIENT_SYSTEMS:
            flattened = {
                vertex
                for block in system.partition
                for vertex in block
            }

            self.assertEqual(
                flattened,
                expected,
            )

    def test_pair_sets_are_pairwise_disjoint(self):
        p0 = set(P0_BLOCKS)
        p1 = set(P1_BLOCKS)
        p2 = set(P2_BLOCKS)

        self.assertEqual(
            p0 & p1,
            set(),
        )
        self.assertEqual(
            p0 & p2,
            set(),
        )
        self.assertEqual(
            p1 & p2,
            set(),
        )

    def test_union_contains_forty_five_pairs(self):
        all_pairs = (
            set(P0_BLOCKS)
            | set(P1_BLOCKS)
            | set(P2_BLOCKS)
        )

        self.assertEqual(
            len(all_pairs),
            45,
        )

    def test_each_system_can_be_selected(self):
        for selected_name in ("P0", "P1", "P2"):
            selection = select_g60_quotient_system(
                selected_name
            )

            self.assertEqual(
                selection.selected_name,
                selected_name,
            )
            self.assertEqual(
                selection.carrier,
                frozenset(G60_QUOTIENT_CARRIER),
            )
            self.assertEqual(
                len(selection.alternatives),
                2,
            )

    def test_different_selections_preserve_same_carrier(self):
        p0 = select_g60_quotient_system("P0")
        p1 = select_g60_quotient_system("P1")
        p2 = select_g60_quotient_system("P2")

        self.assertEqual(
            p0.carrier,
            p1.carrier,
        )
        self.assertEqual(
            p1.carrier,
            p2.carrier,
        )

        self.assertNotEqual(
            p0.classes(),
            p1.classes(),
        )
        self.assertNotEqual(
            p1.classes(),
            p2.classes(),
        )
        self.assertNotEqual(
            p0.classes(),
            p2.classes(),
        )

    def test_equal_pair_size_profiles_do_not_erase_selection(self):
        selections = tuple(
            select_g60_quotient_system(name)
            for name in ("P0", "P1", "P2")
        )

        profiles = tuple(
            tuple(
                len(block)
                for block in selection.classes()
            )
            for selection in selections
        )

        self.assertEqual(
            profiles,
            (
                (2,) * 15,
                (2,) * 15,
                (2,) * 15,
            ),
        )

        self.assertEqual(
            {
                selection.selected_name
                for selection in selections
            },
            {
                "P0",
                "P1",
                "P2",
            },
        )

    def test_unknown_system_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "selected equivalence system is not registered",
        ):
            select_g60_quotient_system("P3")


if __name__ == "__main__":
    unittest.main()
