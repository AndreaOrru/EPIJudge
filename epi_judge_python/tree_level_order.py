from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque


def binary_tree_depth_order_queue(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []

    queue = deque([(0, tree)])
    result = []

    while queue:
        depth, node = queue.popleft()
        if depth >= len(result):
            result.append([])
        result[depth].append(node.data)

        if node.left:
            queue.append((depth + 1, node.left))
        if node.right:
            queue.append((depth + 1, node.right))

    return result


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []

    result = []
    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])

        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes
            for child in (curr.left, curr.right) if child
        ]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
