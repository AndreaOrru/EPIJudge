from test_framework import generic_test

from collections import defaultdict, Counter


def can_form_palindrome_raw(s: str) -> bool:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    odds = 0
    for count in counts.values():
        if count % 2 == 1:
            odds += 1

    return odds <= 1


def can_form_palindrome(s: str) -> bool:
    return sum(count % 2 for count in Counter(s).values()) <= 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
