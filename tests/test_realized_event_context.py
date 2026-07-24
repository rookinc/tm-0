import unittest

from tm0.realized_event_context import RealizedEvent
from tm0.realized_event_context import derive_boundary_signature
from tm0.realized_event_context import derive_context_from_realized_event
from tm0.realized_event_context import derive_event_character
from tm0.realized_event_context import validate_realized_event


class TestRealizedEventContext(unittest.TestCase):
    def test_boundary_signature_is_derived_from_event(self):
        event = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north", "east"),
            cycle_residue=(1, 0),
        )

        signature = derive_boundary_signature(event)

        self.assertEqual(
            signature,
            (
                "transition:A->B",
                "relation:r1",
                "contact:north",
                "contact:east",
            ),
        )

    def test_character_is_derived_from_event(self):
        event = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north",),
            cycle_residue=(1, 0, 1),
        )

        self.assertEqual(
            derive_event_character(event),
            (1, 1, 1, 0, 1),
        )

    def test_stationary_event_records_no_state_change(self):
        event = RealizedEvent(
            source_state="A",
            target_state="A",
            traversed_relation="loop",
            boundary_contacts=("north",),
            cycle_residue=(0,),
        )

        self.assertEqual(
            derive_event_character(event),
            (0, 1, 0),
        )

    def test_equivalent_contact_order_gives_same_context(self):
        left = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north", "east"),
            cycle_residue=(1, 0),
        )

        right = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("east", "north"),
            cycle_residue=(1, 0),
        )

        self.assertEqual(
            derive_context_from_realized_event(left),
            derive_context_from_realized_event(right),
        )

    def test_changed_relation_changes_context(self):
        left = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north",),
            cycle_residue=(1,),
        )

        right = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r2",
            boundary_contacts=("north",),
            cycle_residue=(1,),
        )

        self.assertNotEqual(
            derive_context_from_realized_event(left),
            derive_context_from_realized_event(right),
        )

    def test_changed_cycle_residue_changes_context(self):
        left = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north",),
            cycle_residue=(1, 0),
        )

        right = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north",),
            cycle_residue=(0, 1),
        )

        self.assertNotEqual(
            derive_context_from_realized_event(left),
            derive_context_from_realized_event(right),
        )

    def test_empty_source_is_rejected(self):
        event = RealizedEvent(
            source_state="",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north",),
            cycle_residue=(1,),
        )

        with self.assertRaises(ValueError):
            validate_realized_event(event)

    def test_duplicate_contact_is_rejected(self):
        event = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north", "north"),
            cycle_residue=(1,),
        )

        with self.assertRaises(ValueError):
            validate_realized_event(event)

    def test_nonbinary_cycle_residue_is_rejected(self):
        event = RealizedEvent(
            source_state="A",
            target_state="B",
            traversed_relation="r1",
            boundary_contacts=("north",),
            cycle_residue=(2,),
        )

        with self.assertRaises(ValueError):
            validate_realized_event(event)


if __name__ == "__main__":
    unittest.main()
