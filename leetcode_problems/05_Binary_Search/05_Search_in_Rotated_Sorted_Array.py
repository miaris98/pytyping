"""
LeetCode 33: Search in Rotated Sorted Array
Companies: Meta, Amazon, Google, Microsoft, LinkedIn, Apple, Bloomberg, Uber
Time Complexity: O(log N) - Single-pass binary search eliminating half the array each step.
Space Complexity: O(1) - Constant space pointers.
Intuition: At any midpoint `mid`, at least one half (`low..mid` or `mid..high`) is guaranteed to be strictly sorted. Check which half is sorted, then check if `target` falls within that sorted half's bounds.
Why Efficient: Solves rotated search in one O(log N) binary search without needing a separate pass to find the pivot first.
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
