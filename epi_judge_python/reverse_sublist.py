from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(None, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        rest = sublist_iter.next.next
        element_to_move = sublist_iter.next

        sublist_iter.next = rest
        element_to_move.next = sublist_head.next
        sublist_head.next = element_to_move

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
