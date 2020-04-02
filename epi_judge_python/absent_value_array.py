from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from itertools import tee


def find_missing_element(stream: Iterator[int]) -> int:
    n_buckets = 1 << 16
    counters = [0] * n_buckets
    stream, stream_copy = tee(stream)

    for ip in stream:
        upper_part_ip = ip >> 16
        counters[upper_part_ip] += 1
    
    bucket_capacity = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counters)
                            if c < bucket_capacity)

    candidates = [0] * bucket_capacity
    for ip in stream_copy:
        lower_part_ip = ip & 0xFFFF
        candidates[lower_part_ip] = 1

    return next(i for i, present in enumerate(candidates)
                if not present)


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
