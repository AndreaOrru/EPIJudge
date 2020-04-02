from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree1, subtree2):
        if not subtree1 and not subtree2:
            return True

        elif subtree1 and subtree2:
            return subtree1.data == subtree2.data and \
                   check_symmetric(subtree1.left, subtree2.right) and \
                   check_symmetric(subtree1.right, subtree2.left)

        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
