from typing import List

from test_framework import generic_test

from sortedcontainers import SortedSet
from math import sqrt


class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)

    def __hash__(self):
        return self.a ^ self.b


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    result = []
    candidates = SortedSet([Number(0, 0)])

    while len(result) < k:
        smallest = candidates.pop(0)
        result.append(smallest.val)

        candidates.add(Number(smallest.a + 1, smallest.b))
        candidates.add(Number(smallest.a, smallest.b + 1))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
