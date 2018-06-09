def tape_equilibrium(numbers):
    total = 0
    for n in numbers:
        total += n

    left = numbers[0]
    right = total - left
    minimal_difference = abs(left - right)
    for p in range(1, len(numbers) - 1):
        left += numbers[p]
        right = total - left
        diference = abs(left - right)
        if diference < minimal_difference:
            minimal_difference = diference

    return minimal_difference
