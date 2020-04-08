import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def construct_tree(i):
        root_val = preorder[i]
        i += 1

        if root_val is None:
            return None, i

        tree = BinaryTreeNode(root_val)
        tree.left, i = construct_tree(i)
        tree.right, i = construct_tree(i)

        return tree, i

    return construct_tree(0)[0]


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
