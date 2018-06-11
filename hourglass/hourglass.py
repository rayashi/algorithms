
def sum_sub_matrix(matrix, initial_line, initial_column, size):
    waist = False
    sum = 0
    for line in range(initial_line, initial_line + size):
        if not waist:
            for column in range(initial_column, initial_column + size):
                try:
                    sum += matrix[line][column]
                except IndexError:
                    pass
        else:
            sum += matrix[line][initial_column+1]
        waist = not waist
    return sum


def hourglass(matrix):
    max_sum = -9**2
    for line in range(4):
        for column in range(4):
            sum = sum_sub_matrix(matrix, line, column, 3)
            if sum > max_sum:
                max_sum = sum
    return max_sum
