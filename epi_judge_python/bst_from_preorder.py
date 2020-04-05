from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder_on2(preorder_sequence: List[int]) -> Optional[BstNode]:
    def build_tree(start, end):
        if start > end:
            return None

        root_val = preorder_sequence[start]

        right_index = start + 1
        while right_index <= end:
            if preorder_sequence[right_index] > root_val:
                break
            right_index += 1

        tree = BstNode(root_val)
        tree.left = build_tree(start + 1, right_index - 1)
        tree.right = build_tree(right_index, end)

        return tree

    return build_tree(0, len(preorder_sequence) - 1)

from collections import namedtuple
Result = namedtuple('Result', ('tree', 'root_idx'))

def rebuild_bst_from_preorder(preorder_sequence: List[int]) -> Optional[BstNode]:
    def construct_tree(root_idx, lower_bound, upper_bound):
        if root_idx == len(preorder_sequence):
            return Result(None, root_idx)

        root_val = preorder_sequence[root_idx]
        if not lower_bound <= root_val <= upper_bound:
            return Result(None, root_idx)
        root_idx += 1

        tree = BstNode(root_val)
        tree.left, root_idx = construct_tree(root_idx, lower_bound, root_val)
        tree.right, root_idx = construct_tree(root_idx, root_val, upper_bound)

        return Result(tree, root_idx)

    return construct_tree(0, float('-inf'), float('inf')).tree


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
