from test_framework import generic_test


def square_root_brute_force(k: int) -> int:
    n = 0
    while (n * n) <= k:
        n += 1
    return n if (n * n) == k else n - 1


def square_root(k: int) -> int:
    lower, upper = 0, k

    while lower <= upper:
        mid = (lower + upper) // 2
        mid_squared = mid * mid

        if k < mid_squared:
            upper = mid - 1
        elif k > mid_squared:
            lower = mid + 1
        else:
            return mid

    return lower - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
