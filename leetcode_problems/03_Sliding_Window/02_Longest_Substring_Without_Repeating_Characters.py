"""
LeetCode 3: Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_length = 0
        left = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length\n