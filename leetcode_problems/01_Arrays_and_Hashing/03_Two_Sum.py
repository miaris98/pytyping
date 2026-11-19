"""
LeetCode 1: Two Sum
Companies: Google, Amazon, Meta, Microsoft, Apple, Bloomberg, Uber, Adobe
Time Complexity: O(N) - Single pass through the array with O(1) hash table lookups.
Space Complexity: O(N) - Stores at most N - 1 elements and their indices in the hash map.
Intuition: For each number `num`, the exact partner needed is `complement = target - num`. Store seen numbers in a dict mapping `{value: index}`.
Why Efficient: Replaces the O(N) inner search loop of an O(N²) brute-force approach with an O(1) hash map lookup, solving the problem in one O(N) pass.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
