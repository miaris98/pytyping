"""
LeetCode 322: Coin Change
Companies: Amazon, Bloomberg, Microsoft, Google, Meta, Apple, Visa
Time Complexity: O(C * A) - C coins times target amount A.
Space Complexity: O(A) - 1D DP array of size `amount + 1`.
Intuition: Build `dp[x]` = fewest coins to make amount `x` via `dp[x] = min(dp[x], dp[x - coin] + 1)`.
Why Efficient: Bottom-up 1D DP avoids exponential recursion and solves unbounded knapsack in O(C * A) time.
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
