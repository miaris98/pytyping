"""
LeetCode 131: Palindrome Partitioning
Companies: Google, Amazon, Meta, Apple, Adobe, TikTok
Time Complexity: O(N * 2^N) - Explores partitioning cuts and verifies palindrome substrings.
Space Complexity: O(N) - Recursion stack and current partition list.
Intuition: Try every prefix `s[i:j+1]` starting at `i`. If that prefix is a palindrome (`sub == sub[::-1]`), add it to `part` and recursively partition the suffix starting at `j + 1`.
Why Efficient: Prunes non-palindrome prefixes immediately without exploring their suffixes.
"""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i: int):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if sub == sub[::-1]:
                    part.append(sub)
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
