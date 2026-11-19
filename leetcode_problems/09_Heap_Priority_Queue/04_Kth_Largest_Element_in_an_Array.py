"""
LeetCode 215: Kth Largest Element in an Array
Companies: Meta, Amazon, LinkedIn, Google, Microsoft, Apple, Bloomberg
Time Complexity: O(N log K) - Maintains a min-heap of size K across N elements.
Space Complexity: O(K) - Heap stores at most K elements at any time.
Intuition: Maintain a Min-Heap of size `k`. After scanning all numbers and evicting anything smaller than the top `k`, `heap[0]` is the `k`-th largest element.
Why Efficient: Avoids O(N log N) full sort and avoids Quickselect's O(N²) worst-case degradation on duplicate-heavy inputs.
"""
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
