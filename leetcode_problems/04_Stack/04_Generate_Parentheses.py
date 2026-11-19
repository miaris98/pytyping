"""
LeetCode 22: Generate Parentheses
Companies: Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Uber
Time Complexity: O(4^N / sqrt(N)) - Generates only valid Catalan-number sequences.
Space Complexity: O(N) - Recursion stack depth and current path list of length 2N.
Intuition: Backtrack by tracking `open_n` and `close_n` counts: add `'('` if `open_n < n`, and add `')'` only if `close_n < open_n`.
Why Efficient: Prunes invalid bracket prefixes immediately instead of generating all 2^(2N) strings and filtering them afterward.
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def backtrack(open_n: int, close_n: int):
            if open_n == close_n == n:
                res.append("".join(stack))
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, close_n)
                stack.pop()
            if close_n < open_n:
                stack.append(")")
                backtrack(open_n, close_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res
