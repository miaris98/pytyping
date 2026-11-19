"""
LeetCode 141: Linked List Cycle
Companies: Amazon, Microsoft, Spotify, Apple, Google, Visa
Time Complexity: O(N) - Fast pointer catches slow pointer within one cycle loop.
Space Complexity: O(1) - Floyd's Tortoise and Hare uses only two pointers.
Intuition: Move `slow` by 1 step and `fast` by 2 steps. If a cycle exists, `fast` will eventually lap and meet `slow` inside the cycle.
Why Efficient: A hash set of visited nodes takes O(N) memory. Floyd's cycle-finding algorithm detects cycles in O(1) constant space.
"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
