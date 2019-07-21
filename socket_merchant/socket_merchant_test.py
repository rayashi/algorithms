import unittest
from .socket_merchant import get_total_machring_pairs


class TestSocketMerchant(unittest.TestCase):
    def test_socket_merchant(self):
        self.assertEqual(get_total_machring_pairs([10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)
        self.assertEqual(get_total_machring_pairs([1, 2, 1, 2, 1, 3, 2]), 2)
        self.assertEqual(get_total_machring_pairs([1, 2, 1, 2, 1, 3, 1]), 3)
