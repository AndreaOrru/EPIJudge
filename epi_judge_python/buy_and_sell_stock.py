from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0.0
    min_so_far = float('inf')

    for price in prices:
        profit = price - min_so_far
        max_profit = max(max_profit, profit)
        min_so_far = min(min_so_far, price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
