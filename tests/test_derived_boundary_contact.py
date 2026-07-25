import unittest

from tm0.derived_boundary_contact import Boundary
from tm0.derived_boundary_contact import MotionRule
from tm0.derived_boundary_contact import derive_boundary_contact
from tm0.derived_boundary_contact import validate_boundary


class TestDerivedBoundaryContact(unittest.TestCase):
    def setUp(self):
        self.boundary = Boundary(
            name="body-a",
            inside_states=("A", "B"),
            boundary_relations=("touch-edge",),
        )

    def test_inside_to_inside_does_not_cross(self):
        rule = MotionRule(
            source_state="A",
            target_state="B",
            relation_name="internal",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertTrue(contact.source_inside)
        self.assertTrue(contact.target_inside)
        self.assertFalse(contact.crosses_boundary)
        self.assertFalse(contact.touches_boundary)

    def test_inside_to_outside_crosses_boundary(self):
        rule = MotionRule(
            source_state="A",
            target_state="C",
            relation_name="exit",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertTrue(contact.source_inside)
        self.assertFalse(contact.target_inside)
        self.assertTrue(contact.crosses_boundary)
        self.assertTrue(contact.touches_boundary)

    def test_outside_to_inside_crosses_boundary(self):
        rule = MotionRule(
            source_state="C",
            target_state="B",
            relation_name="enter",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertFalse(contact.source_inside)
        self.assertTrue(contact.target_inside)
        self.assertTrue(contact.crosses_boundary)
        self.assertTrue(contact.touches_boundary)

    def test_marked_relation_touches_without_crossing(self):
        rule = MotionRule(
            source_state="A",
            target_state="B",
            relation_name="touch-edge",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertFalse(contact.crosses_boundary)
        self.assertTrue(contact.touches_boundary)

    def test_outside_to_outside_can_touch_marked_boundary(self):
        rule = MotionRule(
            source_state="C",
            target_state="D",
            relation_name="touch-edge",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertFalse(contact.source_inside)
        self.assertFalse(contact.target_inside)
        self.assertFalse(contact.crosses_boundary)
        self.assertTrue(contact.touches_boundary)

    def test_unmarked_outside_motion_has_no_contact(self):
        rule = MotionRule(
            source_state="C",
            target_state="D",
            relation_name="external",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertFalse(contact.crosses_boundary)
        self.assertFalse(contact.touches_boundary)

    def test_contact_records_boundary_and_relation(self):
        rule = MotionRule(
            source_state="A",
            target_state="C",
            relation_name="exit",
        )

        contact = derive_boundary_contact(
            rule,
            self.boundary,
        )

        self.assertEqual(contact.boundary_name, "body-a")
        self.assertEqual(contact.relation_name, "exit")

    def test_empty_inside_state_set_is_rejected(self):
        boundary = Boundary(
            name="empty",
            inside_states=(),
            boundary_relations=(),
        )

        with self.assertRaises(ValueError):
            validate_boundary(boundary)

    def test_duplicate_inside_states_are_rejected(self):
        boundary = Boundary(
            name="duplicate",
            inside_states=("A", "A"),
            boundary_relations=(),
        )

        with self.assertRaises(ValueError):
            validate_boundary(boundary)

    def test_duplicate_boundary_relations_are_rejected(self):
        boundary = Boundary(
            name="duplicate",
            inside_states=("A",),
            boundary_relations=("edge", "edge"),
        )

        with self.assertRaises(ValueError):
            validate_boundary(boundary)


if __name__ == "__main__":
    unittest.main()
