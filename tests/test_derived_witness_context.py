import unittest

from tm0.derived_witness_context import derive_witness_context
from tm0.derived_witness_context import normalize_boundary_signature
from tm0.derived_witness_context import normalize_character


class TestDerivedWitnessContext(unittest.TestCase):
    def test_boundary_signature_is_order_independent(self):
        left = derive_witness_context(
            ("edge-b", "edge-a"),
            (1, 0, 1),
        )

        right = derive_witness_context(
            ("edge-a", "edge-b"),
            (1, 0, 1),
        )

        self.assertEqual(left, right)
        self.assertEqual(
            left.boundary_signature,
            ("edge-a", "edge-b"),
        )

    def test_character_order_is_preserved(self):
        left = derive_witness_context(
            ("edge-a",),
            (1, 0),
        )

        right = derive_witness_context(
            ("edge-a",),
            (0, 1),
        )

        self.assertNotEqual(left, right)
        self.assertEqual(left.character, (1, 0))
        self.assertEqual(right.character, (0, 1))

    def test_context_key_is_structurally_derived(self):
        context = derive_witness_context(
            ("edge-b", "edge-a"),
            (1, 0, 1),
        )

        self.assertEqual(
            context.key,
            "boundary[edge-a,edge-b]|character[101]",
        )

    def test_changed_boundary_changes_context(self):
        left = derive_witness_context(
            ("edge-a", "edge-b"),
            (1, 0),
        )

        right = derive_witness_context(
            ("edge-a", "edge-c"),
            (1, 0),
        )

        self.assertNotEqual(left, right)
        self.assertNotEqual(left.key, right.key)

    def test_changed_character_changes_context(self):
        left = derive_witness_context(
            ("edge-a", "edge-b"),
            (1, 0),
        )

        right = derive_witness_context(
            ("edge-a", "edge-b"),
            (1, 1),
        )

        self.assertNotEqual(left, right)
        self.assertNotEqual(left.key, right.key)

    def test_empty_boundary_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_boundary_signature(())

    def test_duplicate_boundary_entry_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_boundary_signature(
                ("edge-a", "edge-a"),
            )

    def test_empty_character_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_character(())

    def test_nonbinary_character_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_character((1, 2, 0))


if __name__ == "__main__":
    unittest.main()
