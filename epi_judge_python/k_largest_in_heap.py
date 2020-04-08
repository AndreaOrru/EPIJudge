from typing import List

from test_framework import generic_test, test_utils


from collections import namedtuple
from heapq import heappush, heappop


Candidate = namedtuple('Candidate', ('value', 'index'))


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    result = []

    candidate_max_heap = [Candidate(-A[0], 0)]
    for _ in range(k):
        candidate_idx = candidate_max_heap[0].index
        result.append(-heappop(candidate_max_heap).value)

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heappush(candidate_max_heap, Candidate(-A[left_child_idx], left_child_idx))

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heappush(candidate_max_heap, Candidate(-A[right_child_idx], right_child_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
