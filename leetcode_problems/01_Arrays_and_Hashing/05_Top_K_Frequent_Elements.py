"""
LeetCode 347: Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]\n