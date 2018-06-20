
def count_divisible(a, b, k):
    count = 0
    first = None

    if k > b != 0:
        return 0

    for i in range(a, b+1):
        if i % k == 0:
            first = i
            count += 1
            break

    if first is None:
        return 0

    for i in range(first+k, b+1, k):
        count += 1

    return count


def faster_count_divisible(a, b, k):
    count = 0
    first = None
    last = None

    if k > b != 0:
        return 0

    for i in range(a, b+1):
        if i % k == 0:
            first = i
            count += 1
            break

    for i in range(b, a-1, -1):
        if i % k == 0:
            last = i
            count += 1
            break

    if first is None:
        return 0

    if first == last:
        return 1

    return 2 + ((last - first)/k) - 1
