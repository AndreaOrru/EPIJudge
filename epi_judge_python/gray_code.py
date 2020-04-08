import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def differ_by_1_bit(x, y):
    bit_difference = x ^ y
    return bit_difference and not bit_difference & (bit_difference - 1)

def gray_code_rec(num_bits: int) -> List[int]:
    def directed_gray_code(history):
        if len(result) == 1 << num_bits:
            return differ_by_1_bit(result[0], result[-1])

        for i in range(num_bits):
            previous_code = result[-1]
            candidate_next_code = previous_code ^ (1 << i)
            if candidate_next_code not in history:
                history.add(candidate_next_code)
                result.append(candidate_next_code)
                if directed_gray_code(history):
                    return True
                result.pop()
                history.remove(candidate_next_code)

        return False

    result = [0]
    directed_gray_code({0})
    return result


def gray_code(num_bits: int) -> List[int]:
    if num_bits == 0:
        return [0]

    prev_gray_code = gray_code(num_bits - 1)
    leading_bit = 1 << (num_bits - 1)

    return prev_gray_code + [leading_bit | i for i in reversed(prev_gray_code)]


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = (1 << num_bits)
    if len(result) != expected_size:
        raise TestFailure('Length mismatch: expected ' + str(expected_size) +
                          ', got ' + str(len(result)))
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure('Two adjacent entries are equal')
            else:
                raise TestFailure(
                    'Two adjacent entries differ by more than 1 bit')

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure('Not all entries are distinct: found ' +
                          str(len(result) - len(uniq)) + ' duplicates')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('gray_code.py', 'gray_code.tsv',
                                       gray_code_wrapper))
