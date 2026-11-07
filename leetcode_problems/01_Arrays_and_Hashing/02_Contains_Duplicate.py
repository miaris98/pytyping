"""
LeetCode 217: Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False\n