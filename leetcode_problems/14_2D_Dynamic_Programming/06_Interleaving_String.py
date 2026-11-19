"""
LeetCode 97: Interleaving String
Companies: Amazon, Apple, Google, Microsoft, Bloomberg
Time Complexity: O(M * N) - Evaluates each `(i, j)` prefix pair once.
Space Complexity: O(N) - 1D boolean DP row.
Intuition: `dp[i][j]` is True if `s3[i+j:]` can be formed by interleaving `s1[i:]` (matching `s1[i] == s3[i+j]`) or `s2[j:]` (matching `s2[j] == s3[i+j]`).
Why Efficient: Collapses exponential branching into O(M * N) time and O(N) space.
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        dp[len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[j]:
                    dp[j] = True
                elif j < len(s2) and s2[j] == s3[i + j] and dp[j + 1]:
                    dp[j] = True
                elif not (i == len(s1) and j == len(s2)):
                    dp[j] = False
        return dp[0]
