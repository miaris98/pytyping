"""
LeetCode 23: Merge k Sorted Lists
Companies: Meta, Amazon, Google, Microsoft, Apple, Uber, LinkedIn
Time Complexity: O(N log K) - Min-heap of size K processes all N total nodes.
Space Complexity: O(K) - Heap holds at most one head node from each of the K lists.
Intuition: Push the head of each non-empty list into a Min-Heap `(node.val, idx, node)`. Repeatedly pop the smallest node, attach it to `tail.next`, and push its `.next` node.
Why Efficient: Merging lists one-by-one takes O(N * K) time. A min-heap of size K finds the next smallest node across all K lists in O(log K) time.
"""
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        tail = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
