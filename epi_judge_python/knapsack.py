import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity_memo(items: List[Item], capacity: int) -> int:
    @functools.lru_cache(None)
    def knapsack(k, available_capacity):
        # All items have been selected, no more can be chosen.
        if k < 0:
            return 0

        # Discard the current item => available capacity stays the same.
        without_curr_item = knapsack(k - 1, available_capacity)

        # Try to pick the current item => decrease available capacity.
        if available_capacity < items[k].weight:
            with_curr_item = 0
        else:
            with_curr_item = items[k].value + knapsack(k - 1, available_capacity - items[k].weight)
        return max(without_curr_item, with_curr_item)

    return knapsack(len(items) - 1, capacity)


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(2)]

    for i in range(len(items) + 1):
        for w in range(capacity + 1):
            item = items[i - 1]
            # No objects or no capacity.
            if i == 0 or w == 0:
                dp[i % 2][w] = 0
            # There is enough space to select this item.
            elif item.weight <= w:
                dp[i % 2][w] = max(dp[(i - 1) % 2][w], item.value + dp[(i - 1) % 2][w - item.weight])
            # There isn't enough space to select this item.
            else:
                dp[i % 2][w] = dp[(i - 1) % 2][w]

    return dp[len(items) % 2][capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
