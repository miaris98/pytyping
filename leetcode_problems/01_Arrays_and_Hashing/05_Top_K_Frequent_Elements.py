"""
LeetCode 347: Top K Frequent Elements
Companies: Meta, Amazon, Google, Microsoft, Apple, Uber, Bloomberg
Time Complexity: O(N) - Frequency counting plus linear bucket scan across N buckets.
Space Complexity: O(N) - Counter map and frequency buckets of size N + 1.
Intuition: Since any element's frequency is between 1 and N, create an array of N + 1 buckets where `bucket[freq]` holds numbers appearing `freq` times.
Why Efficient: Sorting takes O(N log N) and a heap takes O(N log K). Bucket sort exploits the bounded frequency range [1..N] to achieve strict O(N) linear time.
"""
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
