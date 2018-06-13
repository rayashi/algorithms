
import unittest
from collatz.collatz import *


class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual(longest_progression(10), 9)
        self.assertEqual(longest_progression(100), 97)
        self.assertEqual(longest_progression(1000), 871)
        self.assertEqual(longest_progression(10000), 6171)
        self.assertEqual(longest_progression(100000), 77031)
        self.assertEqual(longest_progression(1000000), 837799)


