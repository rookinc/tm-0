import unittest

from tm0.carrier_register import InternalRegister
from tm0.continuity import (
    begin_null_trace,
    continues,
    extend_trace,
)


class TestContinuityWithoutIdentity(unittest.TestCase):
    def test_trace_begins_at_null(self):
        trace = begin_null_trace()

        self.assertEqual(trace.current, InternalRegister.NULL)
        self.assertEqual(
            trace.states,
            (InternalRegister.NULL,),
        )

    def test_characterization_extends_null_trace(self):
        earlier = begin_null_trace()
        later = extend_trace(
            earlier,
            InternalRegister.CHARACTERIZED,
        )

        self.assertTrue(continues(earlier, later))
        self.assertEqual(
            later.states,
            (
                InternalRegister.NULL,
                InternalRegister.CHARACTERIZED,
            ),
        )

    def test_return_to_null_preserves_continuity(self):
        start = begin_null_trace()
        characterized = extend_trace(
            start,
            InternalRegister.CHARACTERIZED,
        )
        returned = extend_trace(
            characterized,
            InternalRegister.NULL,
        )

        self.assertTrue(continues(start, returned))
        self.assertTrue(continues(characterized, returned))
        self.assertEqual(returned.current, InternalRegister.NULL)

    def test_identity_transition_does_not_extend_trace(self):
        trace = begin_null_trace()

        with self.assertRaisesRegex(
            ValueError,
            "identity transition does not extend continuity",
        ):
            extend_trace(trace, InternalRegister.NULL)

    def test_divergent_histories_do_not_continue_each_other(self):
        start = begin_null_trace()
        characterized = extend_trace(
            start,
            InternalRegister.CHARACTERIZED,
        )
        returned = extend_trace(
            characterized,
            InternalRegister.NULL,
        )

        self.assertFalse(continues(returned, characterized))

    def test_identical_histories_remain_extensionally_equal(self):
        first = extend_trace(
            begin_null_trace(),
            InternalRegister.CHARACTERIZED,
        )
        second = extend_trace(
            begin_null_trace(),
            InternalRegister.CHARACTERIZED,
        )

        self.assertEqual(first, second)
        self.assertIsNot(first, second)

    def test_continuity_preserves_lineage_not_plurality(self):
        first = extend_trace(
            begin_null_trace(),
            InternalRegister.CHARACTERIZED,
        )
        second = extend_trace(
            begin_null_trace(),
            InternalRegister.CHARACTERIZED,
        )

        catalogue = {first, second}

        self.assertEqual(len(catalogue), 1)


if __name__ == "__main__":
    unittest.main()
