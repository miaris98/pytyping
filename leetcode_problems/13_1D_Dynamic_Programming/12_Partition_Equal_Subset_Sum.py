"""
LeetCode 416: Partition Equal Subset Sum
Companies: Amazon, Meta, Google, Microsoft, Apple, Expedia
Time Complexity: O(N * S) - N elements times half-sum S.
Space Complexity: O(S) - Hash set / 1D boolean state of reachable subset sums up to `sum(nums) // 2`.
Intuition: If `sum(nums)` is odd, return False; otherwise check if any subset sums to `target = sum(nums) // 2` using 0/1 Knapsack DP.
Why Efficient: Uses a single 1D set of reachable sums (early-exiting as soon as `target` is formed) instead of an O(N * S) 2D table.
"""
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for n in nums:
            dp |= {t + n for t in dp if t + n <= target}
            if target in dp:
                return True
        return target in dp
