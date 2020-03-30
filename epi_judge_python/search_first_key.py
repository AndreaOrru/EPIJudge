from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if k < A[mid]:
            right = mid - 1
        elif k > A[mid]:
            left = mid + 1
        else:
            if mid == 0 or A[mid - 1] != k:
                return mid
            else:
                right = mid - 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
