"""
LeetCode 84: Largest Rectangle in Histogram
Companies: Amazon, Google, Meta, Microsoft, Adobe, Citadel
Time Complexity: O(N) - Each bar is pushed and popped from the stack once.
Space Complexity: O(N) - Monotonic increasing stack of `(start_index, height)` pairs.
Intuition: Keep a Monotonic Increasing Stack. When a shorter bar arrives, taller bars on the stack can no longer extend right—pop them, compute their max area, and carry their `start` index backward.
Why Efficient: Brute-force expanding around each bar takes O(N²). The monotonic stack finds both the left and right boundaries for every bar in a single O(N) pass.
"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area
