import unittest
from pile_of_cubes.pile_of_cubes import *


class TestPileOfCubes(unittest.TestCase):
    def test_pile_of_cubes(self):
        self.assertEqual(pile_of_cube(1), 1)
        self.assertEqual(pile_of_cube(9), 2)
        self.assertEqual(pile_of_cube(36), 3)
        self.assertEqual(pile_of_cube(100), 4)
        self.assertEqual(pile_of_cube(4183059834009), 2022)
        self.assertEqual(pile_of_cube(24723578342962), -1)
        self.assertEqual(pile_of_cube(135440716410000), 4824)
        self.assertEqual(pile_of_cube(40539911473216), 3568)
        self.assertEqual(pile_of_cube(26825883955641), 3218)
