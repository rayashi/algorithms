
def left_rotation_recursion(elements, number_of_rotations):

    if number_of_rotations == 1:
        return elements[1:] + [elements[0]]

    return left_rotation_recursion(elements[1:] + [elements[0]], number_of_rotations - 1)


def left_rotation(elements, number_of_rotation):
    first = number_of_rotation % len(elements)
    return [elements[first]] + elements[first+1:] + elements[:first]