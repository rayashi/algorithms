import unittest
from .left_rotation import left_rotation


class TestLeftRotation(unittest.TestCase):
    def test_left_rotation(self):
        self.assertEqual(left_rotation([1, 2, 3, 4, 5], 4), [5, 1, 2, 3, 4])
