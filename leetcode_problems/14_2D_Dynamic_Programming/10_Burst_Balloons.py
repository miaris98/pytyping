"""
LeetCode 312: Burst Balloons
Companies: Amazon, Google, Samsung, Adobe, C3 IoT
Time Complexity: O(N³) - Interval DP over subarray lengths and last-burst pivot `i`.
Space Complexity: O(N²) - 2D interval DP table `dp[l][r]`.
Intuition: Think in reverse: instead of choosing which balloon to burst FIRST (which makes non-adjacent balloons become adjacent), choose which balloon `i` in `(l, r)` is burst LAST—so its neighbors are guaranteed to be `nums[l-1]` and `nums[r+1]`!
Why Efficient: Choosing the LAST balloon to burst makes the left and right sub-intervals `[l, i-1]` and `[i+1, r]` completely independent, reducing O(N!) to O(N³) interval DP.
"""
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n - 1):
            for l in range(1, n - length):
                r = l + length - 1
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n - 2]
