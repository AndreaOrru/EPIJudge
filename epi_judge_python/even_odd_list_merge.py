from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    even_dummy_head = ListNode(None)
    odd_dummy_head = ListNode(None)

    tails = [even_dummy_head, odd_dummy_head]
    turn = 0

    i = 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn = not turn

    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
