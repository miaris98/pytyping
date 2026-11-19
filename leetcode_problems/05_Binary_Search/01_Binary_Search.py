"""
LeetCode 704: Binary Search
Companies: Google, Amazon, Microsoft, Apple, Meta, Bloomberg
Time Complexity: O(log N) - Halves the search interval on every comparison.
Space Complexity: O(1) - Iterative pointers `low`, `high`, and `mid`.
Intuition: Compare `target` with the middle element `nums[mid]`. Discard the left half if `nums[mid] < target` or the right half if `nums[mid] > target`.
Why Efficient: Reduces O(N) linear search to O(log N) logarithmic time with O(1) memory.
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
        return -1
