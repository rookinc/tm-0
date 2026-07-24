import unittest

from tm0.cycle_switching import cycle_sign_product
from tm0.cycle_switching import switch_cycle_signs
from tm0.cycle_switching import switching_preserves_cycle_product
from tm0.local_sign_product import LocalSign


class TestCycleSwitching(unittest.TestCase):
    def test_single_local_switch_changes_adjacent_edge_signs(self):
        signs = (
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        switches = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        transformed = switch_cycle_signs(signs, switches)

        self.assertEqual(
            transformed,
            (
                LocalSign.INVERT,
                LocalSign.PRESERVE,
                LocalSign.PRESERVE,
                LocalSign.INVERT,
            ),
        )

    def test_cycle_product_is_preserved(self):
        signs = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        switches = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
        )

        self.assertTrue(
            switching_preserves_cycle_product(signs, switches)
        )

    def test_positive_cycle_remains_positive(self):
        signs = (
            LocalSign.INVERT,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        switches = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
        )

        transformed = switch_cycle_signs(signs, switches)

        self.assertEqual(cycle_sign_product(signs), 1)
        self.assertEqual(cycle_sign_product(transformed), 1)

    def test_negative_cycle_remains_negative(self):
        signs = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        switches = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
            LocalSign.PRESERVE,
        )

        transformed = switch_cycle_signs(signs, switches)

        self.assertEqual(cycle_sign_product(signs), -1)
        self.assertEqual(cycle_sign_product(transformed), -1)

    def test_global_switch_changes_no_edge_signs(self):
        signs = (
            LocalSign.INVERT,
            LocalSign.PRESERVE,
            LocalSign.INVERT,
        )

        switches = (
            LocalSign.INVERT,
            LocalSign.INVERT,
            LocalSign.INVERT,
        )

        transformed = switch_cycle_signs(signs, switches)

        self.assertEqual(transformed, signs)

    def test_wrong_switch_count_is_rejected(self):
        signs = (
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
            LocalSign.PRESERVE,
        )

        switches = (
            LocalSign.PRESERVE,
        )

        with self.assertRaisesRegex(
            ValueError,
            "one local switch is required per junction",
        ):
            switch_cycle_signs(signs, switches)


if __name__ == "__main__":
    unittest.main()
