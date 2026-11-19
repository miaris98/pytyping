"""
LeetCode 72: Edit Distance
Companies: Amazon, Google, LinkedIn, Rubrik, Microsoft, Goldman Sachs
Time Complexity: O(M * N) - Levenshtein DP over both strings.
Space Complexity: O(M * N) - 2D DP table storing minimum operations for each suffix pair.
Intuition: If `word1[i] == word2[j]`, cost is `dp[i+1][j+1]`; otherwise `1 + min(insert, delete, replace)` = `1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])`.
Why Efficient: Bottom-up tabulation computes the minimum Levenshtein distance in O(M * N) polynomial time.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
