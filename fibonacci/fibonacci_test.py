import timeit
import unittest
from fibonacci.fibonacci import *


class TestFibonacci(unittest.TestCase):
    def test_recusive_fibonacci(self):
        self.assertEqual(recursive_fibo(0), 0)
        self.assertEqual(recursive_fibo(5), 5)
        self.assertEqual(recursive_fibo(10), 55)
        self.assertEqual(recursive_fibo(20), 6765)
        self.assertRaises(TypeError, recursive_fibo, -1)
        t = timeit.Timer(lambda: recursive_fibo(20)).timeit(500)
        print('Fibonacci recursive performance: %s' % t)

    def test_memoized_fibonacci(self):
        self.assertEqual(memoized_fibo(0), 0)
        self.assertEqual(memoized_fibo(5), 5)
        self.assertEqual(memoized_fibo(10), 55)
        self.assertEqual(memoized_fibo(20), 6765)
        self.assertRaises(TypeError, memoized_fibo, -1)
        t = timeit.Timer(lambda: memoized_fibo(20)).timeit(500)
        print('Fibonacci memoized performance: %s' % t)

    def test_bottom_up_fibonacci(self):
        self.assertEqual(bottom_up_fibo(0), 0)
        self.assertEqual(bottom_up_fibo(5), 5)
        self.assertEqual(bottom_up_fibo(10), 55)
        self.assertEqual(bottom_up_fibo(20), 6765)
        self.assertRaises(TypeError, bottom_up_fibo, -1)
        t = timeit.Timer(lambda: bottom_up_fibo(20)).timeit(500)
        print('Fibonacci bottom up performance: %s' % t)
