import unittest

from tm0.register import AddressedState, realize


class TestMinimalAddressedState(unittest.TestCase):
    def test_carrier_can_arise_with_null_registration(self):
        event = realize(AddressedState.ABSENT, AddressedState.NULL)

        self.assertTrue(event.changed)
        self.assertEqual(event.before, AddressedState.ABSENT)
        self.assertEqual(event.after, AddressedState.NULL)

    def test_null_can_resolve_to_a(self):
        event = realize(AddressedState.NULL, AddressedState.A)
        self.assertTrue(event.changed)

    def test_null_can_resolve_to_b(self):
        event = realize(AddressedState.NULL, AddressedState.B)
        self.assertTrue(event.changed)

    def test_a_can_return_to_null(self):
        event = realize(AddressedState.A, AddressedState.NULL)
        self.assertTrue(event.changed)

    def test_b_can_return_to_null(self):
        event = realize(AddressedState.B, AddressedState.NULL)
        self.assertTrue(event.changed)

    def test_a_can_flip_to_b(self):
        event = realize(AddressedState.A, AddressedState.B)
        self.assertTrue(event.changed)

    def test_b_can_flip_to_a(self):
        event = realize(AddressedState.B, AddressedState.A)
        self.assertTrue(event.changed)

    def test_null_to_null_is_not_a_realization(self):
        with self.assertRaisesRegex(
            ValueError,
            "identity transition is not a realization",
        ):
            realize(AddressedState.NULL, AddressedState.NULL)

    def test_absent_to_absent_is_not_a_realization(self):
        with self.assertRaisesRegex(
            ValueError,
            "identity transition is not a realization",
        ):
            realize(AddressedState.ABSENT, AddressedState.ABSENT)


if __name__ == "__main__":
    unittest.main()
