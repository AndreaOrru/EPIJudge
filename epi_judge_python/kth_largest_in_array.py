from typing import List

from test_framework import generic_test

from heapq import heappush, heappop, nsmallest

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest_heap(k: int, A: List[int]) -> int:
    min_heap = []
    for el in A:
        heappush(min_heap, el)
        if len(min_heap) > k:
            heappop(min_heap)

    return nsmallest(k, min_heap)[-k]


################################################################

from random import randint


def partition(A: List[int], left: int, right: int, pivot_index: int) -> int:
    pivot = A[pivot_index]

    A[right], A[pivot_index] = A[pivot_index], A[right]
    pivot_index, right = right, right - 1

    while left <= right:
        while left <= right and A[left] > pivot:
            left += 1
        while left <= right and A[right] < pivot:
            right -= 1
        if left < right:
            A[left], A[right] = A[right], A[left]
            left, right = left + 1, right - 1

    A[left], A[pivot_index] = A[pivot_index], A[left]
    return left


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    left, right = 0, len(A) - 1

    while left <= right:
        pivot_index = randint(left, right)
        pivot_index = partition(A, left, right, pivot_index)

        if pivot_index == k - 1:
            return A[pivot_index]
        elif pivot_index < k - 1:
            left = pivot_index + 1
        elif pivot_index > k - 1:
            right = pivot_index - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
