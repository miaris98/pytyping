"""
LeetCode 206: Reverse Linked List
Companies: Amazon, Microsoft, Meta, Apple, Google, Bloomberg
Time Complexity: O(N) - Single pass visiting each node once.
Space Complexity: O(1) - Reverses `.next` pointers in-place using `prev`, `curr`, and `next_temp`.
Intuition: Walk through the list iteratively, saving `curr.next` before flipping `curr.next = prev`.
Why Efficient: Iterative pointer reversal uses O(1) memory compared to O(N) recursion stack space.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
