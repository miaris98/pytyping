"""
LeetCode 128: Longest Consecutive Sequence
Companies: Google, Amazon, Meta, Bloomberg, Microsoft, Apple, Spotify
Time Complexity: O(N) - Each number is visited at most twice (once in outer loop, once in inner streak).
Space Complexity: O(N) - Hash set stores all unique numbers for O(1) lookups.
Intuition: Put all numbers in a Set. Only start counting a consecutive streak `x, x+1, x+2...` if `x - 1` is NOT in the set (meaning `x` is the true start of a sequence).
Why Efficient: Sorting costs O(N log N). Checking `if (num - 1) not in num_set` ensures we never redundantly count from the middle of a sequence, guaranteeing O(N) runtime.
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
