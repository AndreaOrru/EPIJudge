from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def directed_generate_balanced_parentheses(n_left, n_right, prefix):
        if n_left == n_right == 0:
            result.append(prefix)
            return 

        if n_left > 0:
            directed_generate_balanced_parentheses(n_left - 1, n_right, prefix + '(')
        if n_right > n_left:
            directed_generate_balanced_parentheses(n_left, n_right - 1, prefix + ')')

    result = []
    directed_generate_balanced_parentheses(num_pairs, num_pairs, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
