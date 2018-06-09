import timeit
import unittest
from tape_equilibrium.tape_equilibrium import *


class TestTapeEquilibrium(unittest.TestCase):
    def test_tape_equilibrium(self):
        self.assertEqual(tape_equilibrium([3, 1, 2, 4, 3]), 1)
        self.assertEqual(tape_equilibrium([3, 1, 4]), 0)
        self.assertEqual(tape_equilibrium([-1000, 1000]), 2000)
        self.assertEqual(tape_equilibrium([0]), 0)
        t = timeit.Timer(lambda: tape_equilibrium(10*[3, 1, 2, 4, 3])).timeit(500)
        print('Tape Equilibrium performance: %s' % t)

