"""
LeetCode 139: Word Break
Companies: Amazon, Meta, Google, Bloomberg, Apple, Qualtrics, Walmart
Time Complexity: O(N * W * L) - For each index i, checks dictionary words of length L.
Space Complexity: O(N) - Boolean DP array of length `len(s) + 1`.
Intuition: Work backward: `dp[i]` is True if some `w` in `wordDict` matches `s[i : i + len(w)]` and the remaining suffix `dp[i + len(w)]` is also True.
Why Efficient: Bottom-up DP eliminates exponential backtracking over overlapping suffix splits.
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
