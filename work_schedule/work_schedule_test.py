import unittest
from work_schedule.work_schedule import *


class TestFindSchedules(unittest.TestCase):
  def test_findSchedules(self):
    schedules = findSchedules(56, 8, '???8???')
    self.assertEqual(schedules, ['8888888'])
    schedules = findSchedules(3, 2, '??2??00')
    print(schedules)
    self.assertEqual(schedules, ['0020100','0021000','0120000','1020000'])
    
  def test_getHoursLeft(self):
    self.assertEqual(getHoursLeft(56, '???8???'), 48)

  def test_getMinStart(self):
    self.assertEqual(getMinStart(6, 8, 48), 8)
    self.assertEqual(getMinStart(2, 4, 4), 0)