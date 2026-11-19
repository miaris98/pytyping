"""
LeetCode 55: Jump Game
Companies: Amazon, Google, Microsoft, Meta, Apple, Uber, DoorDash
Time Complexity: O(N) - Single backward greedy pass.
Space Complexity: O(1) - Single `goal` index variable.
Intuition: Start with `goal = len(nums) - 1` and walk backward. Whenever index `i` can reach or pass `goal` (`i + nums[i] >= goal`), shift `goal = i`.
Why Efficient: Dynamic programming takes O(N²) time and O(N) space. Backward greedy goal-shifting runs in O(N) time and O(1) space.
"""
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
