from test_framework import generic_test


def is_palindrome_number_str(x: int) -> bool:
    str_x = str(x)

    left, right = 0, len(str_x) - 1
    while left <= right:
        if str_x[left] != str_x[right]:
            return False
        left, right = left + 1, right - 1
    return True


from math import log10, floor

def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0

    n_digits = floor(log10(x)) + 1
    msd_mask = 10 ** (n_digits - 1)

    for _ in range(n_digits // 2):
        msd, lsd = x // msd_mask, x % 10
        if msd != lsd:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
