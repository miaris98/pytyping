"""
LeetCode 198: House Robber
Companies: Amazon, Cisco, Google, Apple, Microsoft, Meta
Time Complexity: O(N) - Single pass over N houses.
Space Complexity: O(1) - Tracks only `rob1` (two houses back) and `rob2` (one house back).
Intuition: At each house `n`, decide between robbing it (`n + rob1`) or skipping it (`rob2`): `new_max = max(n + rob1, rob2)`.
Why Efficient: Reduces O(2^N) branching and O(N) DP table space to two rolling integers in O(1) space.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2
