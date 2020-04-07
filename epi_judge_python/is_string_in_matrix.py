from typing import List

from test_framework import generic_test

from functools import lru_cache


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    def find_adjacent(y, x):
        return [(y, x) for y, x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
                if 0 <= y < len(grid) and
                   0 <= x < len(grid[0])]

    @lru_cache(None)
    def search_pattern(y, x, pattern_idx):
        if pattern_idx == len(pattern):
            return True
        for y1, x1 in find_adjacent(y, x):
            if grid[y1][x1] == pattern[pattern_idx]:
                if search_pattern(y1, x1, pattern_idx + 1):
                    return True
        return False

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == pattern[0]:
                if search_pattern(y, x, 1):
                    return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
