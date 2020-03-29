import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove_additional_storage(size: int, s: List[str]) -> int:
    result = []

    operations = 0
    i = 0
    while i < len(s) and s[i] != '' and operations < size:
        if s[i] == 'a':
            result.extend(['d', 'd'])
            operations += 1
        elif s[i] == 'b':
            operations += 1
        else:
            result.append(s[i])
        i += 1

    s[:len(result)] = result
    return len(result)


def remove_bs(size: int, s: List[str]) -> int:
    num_a = num_b = 0
    insert = 0

    for look in range(size):
        if s[look] == 'b':
            num_b += 1
        else:
            if s[look] == 'a':
                num_a += 1
            s[insert] = s[look]
            insert += 1

    return num_a, num_b


def replace_and_remove(size: int, s: List[str]) -> int:
    num_a, num_b = remove_bs(size, s)
    
    look = size - num_b - 1
    insert = look + num_a

    while look >= 0:
        if s[look] == 'a':
            s[insert] = s[insert - 1] = 'd'
            insert -= 2
        else:
            s[insert] = s[look]
            insert -= 1
        look -= 1

    return size - num_b + num_a


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
