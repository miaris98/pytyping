"""
LeetCode 11: Container With Most Water
Find two lines that together with the x-axis form a container, such that the container contains the most water.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water\n