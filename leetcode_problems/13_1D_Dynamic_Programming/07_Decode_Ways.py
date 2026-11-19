"""
LeetCode 91: Decode Ways
Companies: Amazon, Cisco, Google, Meta, TikTok, Uber, Lyft
Time Complexity: O(N) - Single backward DP pass.
Space Complexity: O(1) - Two rolling variables `dp1` and `dp2`.
Intuition: At index `i`, if `s[i] != '0'`, we can decode 1 digit (`dp1` ways), plus if `10 <= int(s[i:i+2]) <= 26`, we can also decode 2 digits (`dp2` ways).
Why Efficient: Processes 1-digit and 2-digit transitions in O(N) time and O(1) space.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0
        for i in range(len(s) - 1, -1, -1):
            cur = 0 if s[i] == "0" else dp1
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cur += dp2
            dp1, dp2 = cur, dp1
        return dp1
