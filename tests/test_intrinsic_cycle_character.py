import unittest

from tm0.derived_boundary_contact import MotionRule
from tm0.derived_region_boundary import MotionGraph
from tm0.intrinsic_cycle_character import (
    cycle_rank_after_state_deletion,
)
from tm0.intrinsic_cycle_character import (
    derive_intrinsic_cycle_character_field,
)
from tm0.intrinsic_cycle_character import (
    derive_intrinsic_cycle_signature,
)
from tm0.intrinsic_cycle_character import (
    graph_without_state,
)
from tm0.intrinsic_cycle_character import (
    states_without_intrinsic_cycle_structure,
)


class TestIntrinsicCycleCharacter(unittest.TestCase):
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
                    target_state="C",
                    relation_name="bc",
                ),
                MotionRule(
                    source_state="C",
                    target_state="A",
                    relation_name="ca",
                ),
                MotionRule(
                    source_state="C",
                    target_state="D",
                    relation_name="cd",
                ),
                MotionRule(
                    source_state="D",
                    target_state="A",
                    relation_name="da",
                ),
                MotionRule(
                    source_state="D",
                    target_state="E",
                    relation_name="de",
                ),
            ),
        )

    def test_state_deletion_removes_state_and_incident_rules(self):
        reduced = graph_without_state(
            self.graph,
            "D",
        )

        self.assertEqual(
            reduced.states,
            ("A", "B", "C", "E"),
        )

        self.assertEqual(
            tuple(
                rule.relation_name
                for rule in reduced.rules
            ),
            ("ab", "bc", "ca"),
        )

    def test_cycle_rank_loss_is_intrinsic_to_state_deletion(self):
        signature = derive_intrinsic_cycle_signature(
            self.graph,
            "D",
        )

        self.assertEqual(signature.total_cycle_rank, 2)
        self.assertEqual(signature.deleted_cycle_rank, 1)
        self.assertEqual(signature.cycle_rank_loss, 1)
        self.assertTrue(signature.carries_cycle_structure)

    def test_shared_cycle_core_can_carry_full_rank_loss(self):
        signature = derive_intrinsic_cycle_signature(
            self.graph,
            "A",
        )

        self.assertEqual(signature.total_cycle_rank, 2)
        self.assertEqual(signature.deleted_cycle_rank, 0)
        self.assertEqual(signature.cycle_rank_loss, 2)
        self.assertEqual(signature.character, (1, 1))

    def test_single_rank_loss_gets_prefix_binary_character(self):
        signature = derive_intrinsic_cycle_signature(
            self.graph,
            "D",
        )

        self.assertEqual(signature.character, (1, 0))

    def test_state_outside_cycle_core_has_zero_character(self):
        signature = derive_intrinsic_cycle_signature(
            self.graph,
            "E",
        )

        self.assertEqual(signature.cycle_rank_loss, 0)
        self.assertFalse(signature.carries_cycle_structure)
        self.assertEqual(signature.character, (0, 0))

    def test_character_field_is_binary(self):
        field = derive_intrinsic_cycle_character_field(
            self.graph
        )

        self.assertTrue(
            all(
                bit in (0, 1)
                for character in field.values()
                for bit in character
            )
        )

    def test_character_width_equals_total_cycle_rank(self):
        field = derive_intrinsic_cycle_character_field(
            self.graph
        )

        self.assertTrue(
            all(
                len(character) == 2
                for character in field.values()
            )
        )

    def test_different_rank_loss_gives_different_character(self):
        field = derive_intrinsic_cycle_character_field(
            self.graph
        )

        self.assertEqual(field["B"], (1, 0))
        self.assertEqual(field["C"], (1, 1))
        self.assertNotEqual(field["B"], field["C"])

    def test_state_outside_intrinsic_cycle_structure_is_reported(self):
        self.assertEqual(
            states_without_intrinsic_cycle_structure(
                self.graph
            ),
            ("E",),
        )

    def test_unknown_state_deletion_is_rejected(self):
        with self.assertRaises(ValueError):
            graph_without_state(
                self.graph,
                "X",
            )

    def test_one_cycle_graph_uses_one_bit_character(self):
        graph = MotionGraph(
            states=("A", "B", "C", "D"),
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
                MotionRule(
                    source_state="C",
                    target_state="A",
                    relation_name="ca",
                ),
                MotionRule(
                    source_state="C",
                    target_state="D",
                    relation_name="cd",
                ),
            ),
        )

        field = derive_intrinsic_cycle_character_field(
            graph
        )

        self.assertEqual(field["A"], (1,))
        self.assertEqual(field["B"], (1,))
        self.assertEqual(field["C"], (1,))
        self.assertEqual(field["D"], (0,))

    def test_cycle_rank_after_state_deletion_can_be_zero(self):
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
                MotionRule(
                    source_state="C",
                    target_state="A",
                    relation_name="ca",
                ),
            ),
        )

        self.assertEqual(
            cycle_rank_after_state_deletion(
                graph,
                "A",
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
