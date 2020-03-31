from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    max_sum = 0
    curr_sum = 0

    for el in A:
        curr_sum = max(el, curr_sum + el)
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
