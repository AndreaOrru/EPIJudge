from typing import List

from test_framework import generic_test, test_utils

from collections import defaultdict


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams = defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagrams.values()
        if len(group) >= 2
    ]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
