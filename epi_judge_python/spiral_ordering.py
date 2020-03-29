from typing import List

from test_framework import generic_test


def spiral_order_rec(M, y, x, size, is_top_left):
    if size == 0:
        return []
    
    result = []
    mul = 1 if is_top_left else -1

    for i in range(size):
        result.append(M[y][x + i*mul])
    for j in range(1, size):
        result.append(M[y + j*mul][x + i*mul])

    y += (size - 1) * mul
    x += (size - 2) * mul

    return result + spiral_order_rec(M, y, x, size - 1, not is_top_left)


def spiral_order(M):
    result = []

    size = len(M)
    y = x = 0
    mul = 1

    while size:
        for i in range(size):
            result.append(M[y][x + i*mul])
        for j in range(1, size):
            result.append(M[y + j*mul][x + i*mul])

        y += (size - 1) * mul
        x += (size - 2) * mul

        mul = -mul
        size -= 1

    return result


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    return spiral_order(square_matrix)
    #return spiral_order(square_matrix, 0, 0, len(square_matrix), True)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
