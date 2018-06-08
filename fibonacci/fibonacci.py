def recursive_fibo(n):
    if n < 0:
        raise TypeError
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return recursive_fibo(n - 1) + recursive_fibo(n - 2)


def memoized_fibo(n, memo=None):
    if n < 0:
        raise TypeError

    if memo is None:
        memo = (n+1) * [None]

    if memo[n] is not None:
        return memo[n]

    if n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        result = memoized_fibo(n-1, memo) + memoized_fibo(n-2, memo)

    memo[n] = result
    return result


def bottom_up_fibo(n):
    if n < 0:
        raise TypeError
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    results = [0, 1, 1]
    for i in range(3, n+1):
        results.append(results[i-1] + results[i-2])
    return results[n]
