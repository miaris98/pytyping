"""
LeetCode 49: Group Anagrams
Companies: Amazon, Meta, Google, Microsoft, Apple, Bloomberg, Uber
Time Complexity: O(N * K) - N words of max length K counted into 26-slot frequency tuples.
Space Complexity: O(N * K) - Hash map stores all N strings grouped by their 26-integer signature.
Intuition: All anagrams share the same 26-letter frequency count. Use the 26-count tuple as a dictionary key to bucket anagrams together.
Why Efficient: Sorting each word of length K takes O(N * K log K). Counting characters into a 26-element array drops the log K factor for optimal O(N * K) time.
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            groups[tuple(key)].append(word)
        return list(groups.values())
