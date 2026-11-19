"""
LeetCode 5: Longest Palindromic Substring
Companies: Amazon, Microsoft, Cisco, Google, Meta, Adobe, Bloomberg, Apple
Time Complexity: O(N²) - Expands around 2N - 1 possible centers.
Space Complexity: O(1) - Tracks only best `(start, end)` indices during expansion.
Intuition: Every palindrome mirrors around its center (either a single character for odd length or between two characters for even length). Expand outward from all `2N - 1` centers.
Why Efficient: Checking all substrings takes O(N³), and 2D DP uses O(N²) space. Expanding around centers achieves O(N²) time in O(1) extra space.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0

        def expand(l: int, r: int):
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    start, max_len = l, r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start : start + max_len]
