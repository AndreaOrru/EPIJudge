from test_framework import generic_test


def gcd_fast(x: int, y: int) -> int:
    while y > 0:
        x, y = y, x % y
    return x


def gcd(x: int, y: int) -> int:
    power = 0

    while x != y:
        x, y = min(x, y), max(x, y)

        if x == 0:
            return y
        elif not x & 1 and not y & 1:
            x, y = x >> 1, y >> 1
            power += 1
        elif not x & 1 and y & 1:
            x, y = x >> 1, y
        elif x & 1 and not y & 1:
            x, y = x, y >> 1
        else:
            x, y = x, y - x

    return x << power


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))
