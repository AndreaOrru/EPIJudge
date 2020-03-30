from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def find_height(root: BinaryTreeNode, cache) -> int:
    if root is None:
        return -1
    
    if id(root) in cache:
        return cache[id(root)]

    height = 1 + max(find_height(root.left, cache), find_height(root.right, cache))
    cache[id(root)] = height

    return height


def is_balanced_binary_tree_helper(tree: BinaryTreeNode, cache) -> bool:
    if tree is None:
        return True

    height_left = find_height(tree.left, cache)
    height_right = find_height(tree.right, cache)

    if abs(height_left - height_right) > 1:
        return False
    else:
        return is_balanced_binary_tree_helper(tree.left, cache) and \
               is_balanced_binary_tree_helper(tree.right, cache)


def is_balanced_binary_tree_unefficient(tree):
    return is_balanced_binary_tree_helper(tree, {})


################################################################################


from collections import namedtuple

BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))


def check_balanced(tree: BinaryTreeNode) -> BalancedStatusWithHeight:
    if tree is None:
        return BalancedStatusWithHeight(balanced=True, height=-1)

    left_result = check_balanced(tree.left)
    if not left_result.balanced:
        return left_result

    right_result = check_balanced(tree.right)
    if not right_result.balanced:
        return right_result

    is_balanced = abs(left_result.height - right_result.height) <= 1
    height = max(left_result.height, right_result.height) + 1
    return BalancedStatusWithHeight(is_balanced, height)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
