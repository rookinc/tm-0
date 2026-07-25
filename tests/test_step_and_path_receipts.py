import unittest

from tm0.step_and_path_receipts import PathReceipt
from tm0.step_and_path_receipts import StepEvent
from tm0.step_and_path_receipts import StepRule
from tm0.step_and_path_receipts import StepSystem
from tm0.step_and_path_receipts import derive_path_residue
from tm0.step_and_path_receipts import execute_path
from tm0.step_and_path_receipts import execute_step
from tm0.step_and_path_receipts import validate_step_system


class TestStepAndPathReceipts(unittest.TestCase):
    def setUp(self):
        self.system = StepSystem(
            states=("A", "B"),
            rules=(
                StepRule(
                    source_state="A",
                    target_state="B",
                    relation_name="forward",
                    boundary_contacts=("gate-ab",),
                ),
                StepRule(
                    source_state="B",
                    target_state="A",
                    relation_name="return",
                    boundary_contacts=("gate-ba",),
                ),
            ),
        )

    def test_step_rule_has_no_cycle_residue(self):
        rule = self.system.rules[0]

        self.assertFalse(
            hasattr(rule, "cycle_residue")
        )

    def test_step_event_has_no_cycle_residue(self):
        event = execute_step(
            system=self.system,
            current_state="A",
            relation_name="forward",
        )

        self.assertIsInstance(event, StepEvent)
        self.assertFalse(
            hasattr(event, "cycle_residue")
        )

    def test_step_event_records_only_step_trace(self):
        event = execute_step(
            system=self.system,
            current_state="A",
            relation_name="forward",
        )

        self.assertEqual(event.source_state, "A")
        self.assertEqual(event.target_state, "B")
        self.assertEqual(
            event.traversed_relation,
            "forward",
        )
        self.assertEqual(
            event.boundary_contacts,
            ("gate-ab",),
        )

    def test_two_step_path_returns(self):
        receipt = execute_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertIsInstance(receipt, PathReceipt)
        self.assertTrue(receipt.returned)
        self.assertEqual(receipt.final_state, "A")

    def test_path_receipt_contains_ordered_step_events(self):
        receipt = execute_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(len(receipt.step_events), 2)
        self.assertEqual(
            receipt.step_events[0].traversed_relation,
            "forward",
        )
        self.assertEqual(
            receipt.step_events[1].traversed_relation,
            "return",
        )

    def test_path_receipt_contains_visited_states(self):
        receipt = execute_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(
            receipt.visited_states,
            ("A", "B", "A"),
        )

    def test_path_receipt_earns_residue(self):
        receipt = execute_path(
            system=self.system,
            initial_state="A",
            relation_requests=("forward", "return"),
        )

        self.assertEqual(
            receipt.traversal_residue,
            (1, 1),
        )

    def test_repeated_return_path_has_even_residue(self):
        receipt = execute_path(
            system=self.system,
            initial_state="A",
            relation_requests=(
                "forward",
                "return",
                "forward",
                "return",
            ),
        )

        self.assertTrue(receipt.returned)
        self.assertEqual(
            receipt.traversal_residue,
            (0, 0),
        )

    def test_residue_is_derived_from_path_history(self):
        residue = derive_path_residue(
            self.system,
            ("forward", "return", "forward"),
        )

        self.assertEqual(residue, (0, 1))

    def test_wrong_source_state_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_step(
                system=self.system,
                current_state="B",
                relation_name="forward",
            )

    def test_empty_path_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_path(
                system=self.system,
                initial_state="A",
                relation_requests=(),
            )

    def test_duplicate_relation_names_are_rejected(self):
        system = StepSystem(
            states=("A", "B"),
            rules=(
                StepRule(
                    source_state="A",
                    target_state="B",
                    relation_name="move",
                    boundary_contacts=("gate-ab",),
                ),
                StepRule(
                    source_state="B",
                    target_state="A",
                    relation_name="move",
                    boundary_contacts=("gate-ba",),
                ),
            ),
        )

        with self.assertRaises(ValueError):
            validate_step_system(system)


if __name__ == "__main__":
    unittest.main()
