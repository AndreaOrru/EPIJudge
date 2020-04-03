from typing import Iterator

from test_framework import generic_test

from collections import defaultdict


def majority_search(stream: Iterator[str]) -> str:
    candidate_count = 0

    for ch in stream:
        if candidate_count == 0:
            candidate = ch
            candidate_count = 1
        elif ch == candidate:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
