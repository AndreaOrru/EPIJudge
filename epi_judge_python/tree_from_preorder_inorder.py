from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    inorder_indexes = {el: i for i, el in enumerate(inorder)}

    def construct_tree(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start > preorder_end or inorder_start > inorder_end:
            return None

        root = preorder[preorder_start]
        root_inorder_idx = inorder_indexes[root]
        n_left_elements = root_inorder_idx - inorder_start

        tree = BinaryTreeNode(root)
        tree.left = construct_tree(preorder_start + 1,
                                   preorder_start + n_left_elements,
                                   inorder_start,
                                   root_inorder_idx - 1)
        tree.right = construct_tree(preorder_start + n_left_elements + 1,
                                    preorder_end,
                                    root_inorder_idx + 1,
                                    inorder_end)
        return tree

    return construct_tree(0, len(preorder) - 1,
                          0, len(inorder) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
