
def collatz(n, progressions):

    l = [n]
    while l[len(l)-1] != 1:
        if l[len(l)-1] % 2 == 0:
            next_element = int(l[len(l)-1] / 2)
        else:
            next_element = int((3 * l[len(l)-1]) + 1)

        try:
            l += progressions[next_element]
            break
        except (KeyError, TypeError):
            l += [next_element]
    return l


def longest_progression(n):
    progressions = {}
    longest = 0
    steps = 0
    for i in range(n, 0, -1):
        progressions[i] = collatz(i, progressions)
        if len(progressions[i]) > steps:
            steps = len(progressions[i])
            longest = progressions[i][0]

    return longest
