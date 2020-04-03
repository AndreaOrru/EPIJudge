from test_framework import generic_test
from functools import lru_cache


@lru_cache(None)
def number_of_ways_lru(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return 1

    return number_of_ways(n - 1, m) + number_of_ways(n, m - 1)


def number_of_ways(n: int, m: int) -> int:
    n, m = min(n, m), max(n, m)
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]
    dp[1][1] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i > 1:
                dp[i % 2][j] = 0
            dp[i % 2][j] += dp[(i - 1) % 2][j]
            dp[i % 2][j] += dp[i % 2][j - 1]

    return dp[m % 2][n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
