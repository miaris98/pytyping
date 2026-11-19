"""
LeetCode 190: Reverse Bits
Companies: Apple, Amazon, Qualcomm, Nvidia, Meta
Time Complexity: O(1) - Fixed 32 iterations for a 32-bit unsigned integer.
Space Complexity: O(1) - Constant bitwise accumulator.
Intuition: For each bit position `i` from 0 to 31, extract the `i`-th bit `(n >> i) & 1` and shift it into its mirrored position `31 - i`.
Why Efficient: Constant-time 32-bit manipulation without string conversion.
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)
        return res
