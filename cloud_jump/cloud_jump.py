def jumpingOnClouds(c):
  jumps = 0
  current = 0

  while current < len(c) - 1 :

    if current + 2 < len(c) and c[current+2] == '0':
      jumps += 1
      current += 2
    else:
      jumps += 1
      current += 1

  return jumps

print(jumpingOnClouds(['0', '0', '0', '1', '0', '0']))