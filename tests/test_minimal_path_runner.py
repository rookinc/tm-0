import unittest

from tm0.minimal_path_runner import derive_traversal_residue
from tm0.minimal_path_runner import run_transition_path
from tm0.minimal_transition_executor import TransitionRule
from tm0.minimal_transition_executor import TransitionSystem


class TestMinimalPathRunner(unittest.TestCase):
    def setUp(self):
        self.system = TransitionSystem(
            states=("A", "B"),
            rules=(
                TransitionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="forward",
                    boundary_contacts=("gate-ab",),
                    cycle_residue=(1, 0),
                ),
                TransitionRule(
                    source_state="B",
                    target_state="A",
                    relation_name="return",
                    boundary_contacts=("gate-ba",),
                    cycle_residue=(0, 1),
                ),
            ),
        )

    def test_one_step_path_does_not_return(self):
        result = run_transition_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward",),
        )

        self.assertEqual(result.initial_state, "A")
        self.assertEqual(result.final_state, "B")
        self.assertFalse(result.returned)

    def test_two_step_path_returns(self):
        result = run_transition_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(result.final_state, "A")
        self.assertTrue(result.returned)

    def test_path_records_visited_states(self):
        result = run_transition_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(
            result.visited_states,
            ("A", "B", "A"),
        )

    def test_path_records_traversed_relations(self):
        result = run_transition_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(
            result.traversed_relations,
            ("forward", "return"),
        )

    def test_path_records_realized_steps(self):
        result = run_transition_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(len(result.steps), 2)
        self.assertEqual(
            result.steps[0].event.traversed_relation,
            "forward",
        )
        self.assertEqual(
            result.steps[1].event.traversed_relation,
            "return",
        )

    def test_residue_is_derived_from_traversal_parity(self):
        residue = derive_traversal_residue(
            self.system,
            ("forward", "return"),
        )

        self.assertEqual(residue, (1, 1))

    def test_repeated_relation_has_even_residue(self):
        residue = derive_traversal_residue(
            self.system,
            ("forward", "forward"),
        )

        self.assertEqual(residue, (0, 0))

    def test_four_step_path_returns_with_even_residue(self):
        result = run_transition_path(
            system=self.system,
            initial_state="A",
            relation_requests=(
                "forward",
                "return",
                "forward",
                "return",
            ),
        )

        self.assertTrue(result.returned)
        self.assertEqual(result.traversal_residue, (0, 0))

    def test_empty_path_is_rejected(self):
        with self.assertRaises(ValueError):
            run_transition_path(
                system=self.system,
                initial_state="A",
                relation_requests=(),
            )

    def test_unknown_initial_state_is_rejected(self):
        with self.assertRaises(ValueError):
            run_transition_path(
                system=self.system,
                initial_state="C",
                relation_requests=("forward",),
            )

    def test_unlawful_relation_sequence_is_rejected(self):
        with self.assertRaises(ValueError):
            run_transition_path(
                system=self.system,
                initial_state="A",
                relation_requests=("return",),
            )

    def test_unknown_relation_in_residue_is_rejected(self):
        with self.assertRaises(ValueError):
            derive_traversal_residue(
                self.system,
                ("missing",),
            )


if __name__ == "__main__":
    unittest.main()
