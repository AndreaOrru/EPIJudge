from typing import List

from test_framework import generic_test, test_utils

from math import log2


def generate_power_set_bits(input_set: List[int]) -> List[List[int]]:
    power_set = []

    for bit_array in range(1 << len(input_set)):
        subset = []
        while bit_array:
            i = int(log2(bit_array & ~(bit_array - 1)))
            subset.append(input_set[i])
            bit_array &= bit_array - 1
        power_set.append(subset)

    return power_set


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])
    return power_set



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
