import unittest

from tm0.incidence_equivalence import EndpointEquivalence
from tm0.incidence_equivalence import anonymous_relations
from tm0.incidence_equivalence import composition_equalities
from tm0.local_orientation_law import LocalOrientationLaw
from tm0.local_orientation_law import traverse_with_local_law
from tm0.orientation_registration import RegistrationValue


def closed_fixture(count):
    relations = anonymous_relations(count)
    equalities = composition_equalities(relations)
    equalities += ((relations[-1].target, relations[0].source),)
    return relations, EndpointEquivalence(equalities)


class TestLocalOrientationLaw(unittest.TestCase):
    def test_same_incidence_admits_both_laws(self):
        relations, incidence = closed_fixture(5)

        preserve = traverse_with_local_law(
            relations, incidence, LocalOrientationLaw.PRESERVE
        )
        invert = traverse_with_local_law(
            relations, incidence, LocalOrientationLaw.INVERT
        )

        self.assertEqual(preserve.registration, RegistrationValue.SAME)
        self.assertEqual(invert.registration, RegistrationValue.POLAR)

    def test_even_chain_hides_law_difference(self):
        relations, incidence = closed_fixture(4)

        preserve = traverse_with_local_law(
            relations, incidence, LocalOrientationLaw.PRESERVE
        )
        invert = traverse_with_local_law(
            relations, incidence, LocalOrientationLaw.INVERT
        )

        self.assertEqual(preserve.registration, RegistrationValue.SAME)
        self.assertEqual(invert.registration, RegistrationValue.SAME)


if __name__ == "__main__":
    unittest.main()
