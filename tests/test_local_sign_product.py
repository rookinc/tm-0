import unittest

from tm0.incidence_equivalence import EndpointEquivalence
from tm0.incidence_equivalence import anonymous_relations
from tm0.incidence_equivalence import composition_equalities
from tm0.local_sign_product import LocalSign
from tm0.local_sign_product import traverse_signed_cycle
from tm0.orientation_registration import RegistrationValue


def closed_fixture(count):
    relations = anonymous_relations(count)
    equalities = composition_equalities(relations)
    equalities += ((relations[-1].target, relations[0].source),)
    return relations, EndpointEquivalence(equalities)


class TestLocalSignProduct(unittest.TestCase):
    def test_all_preserve_returns_same(self):
        relations, incidence = closed_fixture(5)
        signs = (LocalSign.PRESERVE,) * 5

        result = traverse_signed_cycle(relations, incidence, signs)

        self.assertEqual(result.sign_product, 1)
        self.assertEqual(result.registration, RegistrationValue.SAME)

    def test_one_invert_returns_polar(self):
        relations, incidence = closed_fixture(5)
        signs = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        result = traverse_signed_cycle(relations, incidence, signs)

        self.assertEqual(result.sign_product, -1)
        self.assertEqual(result.registration, RegistrationValue.POLAR)

    def test_two_inverts_return_same(self):
        relations, incidence = closed_fixture(5)
        signs = (
            LocalSign.INVERT,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        result = traverse_signed_cycle(relations, incidence, signs)

        self.assertEqual(result.sign_product, 1)
        self.assertEqual(result.registration, RegistrationValue.SAME)

    def test_sign_product_matches_registration(self):
        relations, incidence = closed_fixture(6)

        cases = (
            (
                (
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                ),
                RegistrationValue.SAME,
            ),
            (
                (
                    LocalSign.INVERT,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                ),
                RegistrationValue.POLAR,
            ),
            (
                (
                    LocalSign.INVERT,
                    LocalSign.INVERT,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                    LocalSign.PRESERVE,
                ),
                RegistrationValue.SAME,
            ),
        )

        for signs, expected in cases:
            with self.subTest(signs=signs):
                result = traverse_signed_cycle(
                    relations,
                    incidence,
                    signs,
                )

                self.assertEqual(result.registration, expected)

                if result.sign_product == 1:
                    self.assertEqual(
                        result.registration,
                        RegistrationValue.SAME,
                    )
                else:
                    self.assertEqual(
                        result.registration,
                        RegistrationValue.POLAR,
                    )

    def test_wrong_sign_count_is_rejected(self):
        relations, incidence = closed_fixture(4)

        with self.assertRaisesRegex(
            ValueError,
            "one local sign is required per relation",
        ):
            traverse_signed_cycle(
                relations,
                incidence,
                (LocalSign.PRESERVE,),
            )


if __name__ == "__main__":
    unittest.main()
