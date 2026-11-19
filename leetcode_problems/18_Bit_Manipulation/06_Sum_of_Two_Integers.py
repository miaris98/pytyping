"""
LeetCode 371: Sum of Two Integers
Companies: Meta, Amazon, Apple, Microsoft, Hulu
Time Complexity: O(1) - At most 32 bitwise carry-propagation iterations.
Space Complexity: O(1) - 32-bit mask constants.
Intuition: Bitwise XOR `(a ^ b)` computes addition without carry, while `((a & b) << 1)` computes the carry bits. Repeat with a 32-bit mask `0xFFFFFFFF` until carry `b == 0`.
Why Efficient: Simulates hardware half-adder logic using pure bitwise operations without `+` or `-`.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_int else ~(a ^ mask)
