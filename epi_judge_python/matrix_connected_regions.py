from typing import List

from test_framework import generic_test

from collections import deque


def flip_color_rec(x: int, y: int, image: List[List[bool]]) -> None:
    def flip_color_helper(x: int, y: int) -> None:
        if not 0 <= x < len(image):
            return
        if not 0 <= y < len(image[0]):
            return
        if image[x][y] != orig_color:
            return

        image[x][y] = not orig_color

        flip_color_helper(x + 1, y)
        flip_color_helper(x - 1, y)
        flip_color_helper(x, y + 1)
        flip_color_helper(x, y - 1)

    orig_color = image[x][y]
    flip_color_helper(x, y)


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    orig_color = image[x][y]

    queue = deque([(x, y)])
    image[x][y] = not orig_color

    while queue:
        x, y = queue.popleft()
        for next_x, next_y in ((x + 1, y), (x - 1, y),
                               (x, y + 1), (x, y - 1)):
            if (0 <= next_x < len(image) and
                0 <= next_y < len(image[0]) and 
                image[next_x][next_y] == orig_color):
                   image[next_x][next_y] = not orig_color
                   queue.append((next_x, next_y))



def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
