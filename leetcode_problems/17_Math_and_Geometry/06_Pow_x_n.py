"""
LeetCode 50: Pow(x, n)
Companies: Meta, Amazon, Bloomberg, Google, LinkedIn, Apple, Microsoft
Time Complexity: O(log N) - Binary exponentiation halves the exponent each step.
Space Complexity: O(1) - Iterative squaring loop.
Intuition: Binary Exponentiation: `x^n = (x * x)^(n // 2)`. Whenever `n` is odd, multiply `res *= x`; then square `x *= x` and halve `n //= 2`.
Why Efficient: Multiplying `x` N times takes O(N) time and times out for `n = 2^31`. Squaring halves the exponent every step for O(log N) speed.
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
