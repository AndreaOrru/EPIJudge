from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    words_position = {}
    min_distance = float('inf')

    for position, word in enumerate(paragraph):
        prev_position = words_position.get(word)
        if prev_position is not None:
            min_distance = min(min_distance, position - prev_position)
        words_position[word] = position

    return -1 if min_distance == float('inf') else min_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
