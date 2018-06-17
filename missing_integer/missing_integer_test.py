import unittest
from missing_integer.missing_integer import *


class TestMissingInterger(unittest.TestCase):

    def test_missing_integer(self):
        self.assertEqual(missing_integer([1, 2, 3]), 4)
        self.assertEqual(missing_integer([-1, -3]), 1)
        self.assertEqual(missing_integer([3]), 1)
