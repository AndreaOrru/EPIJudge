from typing import List

from test_framework import generic_test

from math import sqrt


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    n = len(partial_assignment)
    sub_n = int(sqrt(n))

    row_sets = [set() for _ in range(n)]
    col_sets = [set() for _ in range(n)]
    sub_sets = [[set() for _ in range(sub_n)] for _ in range(sub_n)]

    for y, row in enumerate(partial_assignment):
        for x, value in enumerate(row):
            if value and ((value in row_sets[y]) or 
                          (value in col_sets[x]) or
                          (value in sub_sets[y // sub_n][x // sub_n])):
                return False
            row_sets[y].add(value)
            col_sets[x].add(value)
            sub_sets[y // sub_n][x // sub_n].add(value)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
