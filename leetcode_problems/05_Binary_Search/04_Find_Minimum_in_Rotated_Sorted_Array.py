"""
LeetCode 153: Find Minimum in Rotated Sorted Array
Companies: Amazon, Microsoft, Meta, Google, Bloomberg, Uber
Time Complexity: O(log N) - Halves the search range in each step.
Space Complexity: O(1) - Constant pointer variables.
Intuition: Compare `nums[mid]` with `nums[high]`. If `nums[mid] > nums[high]`, the minimum pivot must lie in the right half (`low = mid + 1`); otherwise it lies at `mid` or to the left (`high = mid`).
Why Efficient: Finds the rotation pivot in O(log N) time instead of an O(N) linear scan.
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
