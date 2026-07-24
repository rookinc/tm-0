import unittest

from tm0.minimal_transition_executor import StepResult
from tm0.minimal_transition_executor import TransitionRule
from tm0.minimal_transition_executor import TransitionSystem
from tm0.minimal_transition_executor import execute_transition
from tm0.minimal_transition_executor import rule_by_name
from tm0.minimal_transition_executor import validate_transition_system


class TestMinimalTransitionExecutor(unittest.TestCase):
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

    def test_system_validates(self):
        self.assertEqual(
            validate_transition_system(self.system),
            self.system,
        )

    def test_rule_is_found_by_name(self):
        rule = rule_by_name(
            self.system,
            "forward",
        )

        self.assertEqual(rule.source_state, "A")
        self.assertEqual(rule.target_state, "B")

    def test_lawful_transition_executes(self):
        result = execute_transition(
            self.system,
            current_state="A",
            relation_name="forward",
        )

        self.assertIsInstance(result, StepResult)
        self.assertEqual(result.prior_state, "A")
        self.assertEqual(result.next_state, "B")

    def test_execution_emits_realized_event(self):
        result = execute_transition(
            self.system,
            current_state="A",
            relation_name="forward",
        )

        self.assertEqual(result.event.source_state, "A")
        self.assertEqual(result.event.target_state, "B")
        self.assertEqual(
            result.event.traversed_relation,
            "forward",
        )
        self.assertEqual(
            result.event.boundary_contacts,
            ("gate-ab",),
        )
        self.assertEqual(
            result.event.cycle_residue,
            (1, 0),
        )

    def test_return_transition_executes(self):
        result = execute_transition(
            self.system,
            current_state="B",
            relation_name="return",
        )

        self.assertEqual(result.prior_state, "B")
        self.assertEqual(result.next_state, "A")
        self.assertEqual(
            result.event.traversed_relation,
            "return",
        )

    def test_relation_from_wrong_state_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_transition(
                self.system,
                current_state="B",
                relation_name="forward",
            )

    def test_unknown_relation_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_transition(
                self.system,
                current_state="A",
                relation_name="missing",
            )

    def test_unknown_current_state_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_transition(
                self.system,
                current_state="C",
                relation_name="forward",
            )

    def test_duplicate_relation_names_are_rejected(self):
        system = TransitionSystem(
            states=("A", "B"),
            rules=(
                TransitionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="move",
                    boundary_contacts=("gate-ab",),
                    cycle_residue=(1,),
                ),
                TransitionRule(
                    source_state="B",
                    target_state="A",
                    relation_name="move",
                    boundary_contacts=("gate-ba",),
                    cycle_residue=(0,),
                ),
            ),
        )

        with self.assertRaises(ValueError):
            validate_transition_system(system)

    def test_rule_with_unknown_target_is_rejected(self):
        system = TransitionSystem(
            states=("A", "B"),
            rules=(
                TransitionRule(
                    source_state="A",
                    target_state="C",
                    relation_name="forward",
                    boundary_contacts=("gate-ac",),
                    cycle_residue=(1,),
                ),
            ),
        )

        with self.assertRaises(ValueError):
            validate_transition_system(system)


if __name__ == "__main__":
    unittest.main()
