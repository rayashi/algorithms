import unittest
from count_divisibles.count_divisible import *


class TestCountDivisible(unittest.TestCase):

    def test_count_divisible(self):
        self.assertEqual(count_divisible(6, 11, 2), 3)
        self.assertEqual(count_divisible(0, 0, 11), 1)
        self.assertEqual(count_divisible(0, 14, 2), 8)
        self.assertEqual(faster_count_divisible(6, 11, 2), 3)
        self.assertEqual(faster_count_divisible(0, 0, 11), 1)
        self.assertEqual(faster_count_divisible(0, 14, 2), 8)
