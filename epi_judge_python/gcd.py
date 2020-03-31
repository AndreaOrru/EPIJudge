from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    while y > 0:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))
