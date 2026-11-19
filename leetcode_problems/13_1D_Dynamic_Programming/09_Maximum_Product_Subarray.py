"""
LeetCode 152: Maximum Product Subarray
Companies: LinkedIn, Amazon, Google, Microsoft, Meta, InfoSys
Time Complexity: O(N) - Single pass tracking both running max and running min.
Space Complexity: O(1) - Only scalar variables `cur_max`, `cur_min`, and `res`.
Intuition: Because multiplying two negative numbers produces a huge positive product, track both `cur_max` and `cur_min` at every element.
Why Efficient: Solves sign-flipping subarray products in one O(N) pass and O(1) memory.
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_min = cur_max = nums[0]
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            res = max(res, cur_max)
        return res
