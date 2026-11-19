"""
LeetCode 10: Regular Expression Matching
Companies: Meta, Google, Amazon, Microsoft, Nvidia, Apple, Coursera
Time Complexity: O(M * N) - Memoized top-down DP over indices `(i, j)`.
Space Complexity: O(M * N) - Cache dictionary storing `(i, j)` states.
Intuition: When the next pattern char is `'*'` (`p[j+1] == '*'`), branch into skipping `x*` (`dfs(i, j + 2)`) or consuming one matching char from `s` (`match and dfs(i + 1, j)`).
Why Efficient: Memoizing `(i, j)` prevents exponential backtracking when multiple `*` wildcards appear.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)
