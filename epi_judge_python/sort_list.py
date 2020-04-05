from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_sorted_lists(L1: Optional[ListNode],
                       L2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    tail.next = L1 or L2

    return dummy_head.next


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # Base case (0 or 1 elements).
    if L is None or L.next is None:
        return L

    # Split list in half.
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        slow, fast = slow.next, fast.next.next
    if pre_slow:
        pre_slow.next = None

    # Merge recursively sorted lists.
    return merge_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
