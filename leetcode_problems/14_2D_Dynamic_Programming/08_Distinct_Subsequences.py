"""
LeetCode 115: Distinct Subsequences
Companies: Google, Amazon, Bloomberg, Citadel, Apple
Time Complexity: O(M * N) - Bottom-up DP over lengths of `s` and `t`.
Space Complexity: O(N) - 1D DP array of length `len(t) + 1`.
Intuition: When `s[i] == t[j]`, we can either match them (`dp[j + 1]`) or skip `s[i]` (`dp[j]`), so `dp[j] += dp[j + 1]`.
Why Efficient: 1D reverse-order update computes the exact count in O(M * N) time and O(N) memory.
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]
        return dp[0]
