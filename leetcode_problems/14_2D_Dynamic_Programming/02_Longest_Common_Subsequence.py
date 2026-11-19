"""
LeetCode 1143: Longest Common Subsequence
Companies: Amazon, DoorDash, Google, Microsoft, Karat, Bloomberg
Time Complexity: O(M * N) - Nested loop over characters of `text1` and `text2`.
Space Complexity: O(N) - 1D row DP array of size `len(text2) + 1`.
Intuition: If `text1[i] == text2[j]`, `dp[i][j] = 1 + dp[i+1][j+1]`; otherwise `max(dp[i+1][j], dp[i][j+1])`.
Why Efficient: Bottom-up DP avoids exponential recursion and solves LCS in O(M * N) time.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            prev_diag = 0
            for j in range(len(text2) - 1, -1, -1):
                tmp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev_diag = tmp
        return dp[0]
