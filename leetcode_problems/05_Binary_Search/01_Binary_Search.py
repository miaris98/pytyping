"""
LeetCode 704: Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1\n