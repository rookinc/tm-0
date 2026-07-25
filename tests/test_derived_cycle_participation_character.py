import unittest

from tm0.derived_boundary_contact import MotionRule
from tm0.derived_cycle_participation_character import (
    derive_cycle_participation_character_field,
)
from tm0.derived_cycle_participation_character import (
    enumerate_simple_directed_cycles,
)
from tm0.derived_cycle_participation_character import (
    normalize_directed_cycle,
)
from tm0.derived_cycle_participation_character import (
    states_without_cycle_participation,
)
from tm0.derived_region_boundary import MotionGraph


class TestDerivedCycleParticipationCharacter(unittest.TestCase):
    def setUp(self):
        self.graph = MotionGraph(
            states=("A", "B", "C", "D", "E"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="ab",
                ),
                MotionRule(
                    source_state="B",
                    target_state="A",
                    relation_name="ba",
                ),
                MotionRule(
                    source_state="B",
                    target_state="C",
                    relation_name="bc",
                ),
                MotionRule(
                    source_state="C",
                    target_state="D",
                    relation_name="cd",
                ),
                MotionRule(
                    source_state="D",
                    target_state="B",
                    relation_name="db",
                ),
                MotionRule(
                    source_state="D",
                    target_state="E",
                    relation_name="de",
                ),
            ),
        )

    def test_cycle_normalization_is_rotation_invariant(self):
        left = normalize_directed_cycle(
            states=("A", "B", "C"),
            relations=("ab", "bc", "ca"),
        )

        right = normalize_directed_cycle(
            states=("B", "C", "A"),
            relations=("bc", "ca", "ab"),
        )

        self.assertEqual(left, right)

    def test_two_simple_directed_cycles_are_found(self):
        cycles = enumerate_simple_directed_cycles(
            self.graph
        )

        self.assertEqual(len(cycles), 2)

        self.assertEqual(
            {
                cycle.relations
                for cycle in cycles
            },
            {
                ("ab", "ba"),
                ("bc", "cd", "db"),
            },
        )

    def test_cycle_lengths_are_derived(self):
        cycles = enumerate_simple_directed_cycles(
            self.graph
        )

        self.assertEqual(
            {
                cycle.length
                for cycle in cycles
            },
            {2, 3},
        )

    def test_state_character_records_cycle_participation(self):
        field = derive_cycle_participation_character_field(
            self.graph
        )

        self.assertEqual(field["A"], (1, 0))
        self.assertEqual(field["B"], (1, 1))
        self.assertEqual(field["C"], (0, 1))
        self.assertEqual(field["D"], (0, 1))
        self.assertEqual(field["E"], (0, 0))

    def test_shared_return_class_can_have_distinct_characters(self):
        field = derive_cycle_participation_character_field(
            self.graph
        )

        self.assertNotEqual(field["A"], field["B"])
        self.assertNotEqual(field["B"], field["C"])

    def test_states_on_same_cycle_can_share_character(self):
        field = derive_cycle_participation_character_field(
            self.graph
        )

        self.assertEqual(field["C"], field["D"])

    def test_state_outside_all_cycles_has_zero_character(self):
        field = derive_cycle_participation_character_field(
            self.graph
        )

        self.assertEqual(field["E"], (0, 0))

    def test_states_without_cycle_participation_are_reported(self):
        self.assertEqual(
            states_without_cycle_participation(
                self.graph
            ),
            ("E",),
        )

    def test_character_field_covers_all_states(self):
        field = derive_cycle_participation_character_field(
            self.graph
        )

        self.assertEqual(
            set(field),
            set(self.graph.states),
        )

    def test_acyclic_graph_is_rejected(self):
        graph = MotionGraph(
            states=("A", "B", "C"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="ab",
                ),
                MotionRule(
                    source_state="B",
                    target_state="C",
                    relation_name="bc",
                ),
            ),
        )

        with self.assertRaises(ValueError):
            derive_cycle_participation_character_field(
                graph
            )


if __name__ == "__main__":
    unittest.main()
