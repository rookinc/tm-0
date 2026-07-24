import unittest

from tm0.null import Null


class TestNull(unittest.TestCase):

    def test_null_exists(self):
        self.assertEqual(repr(Null()), "Null()")


if __name__ == "__main__":
    unittest.main()
