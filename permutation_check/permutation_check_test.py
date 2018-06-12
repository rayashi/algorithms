import timeit
import unittest
from permutation_check.permutation_check import *


class TestPermutationCheck(unittest.TestCase):
    def test_test_permutation_check(self):
        self.assertEqual(permutation_check([4, 1, 3, 2]), 1)
        self.assertEqual(permutation_check([4, 1, 3]), 0)
        t = timeit.Timer(lambda: permutation_check([4, 1, 3, 2])).timeit(500)
        print('Permutation Check performance: %s' % t)

