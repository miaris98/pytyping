"""
LeetCode 43: Multiply Strings
Companies: Meta, Microsoft, Amazon, Google, Apple, Yandex
Time Complexity: O(M * N) - Grade-school digit-by-digit multiplication.
Space Complexity: O(M + N) - Result digit array of length `len(num1) + len(num2)`.
Intuition: Multiplying `num1[i]` and `num2[j]` from reversed strings contributes directly to positions `res[i + j]` (ones place) and `res[i + j + 1]` (carry).
Why Efficient: Accumulates products directly into a fixed `M + N` array without intermediate string additions.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return "".join(map(str, res[::-1]))
