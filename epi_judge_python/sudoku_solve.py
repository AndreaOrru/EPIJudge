import copy
import functools
import math
from typing import List, Tuple, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from math import sqrt


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def find_empty_cell(cell_idx: int) -> Tuple[int, int]:
        for i in range(cell_idx, n * n):
            y, x = i // n, i % n
            if partial_assignment[y][x] == 0:
                return y, x
        return None, None

    def possible_values(y: int, x: int) -> Set[int]:
        result = {v for v in range(1, n + 1)}

        for val in range(1, n + 1)
        for i in range(n):
            if partial_assignment[y][i]:
                result.discard(partial_assignment[y][i])
            if partial_assignment[i][x]:
                result.discard(partial_assignment[i][x])

        sub_square_y = (y // sub_n) * sub_n
        sub_square_x = (x // sub_n) * sub_n

        for i in range(sub_square_y, sub_square_y + sub_n):
            for j in range(sub_square_x, sub_square_x + sub_n):
                if partial_assignment[i][j]:
                    result.discard(partial_assignment[i][j])

        return result

    def partial_solve_sudoku(cell_idx: int) -> bool:
        y, x = find_empty_cell(cell_idx)
        if (y, x) == (None, None):
            return True

        for candidate in possible_values(y, x):
            partial_assignment[y][x] = candidate
            if partial_solve_sudoku(y * n + x + 1):
                return True

        partial_assignment[y][x] = 0
        return False

    n = len(partial_assignment)
    sub_n = int(sqrt(n))

    return partial_solve_sudoku(0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
