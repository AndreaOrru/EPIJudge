import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    last_word_length_at = [-1] * len(domain)

    for i in range(len(domain)):
        # Word in dictionary.
        word = domain[:i + 1]
        if word in dictionary:
            last_word_length_at[i] = i + 1
            continue

        # Word composed by dictionary words.
        for j in range(i):
            word = domain[j + 1: i + 1]
            if last_word_length_at[j] != -1 and word in dictionary:
                last_word_length_at[i] = i - j

    if last_word_length_at[i] == -1:
        return []

    decomposition = []
    i = len(domain) - 1

    while i >= 0:
        word = domain[i - last_word_length_at[i] + 1: i + 1]
        decomposition.append(word)
        i -= last_word_length_at[i]

    return decomposition[::-1]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
