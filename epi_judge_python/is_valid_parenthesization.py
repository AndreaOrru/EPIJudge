from test_framework import generic_test


INVERSE = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def is_well_formed(s: str) -> bool:
    stack = []

    for p in s:
        if p in ('(', '[', '{'):
            stack.append(INVERSE[p])
        elif not stack or p != stack.pop():
            return False

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
