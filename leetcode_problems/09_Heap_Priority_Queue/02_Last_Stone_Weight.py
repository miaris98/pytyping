"""
LeetCode 1046: Last Stone Weight
Companies: Amazon, Visa, Nvidia, LinkedIn, Google
Time Complexity: O(N log N) - O(N) heapify plus N smash rounds taking O(log N) each.
Space Complexity: O(N) - Max-heap simulated with negated stone weights.
Intuition: Negate all weights to simulate a Max-Heap using Python's `heapq` min-heap. Repeatedly pop the two heaviest stones `y` and `x`, pushing `y - x` back if they differ.
Why Efficient: Re-sorting the array after every smash takes O(N² log N). A max-heap extracts the two largest stones and re-inserts the remainder in O(log N) per step.
"""
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first > second:
                heapq.heappush(heap, -(first - second))
        return -heap[0] if heap else 0
