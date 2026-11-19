"""
LeetCode 7: Reverse Integer
Companies: Amazon, Apple, Adobe, Google, Bloomberg, Microsoft, Meta
Time Complexity: O(log₁₀ X) - Processes at most 10 base-10 digits.
Space Complexity: O(1) - Scalar accumulator and 32-bit overflow bounds.
Intuition: Pop the last digit `digit = x % 10` and push it onto `res = res * 10 + digit`, checking before the final step if `res` would overflow signed 32-bit bounds `[-2^31, 2^31 - 1]`.
Why Efficient: Checks overflow mathematically before multiplying by 10 in O(1) space.
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            x, digit = divmod(x, 10)
            res = res * 10 + digit
        res *= sign
        return res if -(2**31) <= res <= 2**31 - 1 else 0
