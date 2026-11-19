"""
LeetCode 19: Remove Nth Node From End of List
Companies: Meta, Amazon, Microsoft, Google, Apple, Bloomberg
Time Complexity: O(N) - Single pass using two pointers separated by a gap of `n` nodes.
Space Complexity: O(1) - Uses a `dummy` node and two pointers `left` and `right`.
Intuition: Advance `right` by `n` steps first, then move `left` (starting at `dummy`) and `right` together until `right` hits the end—placing `left` right before the target node.
Why Efficient: Finds and removes the Nth node from the end in a single pass with a `dummy` node that cleanly handles removing the head.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
