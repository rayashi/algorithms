import timeit
import unittest
from hourglass.hourglass import *


class TestHourglass(unittest.TestCase):
    def test_hourglass(self):
        matrix = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]
        self.assertEqual(hourglass(matrix), 19)

