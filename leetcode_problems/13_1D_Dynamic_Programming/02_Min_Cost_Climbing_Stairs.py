"""
LeetCode 746: Min Cost Climbing Stairs
Companies: Amazon, Bloomberg, Google, Microsoft, Apple
Time Complexity: O(N) - Single backward/forward pass over N steps.
Space Complexity: O(1) - Two rolling cost variables `down_one` and `down_two`.
Intuition: At each step `i`, the minimum cost to reach it is `min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`.
Why Efficient: Computes the optimal cost in O(N) time using O(1) space without mutating the input array.
"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
        return min(prev1, prev2)
