import unittest

from tm0.carrier_register import (
    Carrier,
    InternalRegister,
    instantiate_carrier,
    realize_register,
)


class TestCarrierSeparatedRegister(unittest.TestCase):
    def test_internal_register_has_two_states(self):
        self.assertEqual(
            set(InternalRegister),
            {
                InternalRegister.NULL,
                InternalRegister.CHARACTERIZED,
            },
        )

    def test_absence_is_not_an_internal_register_value(self):
        values = {state.value for state in InternalRegister}
        self.assertNotIn("ABSENT", values)

    def test_carrier_instantiates_at_null(self):
        event = instantiate_carrier()

        self.assertIsNone(event.before)
        self.assertEqual(
            event.after,
            Carrier(register=InternalRegister.NULL),
        )
        self.assertTrue(event.changed)

    def test_null_can_become_characterized(self):
        event = realize_register(
            Carrier(register=InternalRegister.NULL),
            Carrier(register=InternalRegister.CHARACTERIZED),
        )
        self.assertTrue(event.changed)

    def test_characterized_can_return_to_null(self):
        event = realize_register(
            Carrier(register=InternalRegister.CHARACTERIZED),
            Carrier(register=InternalRegister.NULL),
        )
        self.assertTrue(event.changed)

    def test_null_to_null_is_identity(self):
        carrier = Carrier(register=InternalRegister.NULL)

        with self.assertRaisesRegex(
            ValueError,
            "identity transition is not an internal realization",
        ):
            realize_register(carrier, carrier)

    def test_characterized_to_characterized_is_identity(self):
        carrier = Carrier(register=InternalRegister.CHARACTERIZED)

        with self.assertRaisesRegex(
            ValueError,
            "identity transition is not an internal realization",
        ):
            realize_register(carrier, carrier)


if __name__ == "__main__":
    unittest.main()
