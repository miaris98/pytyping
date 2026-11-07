"""
LeetCode 121: Best Time to Buy and Sell Stock
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit\n