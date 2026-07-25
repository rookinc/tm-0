import unittest

from tm0.derived_boundary_contact import MotionRule
from tm0.derived_fundamental_cycle_character import (
    derive_fundamental_cycle_character_field,
)
from tm0.derived_fundamental_cycle_character import (
    derive_fundamental_cycles,
)
from tm0.derived_fundamental_cycle_character import (
    derive_spanning_forest,
)
from tm0.derived_fundamental_cycle_character import (
    states_without_basis_cycle_participation,
)
from tm0.derived_fundamental_cycle_character import (
    undirected_cycle_rank,
)
from tm0.derived_region_boundary import MotionGraph


class TestDerivedFundamentalCycleCharacter(unittest.TestCase):
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

    def test_spanning_forest_is_deterministic(self):
        forest = derive_spanning_forest(self.graph)

        self.assertEqual(
            forest.tree_relations,
            ("ab", "bc", "cd", "de"),
        )
        self.assertEqual(
            forest.non_tree_relations,
            ("ca", "da"),
        )
        self.assertEqual(forest.component_count, 1)

    def test_cycle_rank_matches_non_tree_relation_count(self):
        forest = derive_spanning_forest(self.graph)

        self.assertEqual(
            undirected_cycle_rank(self.graph),
            2,
        )
        self.assertEqual(
            len(forest.non_tree_relations),
            2,
        )

    def test_two_fundamental_cycles_are_derived(self):
        cycles = derive_fundamental_cycles(
            self.graph
        )

        self.assertEqual(len(cycles), 2)
        self.assertEqual(
            tuple(
                cycle.closing_relation
                for cycle in cycles
            ),
            ("ca", "da"),
        )

    def test_first_cycle_uses_tree_path_a_b_c(self):
        cycles = derive_fundamental_cycles(
            self.graph
        )

        first = cycles[0]

        self.assertEqual(
            first.states,
            ("C", "B", "A"),
        )
        self.assertEqual(
            first.tree_relations,
            ("bc", "ab"),
        )
        self.assertEqual(
            first.relations,
            ("bc", "ab", "ca"),
        )

    def test_second_cycle_uses_tree_path_d_c_b_a(self):
        cycles = derive_fundamental_cycles(
            self.graph
        )

        second = cycles[1]

        self.assertEqual(
            second.states,
            ("D", "C", "B", "A"),
        )
        self.assertEqual(
            second.tree_relations,
            ("cd", "bc", "ab"),
        )
        self.assertEqual(
            second.relations,
            ("cd", "bc", "ab", "da"),
        )

    def test_character_records_basis_cycle_participation(self):
        field = derive_fundamental_cycle_character_field(
            self.graph
        )

        self.assertEqual(field["A"], (1, 1))
        self.assertEqual(field["B"], (1, 1))
        self.assertEqual(field["C"], (1, 1))
        self.assertEqual(field["D"], (0, 1))
        self.assertEqual(field["E"], (0, 0))

    def test_state_outside_basis_cycles_has_zero_character(self):
        field = derive_fundamental_cycle_character_field(
            self.graph
        )

        self.assertEqual(field["E"], (0, 0))

    def test_states_without_basis_participation_are_reported(self):
        self.assertEqual(
            states_without_basis_cycle_participation(
                self.graph
            ),
            ("E",),
        )

    def test_character_width_equals_cycle_rank(self):
        field = derive_fundamental_cycle_character_field(
            self.graph
        )

        self.assertTrue(
            all(
                len(character) == 2
                for character in field.values()
            )
        )

    def test_tree_graph_is_rejected(self):
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

        self.assertEqual(
            undirected_cycle_rank(graph),
            0,
        )

        with self.assertRaises(ValueError):
            derive_fundamental_cycle_character_field(
                graph
            )


if __name__ == "__main__":
    unittest.main()
