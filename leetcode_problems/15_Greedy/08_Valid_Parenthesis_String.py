"""
LeetCode 678: Valid Parenthesis String
Companies: Amazon, Meta, Yahoo, Google, LinkedIn, Apple
Time Complexity: O(N) - Single pass tracking `[left_min, left_max]` range.
Space Complexity: O(1) - Two integer range variables.
Intuition: Track the range `[left_min, left_max]` of possible unmatched open parentheses: `'('` increments both, `')'` decrements both, and `'*'` decrements `left_min` and increments `left_max` (clamping `left_min = max(left_min, 0)`).
Why Efficient: Reduces O(3^N) wildcard branching and O(N²) DP down to O(N) time and O(1) space.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        for ch in s:
            if ch == "(":
                left_min, left_max = left_min + 1, left_max + 1
            elif ch == ")":
                left_min, left_max = left_min - 1, left_max - 1
            else:
                left_min, left_max = left_min - 1, left_max + 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0
