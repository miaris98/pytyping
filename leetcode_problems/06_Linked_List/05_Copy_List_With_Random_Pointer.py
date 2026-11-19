"""
LeetCode 138: Copy List with Random Pointer
Companies: Meta, Amazon, Microsoft, Bloomberg, Google, Nvidia
Time Complexity: O(N) - Two linear passes over the linked list.
Space Complexity: O(N) - Hash map mapping each original node to its cloned counterpart.
Intuition: Pass 1 creates a clone for every node in a dictionary `{old_node: new_node}`. Pass 2 wires up `.next` and `.random` pointers via O(1) dictionary lookups.
Why Efficient: Handles arbitrary cycles and forward/backward `.random` pointers cleanly in O(N) time.
"""
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        old_to_copy = {None: None}
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next
        return old_to_copy[head]
