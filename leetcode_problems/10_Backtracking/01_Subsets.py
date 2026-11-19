"""
LeetCode 78: Subsets
Companies: Meta, Amazon, Google, Bloomberg, Microsoft, Apple
Time Complexity: O(N * 2^N) - Generates all 2^N subsets, copying up to N elements per subset.
Space Complexity: O(N) - Recursion stack depth and current `subset` path.
Intuition: At every index `i`, make a binary decision: either include `nums[i]` in the current subset or skip `nums[i]`.
Why Efficient: Explores the binary decision tree directly without generating duplicate subsets.
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def dfs(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
