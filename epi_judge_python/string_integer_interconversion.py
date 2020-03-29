from test_framework import generic_test
from test_framework.test_failure import TestFailure


def num_to_char(digit: int) -> str:
    return chr(ord('0') + digit)


def char_to_num(char: str) -> int:
    return ord(char) - ord('0')


def int_to_string(x: int) -> str:
    result = []
    negative = x < 0
    x = -x if negative else x

    while True:
        result.append(num_to_char(x % 10))
        x //= 10
        if x == 0:
            break

    if negative:
        result.append('-')

    return ''.join(reversed(result))


def string_to_int(s: str) -> int:
    result = 0

    for power, ch in enumerate(reversed(s)):
        if ch in ('+', '-'):
            break
        digit = char_to_num(ch)
        result += digit * (10 ** power)

    return -result if s[0] == '-' else result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
