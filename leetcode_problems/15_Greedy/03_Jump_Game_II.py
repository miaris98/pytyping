"""
LeetCode 45: Jump Game II
Companies: Amazon, Google, Apple, TikTok, Microsoft, Bloomberg
Time Complexity: O(N) - 1D level-by-level greedy BFS window `[l, r]`.
Space Complexity: O(1) - Tracks only window pointers `l`, `r`, and `jumps`.
Intuition: Maintain the current jump range `[l, r]` (like a BFS level). Scan `[l, r]` to find the `farthest` index reachable in one more jump, then advance `(l, r) = (r + 1, farthest)`.
Why Efficient: Simulates level-order shortest-path BFS on the array in O(N) time using O(1) pointers instead of a queue.
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = max(i + nums[i] for i in range(l, r + 1))
            l = r + 1
            r = farthest
            jumps += 1
        return jumps
