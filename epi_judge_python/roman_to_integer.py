from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = values[s[-1]]

    for i, c in enumerate(s[:-1]):
        result += -values[c] if values[c] < values[s[i + 1]] else values[c]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
