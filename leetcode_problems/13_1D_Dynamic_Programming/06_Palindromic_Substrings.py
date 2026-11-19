"""
LeetCode 647: Palindromic Substrings
Companies: Meta, Amazon, Google, Goldman Sachs, Microsoft
Time Complexity: O(N²) - Expands around each odd and even center.
Space Complexity: O(1) - Constant space counters.
Intuition: Expand outward `(l -= 1, r += 1)` from every odd center `(i, i)` and even center `(i, i + 1)`, incrementing `count` for every matching pair.
Why Efficient: Counts all palindromes in O(N²) time and O(1) space without a 2D boolean table.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count
