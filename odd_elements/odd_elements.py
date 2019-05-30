
def odd_elements(array):

    counts = {}

    for e in array:
        try:
            counts[e] += 1
        except KeyError:
            counts[e] = 1

    for i in counts:
        if counts[i] == 1:
            print(i)


odd_elements(['a','b','c','d','f','a','b'])
