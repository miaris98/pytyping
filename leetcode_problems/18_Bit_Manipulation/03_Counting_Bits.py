"""
LeetCode 338: Counting Bits
Companies: Amazon, Google, Goldman Sachs, Nvidia, Apple
Time Complexity: O(N) - Computes each number's bit count in O(1) using `dp[i >> 1] + (i & 1)`.
Space Complexity: O(N) - Output array `dp` of length `n + 1`.
Intuition: The number of 1-bits in `i` equals the number of 1-bits in `i >> 1` (which is `i // 2`, already computed!) plus the lowest bit `(i & 1)`.
Why Efficient: Reuses previously computed bit counts in O(1) per number instead of O(N log N).
"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
