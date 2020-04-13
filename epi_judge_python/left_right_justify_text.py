from typing import List

from test_framework import generic_test
from math import ceil


def justify_text(words: List[str], L: int) -> List[str]:
    result = []
    curr_line, curr_line_len = [], 0

    for word in words:
        if curr_line_len + len(word) + len(curr_line) > L:
            for i in range(L - curr_line_len):
                curr_line[i % max(len(curr_line) - 1, 1)] += ' '
            result.append(''.join(curr_line))
            curr_line, curr_line_len = [], 0
        curr_line.append(word)
        curr_line_len += len(word)

    return result + [' '.join(curr_line).ljust(L)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('left_right_justify_text.py',
                                       'left_right_justify_text.tsv',
                                       justify_text))
