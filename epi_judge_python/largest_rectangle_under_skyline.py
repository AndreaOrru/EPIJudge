from typing import List

from test_framework import generic_test


def calculate_largest_rectangle(heights: List[int]) -> int:
    pillar_indexes = []
    max_rect_area = 0

    for i, h in enumerate(heights + [0]):
        while pillar_indexes and heights[pillar_indexes[-1]] >= h:
            height = heights[pillar_indexes.pop()]
            width = i if not pillar_indexes else i - pillar_indexes[-1] - 1
            max_rect_area = max(max_rect_area, height * width)
        pillar_indexes.append(i)

    return max_rect_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('largest_rectangle_under_skyline.py',
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
