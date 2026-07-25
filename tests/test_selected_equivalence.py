import unittest

from tm0.selected_equivalence import (
    EquivalenceSystem,
    canonical_partition,
    select_equivalence,
)


class TestSelectedEquivalence(unittest.TestCase):
    def setUp(self):
        self.carrier = ("A", "B", "C", "D")

        self.system_ab_cd = EquivalenceSystem(
            name="ab_cd",
            partition=(
                ("A", "B"),
                ("C", "D"),
            ),
        )

        self.system_ac_bd = EquivalenceSystem(
            name="ac_bd",
            partition=(
                ("A", "C"),
                ("B", "D"),
            ),
        )

        self.system_ad_bc = EquivalenceSystem(
            name="ad_bc",
            partition=(
                ("A", "D"),
                ("B", "C"),
            ),
        )

    def test_partition_is_canonicalized(self):
        partition = canonical_partition(
            frozenset(self.carrier),
            (
                ("D", "C"),
                ("B", "A"),
            ),
        )

        self.assertEqual(
            partition,
            (
                ("A", "B"),
                ("C", "D"),
            ),
        )

    def test_partition_must_cover_carrier(self):
        with self.assertRaisesRegex(
            ValueError,
            "must cover the carrier",
        ):
            canonical_partition(
                frozenset(self.carrier),
                (
                    ("A", "B"),
                    ("C",),
                ),
            )

    def test_partition_classes_must_be_disjoint(self):
        with self.assertRaisesRegex(
            ValueError,
            "must be disjoint",
        ):
            canonical_partition(
                frozenset(self.carrier),
                (
                    ("A", "B"),
                    ("B", "C", "D"),
                ),
            )

    def test_at_least_two_systems_are_required(self):
        with self.assertRaisesRegex(
            ValueError,
            "at least two equivalence systems",
        ):
            select_equivalence(
                self.carrier,
                (self.system_ab_cd,),
                "ab_cd",
            )

    def test_systems_must_be_distinct(self):
        duplicate = EquivalenceSystem(
            name="duplicate",
            partition=(
                ("A", "B"),
                ("C", "D"),
            ),
        )

        with self.assertRaisesRegex(
            ValueError,
            "equivalence systems must be distinct",
        ):
            select_equivalence(
                self.carrier,
                (
                    self.system_ab_cd,
                    duplicate,
                ),
                "ab_cd",
            )

    def test_selected_system_must_be_registered(self):
        with self.assertRaisesRegex(
            ValueError,
            "selected equivalence system is not registered",
        ):
            select_equivalence(
                self.carrier,
                (
                    self.system_ab_cd,
                    self.system_ac_bd,
                ),
                "missing",
            )

    def test_selection_preserves_fixed_carrier(self):
        selection = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
            ),
            "ab_cd",
        )

        self.assertEqual(
            selection.carrier,
            frozenset(self.carrier),
        )

    def test_selection_preserves_alternatives(self):
        selection = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
                self.system_ad_bc,
            ),
            "ac_bd",
        )

        self.assertEqual(
            tuple(
                system.name
                for system in selection.alternatives
            ),
            (
                "ab_cd",
                "ad_bc",
            ),
        )

    def test_selected_classes_are_derived(self):
        selection = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
            ),
            "ac_bd",
        )

        self.assertEqual(
            selection.classes(),
            (
                ("A", "C"),
                ("B", "D"),
            ),
        )

    def test_different_selections_leave_carrier_unchanged(self):
        first = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
            ),
            "ab_cd",
        )

        second = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
            ),
            "ac_bd",
        )

        self.assertEqual(
            first.carrier,
            second.carrier,
        )
        self.assertNotEqual(
            first.classes(),
            second.classes(),
        )

    def test_matching_class_sizes_do_not_erase_selection(self):
        first = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
            ),
            "ab_cd",
        )

        second = select_equivalence(
            self.carrier,
            (
                self.system_ab_cd,
                self.system_ac_bd,
            ),
            "ac_bd",
        )

        first_sizes = tuple(
            len(equivalence_class)
            for equivalence_class in first.classes()
        )
        second_sizes = tuple(
            len(equivalence_class)
            for equivalence_class in second.classes()
        )

        self.assertEqual(
            first_sizes,
            second_sizes,
        )
        self.assertNotEqual(
            first.selected_name,
            second.selected_name,
        )


if __name__ == "__main__":
    unittest.main()
