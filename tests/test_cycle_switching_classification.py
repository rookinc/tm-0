import unittest

from tm0.cycle_switching import cycle_sign_product
from tm0.cycle_switching import switch_cycle_signs
from tm0.cycle_switching_classification import switching_equivalent
from tm0.cycle_switching_classification import switching_witness
from tm0.local_sign_product import LocalSign


class TestCycleSwitchingClassification(unittest.TestCase):
    def test_same_product_is_switching_equivalent(self):
        source = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
        )

        target = (
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
        )

        self.assertEqual(
            cycle_sign_product(source),
            cycle_sign_product(target),
        )

        self.assertTrue(
            switching_equivalent(source, target)
        )

    def test_witness_transforms_source_to_target(self):
        source = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        target = (
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        witness = switching_witness(source, target)

        self.assertIsNotNone(witness)
        self.assertEqual(
            switch_cycle_signs(source, witness),
            target,
        )

    def test_different_products_are_not_switching_equivalent(self):
        source = (
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        target = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        self.assertNotEqual(
            cycle_sign_product(source),
            cycle_sign_product(target),
        )

        self.assertFalse(
            switching_equivalent(source, target)
        )

        self.assertIsNone(
            switching_witness(source, target)
        )

    def test_positive_class_collapses_to_all_preserve(self):
        source = (
            LocalSign.INVERT,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        target = (
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        self.assertTrue(
            switching_equivalent(source, target)
        )

    def test_negative_class_collapses_to_one_invert(self):
        source = (
            LocalSign.INVERT,
            LocalSign.INVERT,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        target = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        self.assertTrue(
            switching_equivalent(source, target)
        )

    def test_equal_length_is_required(self):
        source = (
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        target = (
            LocalSign.PRESERVE,
        )

        with self.assertRaisesRegex(
            ValueError,
            "sign assignments must have equal length",
        ):
            switching_witness(source, target)


if __name__ == "__main__":
    unittest.main()
