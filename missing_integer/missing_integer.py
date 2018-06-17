
def missing_integer(numbers):
    nexts = {}
    for number in numbers:
        if number >= 0:
            nexts[number] = number + 1
        else:
            nexts[number] = 1

    result = None

    try:
        nexts[1]
    except KeyError:
        return 1

    for number in numbers:
        if number >= 0:
            missing = number + 1
        else:
            missing = 1
        try:
            nexts[missing]
        except KeyError:
            if not result or missing < result:
                result = missing
    return result
