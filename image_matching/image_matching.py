
def countMatches(grid1, grid2):
  count = 0
  regions1 = makeRegions(grid1)
  regions2 = makeRegions(grid2)
  for reg1 in regions1:
    for reg2 in regions2:
      if reg1 == reg2:
        count += 1
  return count


def makeRegions(grid):
  regions = []
  for line_index, line in enumerate(grid):
    for colunm_index, bit in enumerate(line):
      if bit == '1':
        regions = getAdjacentsRegions((line_index, colunm_index), regions)
  return regions


def getAdjacentsRegions(position, regions):
  if not regions:
    return [{ position }]
  adjacents_regions = []

  # Find adjacents regions
  for region_index, region in enumerate(regions):
    for dot in region:
      if isAdjacent(position, dot):
        adjacents_regions.append(region_index) 
        break

  if adjacents_regions:
    return mergeAdjacentsRegions(regions, adjacents_regions, position)
  else:
    return regions + [{position}] 


def mergeAdjacentsRegions(regions, adjacents_regions, position):
  new_region = set()
  for adjacent_region in adjacents_regions:
    new_region.update(regions[adjacent_region])
  
  new_region.add(position)
  new_regions = [x for i,x in enumerate(regions) if i not in adjacents_regions]
  new_regions.append(new_region)
  return new_regions


def isAdjacent(position1, position2):
  if (position2[0] - 1 == position1[0] and position2[1] == position1[1]) or \
    (position2[0] == position1[0] and position2[1] - 1 == position1[1]) or \
    (position2[0] == position1[0] and position2[1] + 1 == position1[1]) or \
    (position2[0] + 1 == position1[0] and position2[1] == position1[1]):
    return True
  return False