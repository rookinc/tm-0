import unittest

from tm0.derived_boundary_contact import MotionRule
from tm0.derived_region_boundary import MotionGraph
from tm0.refined_intrinsic_character import (
    derive_perturbation_signature,
)
from tm0.refined_intrinsic_character import (
    derive_refined_intrinsic_character_field,
)
from tm0.refined_intrinsic_character import (
    perturbation_signatures,
)
from tm0.refined_intrinsic_character import (
    unary_block,
)
from tm0.refined_intrinsic_character import (
    undirected_component_count,
)


class TestRefinedIntrinsicCharacter(unittest.TestCase):
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

    def test_original_graph_is_connected(self):
        self.assertEqual(
            undirected_component_count(self.graph),
            1,
        )

    def test_cycle_core_state_has_full_rank_loss(self):
        signature = derive_perturbation_signature(
            self.graph,
            "A",
        )

        self.assertEqual(signature.cycle_rank_loss, 2)

    def test_partial_cycle_state_has_partial_rank_loss(self):
        signature = derive_perturbation_signature(
            self.graph,
            "D",
        )

        self.assertEqual(signature.cycle_rank_loss, 1)

    def test_leaf_state_has_zero_rank_loss(self):
        signature = derive_perturbation_signature(
            self.graph,
            "E",
        )

        self.assertEqual(signature.cycle_rank_loss, 0)

    def test_deleting_bridge_like_state_can_increase_components(self):
        signature = derive_perturbation_signature(
            self.graph,
            "D",
        )

        self.assertEqual(signature.component_gain, 1)

    def test_deleting_leaf_does_not_increase_components(self):
        signature = derive_perturbation_signature(
            self.graph,
            "E",
        )

        self.assertEqual(signature.component_gain, 0)

    def test_surviving_return_profile_is_recorded(self):
        signature = derive_perturbation_signature(
            self.graph,
            "D",
        )

        self.assertEqual(
            signature.surviving_return_class_count,
            2,
        )
        self.assertEqual(
            signature.largest_surviving_return_class_size,
            3,
        )

    def test_signatures_distinguish_equal_rank_loss_damage(self):
        graph = MotionGraph(
            states=("A", "B", "C", "D", "E", "F"),
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
                    target_state="E",
                    relation_name="de",
                ),
                MotionRule(
                    source_state="E",
                    target_state="C",
                    relation_name="ec",
                ),
                MotionRule(
                    source_state="D",
                    target_state="F",
                    relation_name="df",
                ),
            ),
        )

        c_signature = derive_perturbation_signature(
            graph,
            "C",
        )

        d_signature = derive_perturbation_signature(
            graph,
            "D",
        )

        self.assertNotEqual(
            c_signature,
            d_signature,
        )

    def test_unary_block_encodes_value(self):
        self.assertEqual(
            unary_block(2, 4),
            (1, 1, 0, 0),
        )

    def test_unary_block_rejects_excess_value(self):
        with self.assertRaises(ValueError):
            unary_block(3, 2)

    def test_refined_character_field_is_binary(self):
        field = derive_refined_intrinsic_character_field(
            self.graph
        )

        self.assertTrue(
            all(
                bit in (0, 1)
                for character in field.values()
                for bit in character
            )
        )

    def test_refined_character_field_has_equal_width(self):
        field = derive_refined_intrinsic_character_field(
            self.graph
        )

        widths = {
            len(character)
            for character in field.values()
        }

        self.assertEqual(len(widths), 1)

    def test_refined_character_distinguishes_leaf_from_cycle_core(self):
        field = derive_refined_intrinsic_character_field(
            self.graph
        )

        self.assertNotEqual(
            field["A"],
            field["E"],
        )

    def test_signature_map_covers_all_states(self):
        signatures = perturbation_signatures(
            self.graph
        )

        self.assertEqual(
            set(signatures),
            set(self.graph.states),
        )

    def test_unknown_state_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_perturbation_signature(
                self.graph,
                "X",
            )


if __name__ == "__main__":
    unittest.main()
