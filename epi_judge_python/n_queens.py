from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def attacked(row, col):
        for y in range(row):
            if col_placements[y] == col:
                return True
            if abs(col_placements[y] - col) == abs(y - row):
                return True
        return False

    def solve_queens(row):
        if row == n:
            results.append(col_placements.copy())
            return
        for col in range(n):
            if attacked(row, col):
                continue
            col_placements[row] = col
            solve_queens(row + 1)

    results = []
    col_placements = [0] * n
    solve_queens(0)
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
