from typing import Set

from test_framework import generic_test

from collections import deque, defaultdict
from string import ascii_lowercase


def transform_string(D: Set[str], s: str, t: str) -> int:
    D.remove(s)
    queue = deque([(0, s)])

    while queue:
        depth, curr_str = queue.popleft()
        if curr_str == t:
            return depth

        for i in range(len(curr_str)):
            for c in ascii_lowercase:
                candidate = curr_str[:i] + c + curr_str[i + 1:]
                if candidate in D:
                    D.remove(candidate)
                    queue.append((depth + 1, candidate))

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
