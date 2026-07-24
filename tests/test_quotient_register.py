import unittest

from tm0.quotient_register import (
    QuotientState,
    forget_polarity,
    realize_quotient,
)
from tm0.register import AddressedState


class TestCharacterBlindQuotient(unittest.TestCase):
    def test_absent_survives_the_quotient(self):
        self.assertEqual(
            forget_polarity(AddressedState.ABSENT),
            QuotientState.ABSENT,
        )

    def test_null_survives_the_quotient(self):
        self.assertEqual(
            forget_polarity(AddressedState.NULL),
            QuotientState.NULL,
        )

    def test_a_becomes_characterized(self):
        self.assertEqual(
            forget_polarity(AddressedState.A),
            QuotientState.CHARACTERIZED,
        )

    def test_b_becomes_characterized(self):
        self.assertEqual(
            forget_polarity(AddressedState.B),
            QuotientState.CHARACTERIZED,
        )

    def test_carrier_can_arise_with_null_registration(self):
        event = realize_quotient(
            QuotientState.ABSENT,
            QuotientState.NULL,
        )
        self.assertTrue(event.changed)

    def test_null_can_become_characterized(self):
        event = realize_quotient(
            QuotientState.NULL,
            QuotientState.CHARACTERIZED,
        )
        self.assertTrue(event.changed)

    def test_characterized_can_return_to_null(self):
        event = realize_quotient(
            QuotientState.CHARACTERIZED,
            QuotientState.NULL,
        )
        self.assertTrue(event.changed)

    def test_null_identity_is_rejected(self):
        with self.assertRaisesRegex(
            ValueError,
            "identity transition is not a quotient realization",
        ):
            realize_quotient(
                QuotientState.NULL,
                QuotientState.NULL,
            )

    def test_a_to_b_flip_disappears_in_the_quotient(self):
        before = forget_polarity(AddressedState.A)
        after = forget_polarity(AddressedState.B)

        self.assertEqual(before, after)

        with self.assertRaisesRegex(
            ValueError,
            "identity transition is not a quotient realization",
        ):
            realize_quotient(before, after)


if __name__ == "__main__":
    unittest.main()
