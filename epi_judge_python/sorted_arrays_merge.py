from typing import List

from test_framework import generic_test

from heapq import heappush, heappop


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    result = []
    min_heap = []
    array_iters = [iter(a) for a in sorted_arrays]

    for i, it in enumerate(array_iters):
        first_elem = next(it, None)
        if first_elem is not None:
            heappush(min_heap, (first_elem, i))

    while min_heap:
        smallest_elem, smallest_array_i = heappop(min_heap)
        smallest_array_iter = array_iters[smallest_array_i]
        result.append(smallest_elem)

        next_elem = next(smallest_array_iter, None)
        if next_elem is not None:
            heappush(min_heap, (next_elem, smallest_array_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
