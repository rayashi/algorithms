import unittest
from image_matching.image_matching import *


class TestMissingInterger(unittest.TestCase):
    def test_countMatches(self):
        self.assertEqual(countMatches(['001', '011', '100'], ['001', '011', '101']), None)
        self.assertEqual(countMatches(['111', '100', '100'], ['111', '100', '101']), None)

    def test_is_adjacent(self):
        self.assertEqual(isAdjacent((1,1),(0,0)), False)
        self.assertEqual(isAdjacent((1,1),(0,1)), True)
        self.assertEqual(isAdjacent((1,1),(0,2)), False)
        self.assertEqual(isAdjacent((1,1),(1,2)), True)
        self.assertEqual(isAdjacent((1,1),(2,0)), False)
        self.assertEqual(isAdjacent((1,1),(2,1)), True)
        self.assertEqual(isAdjacent((1,1),(2,2)), False)