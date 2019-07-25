def print_rangoli(size):
  alphas = 'abcdefghijklmnopqrstuvwxyz'
  right = list(alphas[:size])
  left = list(alphas[1:size])
  left.reverse()
  full_line = left + right
  line_size = len(full_line)*2-1

  bottom = []
  current_line = full_line
  for i in range(size-1):
    middle = len(current_line) // 2
    current_line = current_line[:middle] + current_line[middle+2:]
    bottom.append('-'.join(current_line).center(line_size, '-'))
  
  top = bottom.copy()
  top.reverse()

  print(*top, sep='\n')
  print(*full_line, sep='-')
  print(*bottom, sep='\n')

print_rangoli(26)