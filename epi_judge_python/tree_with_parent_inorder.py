from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []
    prev_node = None

    while tree:
        if prev_node is tree.parent:
            if tree.left:
                next_node = tree.left
            else:
                result.append(tree.data)
                next_node = tree.right or tree.parent
        elif prev_node is tree.left:
            result.append(tree.data)
            next_node = tree.right or tree.parent
        else:
            next_node = tree.parent

        prev_node, tree = tree, next_node

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
