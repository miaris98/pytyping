"""
LeetCode 21: Merge Two Sorted Lists
Companies: Amazon, Microsoft, Meta, Apple, Google, Adobe
Time Complexity: O(N + M) - Advances through one node of `list1` or `list2` on each comparison.
Space Complexity: O(1) - Splices existing nodes in-place using a single `dummy` anchor node.
Intuition: Use a `dummy` node and `tail` pointer, repeatedly attaching the smaller front node of `list1` or `list2`.
Why Efficient: In-place pointer splicing uses O(1) memory and attaches any leftover tail in O(1).
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
