"""
LeetCode 424: Longest Repeating Character Replacement
Companies: Google, Amazon, Meta, Uber, Microsoft, Bloomberg
Time Complexity: O(N) - Both `left` and `right` pointers advance at most N times.
Space Complexity: O(1) - Frequency dictionary stores at most 26 uppercase English letters.
Intuition: A window is valid if `(window_length - max_frequency_char_count) <= k`. Expand `right` and only shift `left` by 1 when replacements needed exceed `k`.
Why Efficient: We never need to decrement `max_freq` when shrinking because only a strictly larger `max_freq` can ever produce a longer valid window—keeping the check O(1).
"""
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0
        for right, char in enumerate(s):
            count[char] += 1
            max_freq = max(max_freq, count[char])
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
