
def binarySearch(numbers, element):
  mid = int(numbers.__len__() / 2)
  if numbers.__len__() == 1 and numbers[0] != element:         
    return False
  
  if element == numbers[mid]:
    return True
  elif element < numbers[mid]:         
    return binarySearch(numbers[:mid], element)     
  else:         
    return binarySearch(numbers[mid:], element)
