"""
LeetCode 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
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
        return []\n