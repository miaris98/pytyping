"""
LeetCode 973: K Closest Points to Origin
Companies: Meta, Amazon, Google, Asana, Apple, Uber
Time Complexity: O(N + K log N) - Linear O(N) `heapify` followed by K `heappop` operations.
Space Complexity: O(N) - Heap of squared distances `(x² + y², x, y)`.
Intuition: Compare squared Euclidean distances `x*x + y*y` (skipping `sqrt`), `heapify` all points in O(N) time, and pop the `k` smallest.
Why Efficient: Bottom-up `heapq.heapify` builds the heap in O(N) linear time, and popping `k` times costs O(K log N)—faster than full O(N log N) sorting.
"""
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(heap)
        return [[x, y] for _, x, y in [heapq.heappop(heap) for _ in range(k)]]
