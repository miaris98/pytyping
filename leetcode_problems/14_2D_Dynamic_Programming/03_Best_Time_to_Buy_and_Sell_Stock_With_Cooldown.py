"""
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
Companies: Amazon, Google, Adobe, Citadel
Time Complexity: O(N) - Single pass tracking state machine transitions.
Space Complexity: O(1) - Three state variables: `held`, `sold`, and `reset`.
Intuition: Model the 3 states on each day: `held` (holding stock), `sold` (just sold today, entering cooldown), and `reset` (ready to buy).
Why Efficient: State-machine DP uses O(N) time and O(1) space instead of an O(N) recursion cache.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float("-inf"), float("-inf"), 0
        for p in prices:
            pre_sold = sold
            sold = held + p
            held = max(held, reset - p)
            reset = max(reset, pre_sold)
        return max(sold, reset)
