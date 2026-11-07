"""
LeetCode 49: Group Anagrams
Given an array of strings strs, group the anagrams together.
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
        return list(groups.values())\n