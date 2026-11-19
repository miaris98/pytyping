"""
LeetCode 739: Daily Temperatures
Companies: Meta, Amazon, Google, Microsoft, Apple, TikTok, Bloomberg
Time Complexity: O(N) - Each index is pushed and popped from the monotonic stack at most once.
Space Complexity: O(N) - Monotonic stack stores unresolved day indices.
Intuition: Maintain a Monotonic Decreasing Stack of indices. When today's temperature is warmer than the day at the top of the stack, pop that day and record `today - prev_day`.
Why Efficient: Replaces O(N²) forward scans with a single O(N) monotonic stack pass that resolves multiple waiting days as soon as a warmer day arrives.
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res
