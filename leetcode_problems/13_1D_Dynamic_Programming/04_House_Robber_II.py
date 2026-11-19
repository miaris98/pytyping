"""
LeetCode 213: House Robber II
Companies: Google, Amazon, Microsoft, TikTok, eBay
Time Complexity: O(N) - Two linear passes of standard House Robber.
Space Complexity: O(1) - Rolling variables in helper.
Intuition: Since the first and last houses are adjacent in a circle, you cannot rob both. Run linear House Robber twice: once excluding the first house `nums[1:]` and once excluding the last `nums[:-1]`.
Why Efficient: Decomposes a circular DP constraint into two simple linear O(N) passes with O(1) space.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob_linear(nums[1:]), self._rob_linear(nums[:-1]))

    def _rob_linear(self, arr: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in arr:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2
