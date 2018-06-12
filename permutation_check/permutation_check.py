
def permutation_check(numbers):
    increments = {}
    for number in numbers:
        increments[number] = number + 1

    for number in numbers:
        try:
            increments[number+1]
        except KeyError:
            if number != len(numbers):
                return 0
    return 1
