"""
LeetCode 90: Subsets II
Companies: Amazon, Meta, Bloomberg, Google, Yahoo
Time Complexity: O(N * 2^N) - Sorting plus exploring unique subset branches.
Space Complexity: O(N) - Recursion stack depth.
Intuition: Sort `nums` first so duplicate numbers are adjacent. When we decide to skip `nums[i]`, advance `i` past all identical copies of `nums[i]` so we never start a duplicate branch.
Why Efficient: Sorting and skipping adjacent duplicates in the exclude branch avoids O(2^N) set hashing overhead.
"""
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []

        def backtrack(i: int):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
