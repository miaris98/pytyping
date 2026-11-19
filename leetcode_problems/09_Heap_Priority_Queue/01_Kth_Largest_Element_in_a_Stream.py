"""
LeetCode 703: Kth Largest Element in a Stream
Companies: Amazon, Meta, Google, LinkedIn, Adobe
Time Complexity: O(log K) per `add` call - Min-heap capped at size K.
Space Complexity: O(K) - Stores only the K largest elements seen so far.
Intuition: Maintain a Min-Heap of size `k` containing the `k` largest elements. The smallest among the top `k` (sitting at `self.heap[0]`) is the exact Kth largest element!
Why Efficient: Keeping a sorted list costs O(N) per insertion. A size-K min-heap processes every new stream element in O(log K) time and reads the Kth largest in O(1).
"""
from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
