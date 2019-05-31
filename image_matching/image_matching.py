
def countMatches(grid1, grid2):
  pass

def makeRegions(grid):
  regions = []
  for line_index, line in enumerate(grid):
    for bit in enumerate(line):
      if bit == '1':
        pass    

  pass


def getAdjacentsRegions(position, regions):
  for region in regions:
    for dot in region:
      pass


def isAdjacent(position1, position2):
  if (position2[0] - 1 == position1[0] and position2[1] == position1[1]) or \
    (position2[0] == position1[0] and position2[1] - 1 == position1[1]) or \
    (position2[0] == position1[0] and position2[1] + 1 == position1[1]) or \
    (position2[0] + 1 == position1[0] and position2[1] == position1[1]):
    return True
  return False