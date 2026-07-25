import unittest

from tm0.boundary_aware_executor import BoundaryAwarePathReceipt
from tm0.boundary_aware_executor import BoundaryAwareStepEvent
from tm0.boundary_aware_executor import BoundaryAwareSystem
from tm0.boundary_aware_executor import execute_boundary_aware_path
from tm0.boundary_aware_executor import execute_boundary_aware_step
from tm0.boundary_aware_executor import validate_boundary_aware_system
from tm0.derived_boundary_contact import Boundary
from tm0.derived_boundary_contact import MotionRule


class TestBoundaryAwareExecutor(unittest.TestCase):
    def setUp(self):
        self.system = BoundaryAwareSystem(
            states=("A", "B", "C"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="internal",
                ),
                MotionRule(
                    source_state="B",
                    target_state="C",
                    relation_name="exit",
                ),
                MotionRule(
                    source_state="C",
                    target_state="B",
                    relation_name="enter",
                ),
                MotionRule(
                    source_state="B",
                    target_state="A",
                    relation_name="return",
                ),
            ),
            boundary=Boundary(
                name="body-ab",
                inside_states=("A", "B"),
                boundary_relations=("return",),
            ),
        )

    def test_system_validates(self):
        self.assertEqual(
            validate_boundary_aware_system(self.system),
            self.system,
        )

    def test_step_event_has_no_authored_contact_field_on_rule(self):
        rule = self.system.rules[0]

        self.assertFalse(
            hasattr(rule, "boundary_contacts")
        )

    def test_internal_step_derives_no_contact(self):
        event = execute_boundary_aware_step(
            system=self.system,
            current_state="A",
            relation_name="internal",
        )

        self.assertIsInstance(
            event,
            BoundaryAwareStepEvent,
        )
        self.assertFalse(
            event.boundary_contact.crosses_boundary
        )
        self.assertFalse(
            event.boundary_contact.touches_boundary
        )

    def test_exit_step_derives_crossing_contact(self):
        event = execute_boundary_aware_step(
            system=self.system,
            current_state="B",
            relation_name="exit",
        )

        self.assertTrue(
            event.boundary_contact.source_inside
        )
        self.assertFalse(
            event.boundary_contact.target_inside
        )
        self.assertTrue(
            event.boundary_contact.crosses_boundary
        )
        self.assertTrue(
            event.boundary_contact.touches_boundary
        )

    def test_enter_step_derives_crossing_contact(self):
        event = execute_boundary_aware_step(
            system=self.system,
            current_state="C",
            relation_name="enter",
        )

        self.assertFalse(
            event.boundary_contact.source_inside
        )
        self.assertTrue(
            event.boundary_contact.target_inside
        )
        self.assertTrue(
            event.boundary_contact.crosses_boundary
        )

    def test_marked_internal_relation_touches_without_crossing(self):
        event = execute_boundary_aware_step(
            system=self.system,
            current_state="B",
            relation_name="return",
        )

        self.assertFalse(
            event.boundary_contact.crosses_boundary
        )
        self.assertTrue(
            event.boundary_contact.touches_boundary
        )

    def test_path_accumulates_boundary_aware_events(self):
        receipt = execute_boundary_aware_path(
            system=self.system,
            initial_state="A",
            relation_requests=(
                "internal",
                "exit",
                "enter",
                "return",
            ),
        )

        self.assertIsInstance(
            receipt,
            BoundaryAwarePathReceipt,
        )
        self.assertEqual(
            len(receipt.step_events),
            4,
        )
        self.assertFalse(
            receipt.step_events[0]
            .boundary_contact
            .touches_boundary
        )
        self.assertTrue(
            receipt.step_events[1]
            .boundary_contact
            .crosses_boundary
        )
        self.assertTrue(
            receipt.step_events[2]
            .boundary_contact
            .crosses_boundary
        )
        self.assertTrue(
            receipt.step_events[3]
            .boundary_contact
            .touches_boundary
        )

    def test_path_returns_and_derives_residue(self):
        receipt = execute_boundary_aware_path(
            system=self.system,
            initial_state="A",
            relation_requests=(
                "internal",
                "exit",
                "enter",
                "return",
            ),
        )

        self.assertTrue(receipt.returned)
        self.assertEqual(receipt.final_state, "A")
        self.assertEqual(
            receipt.traversal_residue,
            (1, 1, 1, 1),
        )

    def test_wrong_source_state_is_rejected(self):
        with self.assertRaises(ValueError):
            execute_boundary_aware_step(
                system=self.system,
                current_state="A",
                relation_name="exit",
            )

    def test_boundary_with_unknown_state_is_rejected(self):
        system = BoundaryAwareSystem(
            states=("A", "B"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="move",
                ),
            ),
            boundary=Boundary(
                name="bad",
                inside_states=("A", "C"),
                boundary_relations=(),
            ),
        )

        with self.assertRaises(ValueError):
            validate_boundary_aware_system(system)

    def test_boundary_with_unknown_relation_is_rejected(self):
        system = BoundaryAwareSystem(
            states=("A", "B"),
            rules=(
                MotionRule(
                    source_state="A",
                    target_state="B",
                    relation_name="move",
                ),
            ),
            boundary=Boundary(
                name="bad",
                inside_states=("A",),
                boundary_relations=("missing",),
            ),
        )

        with self.assertRaises(ValueError):
            validate_boundary_aware_system(system)


if __name__ == "__main__":
    unittest.main()
