"""
LeetCode 191: Number of 1 Bits
Companies: Apple, Amazon, Qualcomm, Microsoft, Box, Cisco
Time Complexity: O(K) - Runs exactly K times where K is the number of set `1` bits (at most 32).
Space Complexity: O(1) - Constant space.
Intuition: Brian Kernighan's trick: `n &= (n - 1)` clears the lowest set `1` bit of `n` in a single operation. Count how many times this operation runs until `n == 0`.
Why Efficient: Skips all `0` bits completely, looping only as many times as there are `1` bits.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
