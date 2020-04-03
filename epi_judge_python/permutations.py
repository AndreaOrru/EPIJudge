from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def perform_permutations(start: int):
        if start == len(A) - 1:
            result.append(A.copy())

        for i in range(start, len(A)):
            A[start], A[i] = A[i], A[start]
            perform_permutations(start + 1)
            A[i], A[start] = A[start], A[i]

    result = []
    perform_permutations(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
