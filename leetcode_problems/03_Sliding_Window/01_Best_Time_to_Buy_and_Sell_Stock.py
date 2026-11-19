"""
LeetCode 121: Best Time to Buy and Sell Stock
Companies: Amazon, Meta, Google, Microsoft, Bloomberg, Apple, Goldman Sachs
Time Complexity: O(N) - Single chronological pass through prices.
Space Complexity: O(1) - Tracks only `min_price` and `max_profit`.
Intuition: Track the lowest buying price seen so far (`min_price`) and test selling at each current price (`price - min_price`).
Why Efficient: Replaces O(N²) nested buy/sell loops with a single O(N) running-minimum pass using O(1) space.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
