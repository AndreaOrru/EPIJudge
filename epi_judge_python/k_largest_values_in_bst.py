from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def traversal(tree, k, result):
    if tree is None or len(result) >= k:
        return

    traversal(tree.right, k, result)
    if len(result) < k:
        result.append(tree.data)
        traversal(tree.left, k, result)

    return result


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []
    traversal(tree, k, result)
    return result[:k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
