
def pile_of_cube(m):
    n = 1
    incremental_result = 0
    while incremental_result < m:
        incremental_result += n**3
        n += 1

    if incremental_result > m:
        return -1
    return n - 1

