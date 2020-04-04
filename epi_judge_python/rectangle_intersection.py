import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    x = max(r1.x, r2.x)
    x_end = min(r1.x + r1.width, r2.x + r2.width)
    width = x_end - x

    y = max(r1.y, r2.y)
    y_end = min(r1.y + r1.height, r2.y + r2.height)
    height = y_end - y

    if width < 0 or height < 0:
        return Rect(0, 0, -1, -1)

    return Rect(x, y, width, height)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
