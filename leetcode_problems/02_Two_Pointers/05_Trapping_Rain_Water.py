"""
LeetCode 42: Trapping Rain Water
Companies: Goldman Sachs, Amazon, Google, Meta, Microsoft, Apple, Bloomberg
Time Complexity: O(N) - Single two-pointer traversal visiting each bar once.
Space Complexity: O(1) - Tracks `left_max` and `right_max` scalars instead of O(N) prefix/suffix arrays.
Intuition: Water trapped above any bar depends on `min(max_left, max_right) - height[i]`. By always advancing the side with the smaller running maximum, we know the exact bottleneck height immediately.
Why Efficient: Dynamic programming prefix/suffix tables require O(N) extra memory. Two pointers achieve the same O(N) speed in O(1) constant space.
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water
