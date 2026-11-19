"""
LeetCode 25: Reverse Nodes in k-Group
Companies: Amazon, Microsoft, Meta, Google, Apple, Bloomberg
Time Complexity: O(N) - Each node is visited twice (once by `get_kth`, once during reversal).
Space Complexity: O(1) - Reverses each group of `k` nodes in-place using pointer manipulation.
Intuition: Use `group_prev` before each chunk of `k` nodes. Check if `k` nodes remain; if so, reverse those `k` nodes in-place and stitch `group_prev.next` to the new chunk head.
Why Efficient: Achieves O(1) space in-place reversal without recursion or auxiliary arrays.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
