
def findSchedules(workHours, dayHours, pattern):
  schedules = []

  hoursLetf = getHoursLeft(workHours, pattern)
  numberOfEmptySlots = pattern.count('?')
  emptySlots = getEmptySlots(pattern)
  start = getMinStart(numberOfEmptySlots, dayHours, hoursLetf)

  possiblesHours = list(range(start, min(dayHours-start, hoursLetf)+1))

  combine(0, possiblesHours, [], numberOfEmptySlots)

  return schedules

def getHoursLeft(workHours, pattern):
  definedTotalHours = 0
  for hour in pattern:
    if hour != "?":
      definedTotalHours += int(hour)
  return int(workHours - definedTotalHours)

def getMinStart(emptySlots, dayHours, hoursLetf):
  minimum = hoursLetf - ((emptySlots-1) * dayHours)
  return minimum if minimum > 0 else 0

def getEmptySlots(pattern):
  return [i for i, x in enumerate(pattern) if x == "?"]

def fillEmptySlot(hours, position, week):
  l = list(week)
  l[position] = str(hours)
  return "".join(l)


def combine(pos, elements, current, length):
  if pos == length:
    print(current)
    return

  for e in elements:
    current[pos] = e
    combine(pos+1, elements, current, length)


schedules = findSchedules(3, 2, '??2??00')