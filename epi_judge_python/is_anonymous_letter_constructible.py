from test_framework import generic_test

from collections import defaultdict


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_count = defaultdict(int)
    for ch in letter_text:
        letter_count[ch] += 1
        
    for ch in magazine_text:
        if ch not in letter_count:
            continue
        letter_count[ch] -= 1
        if letter_count[ch] == 0:
            del letter_count[ch]
            if not letter_count:
                return True

    return not letter_count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
