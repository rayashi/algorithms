import unittest
from passing_cars.passing_cars import *


class TestPassingCars(unittest.TestCase):

    def test_passing_cars(self):
        self.assertEqual(fast_passing_cars([0, 1, 0, 1, 1]), 5)

