from typing import List

from test_framework import generic_test

from collections import deque


def fill_surrounded_regions(board: List[List[str]]) -> None:
    h, w = len(board), len(board[0])
    queue = deque()

    for x in range(w):
        queue.extend([(0, x), (h - 1, x)])
    for y in range(1, h - 1):
        queue.extend([(y, 0), (y, w - 1)])

    while queue:
        y, x = queue.popleft()
        if 0 <= y < h and 0 <= x < w and board[y][x] == 'W':
            board[y][x] = 'V'
            queue.extend([(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)])

    for y in range(h):
        for x in range(w):
            board[y][x] = 'B' if board[y][x] != 'V' else 'W'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
