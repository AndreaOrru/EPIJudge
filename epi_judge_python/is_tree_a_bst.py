from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst_helper(tree, lower_bound=float('-inf'), upper_bound=float('inf')):
    if tree is None:
        return True
    if tree.data < lower_bound:
        return False
    if tree.data > upper_bound:
        return False

    return is_binary_tree_bst_helper(tree.left, lower_bound, tree.data) and \
           is_binary_tree_bst_helper(tree.right, tree.data, upper_bound)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return is_binary_tree_bst_helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
