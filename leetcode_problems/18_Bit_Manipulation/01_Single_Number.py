"""
LeetCode 136: Single Number
Companies: Amazon, Google, Apple, Microsoft, Meta, Bloomberg
Time Complexity: O(N) - Single XOR reduction over all N numbers.
Space Complexity: O(1) - Single accumulator variable `res`.
Intuition: XOR has the properties `a ^ a = 0` and `a ^ 0 = a`. XORing all numbers together cancels every duplicate pair to `0`, leaving only the unique number!
Why Efficient: Achieves O(N) time and strict O(1) memory without a hash set.
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
