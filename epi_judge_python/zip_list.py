from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_list(L: ListNode) -> Optional[ListNode]:
    prev_node, curr_node, next_node = None, L, None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node

    return prev_node


def zipping_linked_list(L: ListNode) -> Optional[ListNode]:
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    first_half, second_half = L, slow.next
    slow.next = None
    second_half = reverse_list(second_half)

    first_half_iter, second_half_iter = first_half, second_half
    while second_half_iter:
        next_first_node = first_half_iter.next
        next_second_node = second_half_iter.next

        first_half_iter.next = second_half_iter
        second_half_iter.next = next_first_node

        first_half_iter = next_first_node
        second_half_iter = next_second_node

    return first_half


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('zip_list.py', 'zip_list.tsv',
                                       zipping_linked_list))
