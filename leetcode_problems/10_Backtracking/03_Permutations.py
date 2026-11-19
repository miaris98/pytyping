"""
LeetCode 46: Permutations
Companies: Amazon, LinkedIn, Microsoft, Meta, Google, Apple
Time Complexity: O(N * N!) - Generates N! permutations of length N.
Space Complexity: O(N) - In-place swapping along the recursion stack of depth N.
Intuition: Fix each element at index `idx` by swapping `nums[idx]` with every candidate `nums[i]` from `idx` to `n - 1`, recurse on `idx + 1`, then swap back.
Why Efficient: In-place swapping avoids allocating boolean `used` arrays or slicing new lists at every recursive step.
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx: int):
            if idx == len(nums):
                res.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)
        return res
