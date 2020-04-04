from test_framework import generic_test
from math import isclose


def square_root(x: float) -> float:
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not isclose(left, right):
        mid = (left + right) / 2
        mid_squared = mid * mid

        if mid_squared < x:
            left = mid
        else:
            right = mid

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
