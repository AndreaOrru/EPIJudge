from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree, k, first_so_far=None):
    if tree is None:
        return first_so_far if first_so_far else None

    if tree.data > k:
        return find_first_greater_than_k(tree.left, k, tree)
    else:
        return find_first_greater_than_k(tree.right, k, first_so_far)


def find_first_greater_than_k_iter(tree: BstNode, k: int) -> Optional[BstNode]:
    first_so_far = None
    while tree:
        if tree.data > k:
            first_so_far = tree
            tree = tree.left
        else:
            tree = tree.right
    return first_so_far


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
