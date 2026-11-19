"""
LeetCode 17: Letter Combinations of a Phone Number
Companies: Amazon, Meta, Microsoft, Google, Apple, Uber, Epic Systems
Time Complexity: O(N * 4^N) - At most 4 letters per digit across N digits.
Space Complexity: O(N) - Recursion depth of length N.
Intuition: Map each digit `'2'..'9'` to its keypad letters and backtrack character by character from index `0` to `len(digits)`.
Why Efficient: Cleanly builds combinations of exact length N in a single depth-first traversal.
"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res, path = [], []

        def backtrack(i: int):
            if i == len(digits):
                res.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res
