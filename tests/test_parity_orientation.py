import unittest

from tm0.incidence_equivalence import (
    EndpointEquivalence,
    anonymous_relations,
    composition_equalities,
)
from tm0.orientation_registration import (
    RegistrationValue,
    TraversalReading,
)
from tm0.parity_orientation import (
    invert,
    traverse_with_local_inversion,
)


def closed_fixture(count):
    relations = anonymous_relations(count)

    equalities = composition_equalities(
        relations
    ) + (
        (
            relations[-1].target,
            relations[0].source,
        ),
    )

    incidence = EndpointEquivalence(equalities)

    return relations, incidence


class TestParityOrientation(unittest.TestCase):
    def test_one_inversion_reverses_forward(self):
        self.assertEqual(
            invert(TraversalReading.FORWARD),
            TraversalReading.REVERSED,
        )

    def test_one_inversion_reverses_reversed(self):
        self.assertEqual(
            invert(TraversalReading.REVERSED),
            TraversalReading.FORWARD,
        )

    def test_two_inversions_restore_orientation(self):
        reading = TraversalReading.FORWARD
        reading = invert(reading)
        reading = invert(reading)

        self.assertEqual(
            reading,
            TraversalReading.FORWARD,
        )

    def test_odd_closed_chain_returns_polar(self):
        relations, incidence = closed_fixture(3)

        result = traverse_with_local_inversion(
            relations,
            incidence,
        )

        self.assertEqual(result.relation_count, 3)
        self.assertEqual(
            result.returned,
            TraversalReading.REVERSED,
        )
        self.assertEqual(
            result.registration,
            RegistrationValue.POLAR,
        )

    def test_even_closed_chain_returns_same(self):
        relations, incidence = closed_fixture(4)

        result = traverse_with_local_inversion(
            relations,
            incidence,
        )

        self.assertEqual(result.relation_count, 4)
        self.assertEqual(
            result.returned,
            TraversalReading.FORWARD,
        )
        self.assertEqual(
            result.registration,
            RegistrationValue.SAME,
        )

    def test_five_relation_closure_returns_polar(self):
        relations, incidence = closed_fixture(5)

        result = traverse_with_local_inversion(
            relations,
            incidence,
        )

        self.assertEqual(result.relation_count, 5)
        self.assertEqual(
            result.registration,
            RegistrationValue.POLAR,
        )

    def test_fifteen_relation_closure_returns_polar(self):
        relations, incidence = closed_fixture(15)

        result = traverse_with_local_inversion(
            relations,
            incidence,
        )

        self.assertEqual(result.relation_count, 15)
        self.assertEqual(
            result.registration,
            RegistrationValue.POLAR,
        )

    def test_departure_orientation_does_not_change_parity_result(self):
        odd_relations, odd_incidence = closed_fixture(5)
        even_relations, even_incidence = closed_fixture(6)

        odd_result = traverse_with_local_inversion(
            odd_relations,
            odd_incidence,
            departure=TraversalReading.REVERSED,
        )

        even_result = traverse_with_local_inversion(
            even_relations,
            even_incidence,
            departure=TraversalReading.REVERSED,
        )

        self.assertEqual(
            odd_result.registration,
            RegistrationValue.POLAR,
        )
        self.assertEqual(
            even_result.registration,
            RegistrationValue.SAME,
        )

    def test_open_chain_is_rejected(self):
        relations = anonymous_relations(3)
        incidence = EndpointEquivalence(
            composition_equalities(relations)
        )

        with self.assertRaisesRegex(
            ValueError,
            "parity return requires a closed relation chain",
        ):
            traverse_with_local_inversion(
                relations,
                incidence,
            )


if __name__ == "__main__":
    unittest.main()
