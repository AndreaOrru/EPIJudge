import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd_storage(A: List[int]) -> None:
    result = []

    for el in A:
        if el % 2 == 0:
            result.append(el)
    for el in A:
        if el % 2 == 1:
            result.append(el)
    for i, el in enumerate(result):
        A[i] = el


def even_odd(A: List[int]) -> None:
    next_even = 0
    next_odd = len(A) - 1

    while True:
        while next_even < next_odd and A[next_even] % 2 == 0:
            next_even += 1
        while next_even < next_odd and A[next_odd] % 2 == 1:
            next_odd -= 1

        if next_even >= next_odd:
            break
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_even += 1
            next_odd -= 1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
