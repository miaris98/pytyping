"""
LeetCode 11: Container With Most Water
Companies: Amazon, Google, Meta, Microsoft, Apple, Bloomberg, Adobe
Time Complexity: O(N) - Single pass moving the shorter boundary pointer inward N - 1 times.
Space Complexity: O(1) - Only scalar pointer and maximum tracking variables.
Intuition: Start with maximum width (`left = 0, right = n - 1`). Since water height is capped by the shorter wall, always move the shorter pointer inward in hopes of finding a taller wall.
Why Efficient: Eliminates N - 1 suboptimal pairs on every single step, turning an O(N²) all-pairs check into an optimal O(N) greedy two-pointer scan.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            max_water = max(max_water, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
