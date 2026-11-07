"""
LeetCode 242: Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
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
        return True\n