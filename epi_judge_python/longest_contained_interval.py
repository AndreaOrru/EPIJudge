from typing import List

from test_framework import generic_test


def longest_contained_range_sort(A: List[int]) -> int:
    A.sort()
    current = longest = 1

    for i in range(len(A) - 1):
        if A[i + 1] - A[i] == 1:
            current += 1
        elif A[i + 1] - A[i] != 0:
            current = 1
        longest = max(longest, current)

    return longest


def longest_contained_range(A: List[int]) -> int:
    elements = set(A)  # O(n) time, space
    longest = 0

    # O(n)
    while elements:
        pivot = elements.pop()
        current = 1

        candidate = pivot + 1
        while candidate in elements:
            elements.remove(candidate)
            candidate, current = candidate + 1, current + 1

        candidate = pivot - 1
        while candidate in elements:
            elements.remove(candidate)
            candidate, current = candidate - 1, current + 1
        
        longest = max(longest, current)

    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
