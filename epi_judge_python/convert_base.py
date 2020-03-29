from test_framework import generic_test


def char_to_num(char: str) -> int:
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    elif 'A' <= char <= 'F':
        return ord(char) - ord('A') + 10
    return None


def num_to_char(num: int) -> str:
    if 0 <= num <= 9:
        return chr(ord('0') + num)
    elif 10 <= num <= 15:
        return chr(ord('A') + num - 10)
    return None


def str_to_num(string: str, base: int) -> int:
    number = 0

    for power, char in enumerate(reversed(string)):
        if char in ('+', '-'):
            break
        digit = char_to_num(char)
        number += digit * (base ** power)

    return -number if string[0] == '-' else number


def num_to_str(number: int, base: int) -> str:
    negative = number < 0
    number = -number if negative else number

    result = []
    while True:
        result.append(num_to_char(number % base))
        number //= base
        if number == 0:
            break

    if negative:
        result.append('-')

    return ''.join(reversed(result))


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    number = str_to_num(num_as_string, b1)
    return num_to_str(number, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
