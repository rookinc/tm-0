import unittest

from tm0.carrier_plurality import (
    extensional_catalogue,
    instantiate_null_carrier,
)


class TestCarrierPlurality(unittest.TestCase):
    def test_two_instantiations_are_equal_by_admitted_structure(self):
        first = instantiate_null_carrier()
        second = instantiate_null_carrier()

        self.assertEqual(first, second)

    def test_two_null_carriers_collapse_to_one_description(self):
        first = instantiate_null_carrier()
        second = instantiate_null_carrier()

        catalogue = extensional_catalogue([first, second])

        self.assertEqual(len(catalogue), 1)
        self.assertEqual(catalogue[0], first)

    def test_python_identity_exists_but_is_not_lawful_structure(self):
        first = instantiate_null_carrier()
        second = instantiate_null_carrier()

        self.assertIsNot(first, second)
        self.assertEqual(first, second)

    def test_repetition_changes_multiplicity_not_description(self):
        carrier = instantiate_null_carrier()

        one = extensional_catalogue([carrier])
        many = extensional_catalogue([carrier, carrier, carrier])

        self.assertEqual(one, many)


if __name__ == "__main__":
    unittest.main()
