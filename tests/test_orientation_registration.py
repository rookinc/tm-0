import unittest

from tm0.incidence_equivalence import (
    EndpointEquivalence,
    anonymous_relations,
    composition_equalities,
)
from tm0.orientation_registration import (
    OrientedReturn,
    RegistrationValue,
    TraversalReading,
    compare_orientations,
    unregistered_return,
)
from tm0.return_admissibility import realize_return


class TestOrientationRegistration(unittest.TestCase):
    def setUp(self):
        self.relations = anonymous_relations(3)

        closed_equalities = composition_equalities(
            self.relations
        ) + (
            (
                self.relations[-1].target,
                self.relations[0].source,
            ),
        )

        self.incidence = EndpointEquivalence(
            closed_equalities
        )

        self.receipt = realize_return(
            self.relations,
            self.incidence,
        )

    def test_return_receipt_alone_has_null_registration(self):
        self.assertEqual(
            unregistered_return(self.receipt),
            RegistrationValue.NULL,
        )

    def test_same_orientation_registers_same(self):
        departure = OrientedReturn(
            receipt=self.receipt,
            reading=TraversalReading.FORWARD,
        )
        returned = OrientedReturn(
            receipt=self.receipt,
            reading=TraversalReading.FORWARD,
        )

        registration = compare_orientations(
            departure,
            returned,
        )

        self.assertEqual(
            registration.value,
            RegistrationValue.SAME,
        )

    def test_opposite_orientation_registers_polarity(self):
        departure = OrientedReturn(
            receipt=self.receipt,
            reading=TraversalReading.FORWARD,
        )
        returned = OrientedReturn(
            receipt=self.receipt,
            reading=TraversalReading.REVERSED,
        )

        registration = compare_orientations(
            departure,
            returned,
        )

        self.assertEqual(
            registration.value,
            RegistrationValue.POLAR,
        )

    def test_reverse_departure_and_forward_return_are_also_polar(self):
        departure = OrientedReturn(
            receipt=self.receipt,
            reading=TraversalReading.REVERSED,
        )
        returned = OrientedReturn(
            receipt=self.receipt,
            reading=TraversalReading.FORWARD,
        )

        registration = compare_orientations(
            departure,
            returned,
        )

        self.assertEqual(
            registration.value,
            RegistrationValue.POLAR,
        )

    def test_polarity_is_symmetric_under_exchange(self):
        first = compare_orientations(
            OrientedReturn(
                receipt=self.receipt,
                reading=TraversalReading.FORWARD,
            ),
            OrientedReturn(
                receipt=self.receipt,
                reading=TraversalReading.REVERSED,
            ),
        )

        second = compare_orientations(
            OrientedReturn(
                receipt=self.receipt,
                reading=TraversalReading.REVERSED,
            ),
            OrientedReturn(
                receipt=self.receipt,
                reading=TraversalReading.FORWARD,
            ),
        )

        self.assertEqual(first.value, second.value)
        self.assertEqual(
            first.value,
            RegistrationValue.POLAR,
        )

    def test_different_receipts_cannot_be_compared(self):
        other_relations = anonymous_relations(2)

        other_equalities = composition_equalities(
            other_relations
        ) + (
            (
                other_relations[-1].target,
                other_relations[0].source,
            ),
        )

        other_receipt = realize_return(
            other_relations,
            EndpointEquivalence(other_equalities),
        )

        with self.assertRaisesRegex(
            ValueError,
            "orientation comparison requires the same return receipt",
        ):
            compare_orientations(
                OrientedReturn(
                    receipt=self.receipt,
                    reading=TraversalReading.FORWARD,
                ),
                OrientedReturn(
                    receipt=other_receipt,
                    reading=TraversalReading.REVERSED,
                ),
            )

    def test_return_does_not_select_reversed_reading(self):
        possible_readings = {
            TraversalReading.FORWARD,
            TraversalReading.REVERSED,
        }

        self.assertEqual(len(possible_readings), 2)
        self.assertEqual(
            unregistered_return(self.receipt),
            RegistrationValue.NULL,
        )


if __name__ == "__main__":
    unittest.main()
