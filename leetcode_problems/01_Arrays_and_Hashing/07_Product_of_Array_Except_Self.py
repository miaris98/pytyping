"""
LeetCode 238: Product of Array Except Self
Companies: Amazon, Meta, Apple, Microsoft, Google, Bloomberg, Uber, Asana
Time Complexity: O(N) - One forward pass for prefixes and one backward pass for suffixes.
Space Complexity: O(1) - Uses the output array directly with only two scalar accumulators.
Intuition: Every element's answer is the product of all numbers to its left multiplied by the product of all numbers to its right.
Why Efficient: Avoids O(N²) nested loops and avoids division (which breaks when zeros exist) while using O(1) auxiliary space beyond the output list.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
