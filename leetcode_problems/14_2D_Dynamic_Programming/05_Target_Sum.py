"""
LeetCode 494: Target Sum
Companies: Meta, Amazon, Google, Adobe
Time Complexity: O(N * S) - Subset sum DP up to `(total + target) // 2`.
Space Complexity: O(S) - 1D DP array of size `P + 1`.
Intuition: Splitting numbers into positive `P` and negative `N` means `P - N = target` and `P + N = total`, so `P = (total + target) // 2`—reducing the problem to 0/1 Subset Sum count!
Why Efficient: Algebraic reduction to 0/1 Knapsack avoids negative index offsets and cuts the state space in half.
"""
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        pos_sum = (total + target) // 2
        dp = [0] * (pos_sum + 1)
        dp[0] = 1
        for n in nums:
            for s in range(pos_sum, n - 1, -1):
                dp[s] += dp[s - n]
        return dp[pos_sum]
