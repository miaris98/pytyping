"""
LeetCode 3: Longest Substring Without Repeating Characters
Companies: Amazon, Meta, Google, Microsoft, Bloomberg, Apple, Uber, Spotify
Time Complexity: O(N) - Single pass with O(1) hash map index jumps.
Space Complexity: O(min(N, M)) - Dictionary stores at most one index per unique character in the charset.
Intuition: Maintain a sliding window `[left, right]` of unique characters. Store each character's latest index so `left` can jump straight past any duplicate.
Why Efficient: Jumping `left = char_index[char] + 1` via a hash map avoids incrementing `left` one by one, completing in strictly N iterations.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
