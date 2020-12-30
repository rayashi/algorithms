import unittest
from datetime_difference.datetime_difference import *


class TestDateTimeDifference(unittest.TestCase):
    def test_hourglass(self):
        t1 = 'Sun 10 May 2015 13:54:36 -0700'
        t2 = 'Sun 10 May 2015 13:54:36 -0000'
        self.assertEqual(datetime_difference(t1, t2), '25200')

        t1 = 'Sat 02 May 2015 19:54:36 +0530'
        t2 = 'Fri 01 May 2015 13:54:36 -0000'
        self.assertEqual(datetime_difference(t1, t2), '88200')

