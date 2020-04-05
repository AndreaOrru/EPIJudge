import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import OrderedDict
from itertools import islice

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    subarray = Subarray(-1, -1)
    keyword_positions = OrderedDict()

    for i, word in enumerate(paragraph):
        if word in keywords:
            keyword_positions[word] = i
            keyword_positions.move_to_end(word)

        if len(keyword_positions) == len(keywords):
            first = next(islice(keyword_positions.values(), 1))
            if subarray == (-1, -1) or (i - first) < (subarray.end - subarray.start):
                subarray = Subarray(first, i)

            del keyword_positions[paragraph[first]]

    return subarray


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
