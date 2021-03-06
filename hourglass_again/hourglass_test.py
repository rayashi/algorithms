import unittest
from hourglass_again.hourglass import *


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
        matrix = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 9, 2, -4, -4, 0],
            [0, 0, 0, -2, 0, 0],
            [0, 0, -1, -2, -4, 0],
        ]
        self.assertEqual(hourglass(matrix), 13)
        matrix = [
            [-1, -1, 0, -9, -2, -2],
            [-2, -1, -6, -8, -2, -5],
            [-1, -1, -1, -2, -3, -4],
            [-1, -9, -2, -4, -4, -5],
            [-7, -3, -3, -2, -9, -9],
            [-1, -3, -1, -2, -4, -5],
        ]
        self.assertEqual(hourglass(matrix), -6)

    def test_sum_hourglass(self):
        matrix = [[2, 4, 4], [1, 2, 4], [1, 2, 4]]
        self.assertEqual(sum_hourglass(matrix), 19)

    def test_get_hourglass(self):
        matrix = [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]
        ]
        result = [
            [1, 0, 0],
            [2, 4, 4],
            [0, 2, 0]
        ]
        self.assertEqual(get_hourglass(2, 2, matrix), result)
        self.assertEqual(get_hourglass(2, 4, matrix), None)
