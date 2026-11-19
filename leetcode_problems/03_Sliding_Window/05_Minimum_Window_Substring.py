"""
LeetCode 76: Minimum Window Substring
Companies: Meta, Airbnb, Amazon, Google, LinkedIn, Uber, Microsoft, Lyft
Time Complexity: O(N + M) - Each character in `s` is visited at most twice (`right` and `left`).
Space Complexity: O(1) - Frequency maps bounded by the ASCII character set.
Intuition: Expand `right` until all required character counts (`have == need`) are satisfied, then greedily contract `left` to find the smallest valid window.
Why Efficient: Tracking `have` vs `need` integer counters lets us verify window validity in O(1) time instead of comparing entire hash maps on every step.
"""
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need_map = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(need_map)
        res, res_len = [-1, -1], float("inf")
        left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need_map and window[ch] == need_map[ch]:
                have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in need_map and window[s[left]] < need_map[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
