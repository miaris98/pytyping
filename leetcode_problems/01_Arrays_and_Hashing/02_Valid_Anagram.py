"""
LeetCode 242: Valid Anagram
Companies: Amazon, Bloomberg, Meta, Google, Spotify, Microsoft
Time Complexity: O(N) - Two linear passes over strings of length N.
Space Complexity: O(1) - At most 26 lowercase English character keys in the frequency map.
Intuition: Two strings are anagrams iff they have the exact same length and identical character frequency counts.
Why Efficient: Sorting both strings costs O(N log N). Counting frequencies in a hash map achieves optimal O(N) time and O(1) bounded alphabet space.
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        for char in t:
            count[char] -= 1
            if count[char] < 0:
                return False
        return True
