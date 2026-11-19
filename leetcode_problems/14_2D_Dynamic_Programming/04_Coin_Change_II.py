"""
LeetCode 518: Coin Change II
Companies: Amazon, Bloomberg, Google, Morgan Stanley, Uber
Time Complexity: O(C * A) - Outer loop over coins, inner loop up to `amount`.
Space Complexity: O(A) - 1D DP array `dp[0..amount]`.
Intuition: Loop over `coin` in the OUTER loop and `x` in the INNER loop (`dp[x] += dp[x - coin]`) so each coin is used in canonical order, counting combinations instead of permutations.
Why Efficient: 1D array reduces memory from O(C * A) to O(A).
"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
