from typing import Iterator, List

from test_framework import generic_test

from heapq import heappushpop, heappush, heappop


def online_median(sequence: Iterator[int]) -> List[float]:
    medians = []
    lower_max_heap = []
    upper_min_heap = []

    for el in sequence:
        if len(lower_max_heap) <= len(upper_min_heap):
            heappush(lower_max_heap, -heappushpop(upper_min_heap, el))
        else:
            heappush(upper_min_heap, -heappushpop(lower_max_heap, -el))

        if len(lower_max_heap) == len(upper_min_heap):
            medians.append((-lower_max_heap[0] + upper_min_heap[0]) / 2)
        else:
            medians.append(-lower_max_heap[0])

    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
