
def hourglass(matrix):
    result = 9*7*-1
    for i in range(4):
        for j in range(4):
            sub = get_hourglass(i, j, matrix)
            sum = sum_hourglass(sub)
            if sum > result:
                result = sum

    return result


def sum_hourglass(matrix):
    sum = 0
    for i in range(3):
        sum += matrix[0][i]
    for i in range(3):
        sum += matrix[2][i]
    sum += matrix[1][1]
    return sum


def get_hourglass(i, j, matrix):
    if i > 3 or j > 3:
        return None
    return [
        matrix[i][j:j + 3],
        matrix[i + 1][j:j + 3],
        matrix[i + 2][j:j + 3]
    ]

