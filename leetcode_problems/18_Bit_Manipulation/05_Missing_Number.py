"""
LeetCode 268: Missing Number
Companies: Amazon, Microsoft, Nvidia, Google, Meta, Apple
Time Complexity: O(N) - Single pass using XOR or Gauss's sum formula.
Space Complexity: O(1) - Single integer variable.
Intuition: By Gauss's formula, the expected sum of `0..n` is `n * (n + 1) // 2`. Subtracting `sum(nums)` leaves the exact missing number (or XOR `0..n` with `nums`).
Why Efficient: Finds the missing number in O(N) time and O(1) space without sorting or a hash set.
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
