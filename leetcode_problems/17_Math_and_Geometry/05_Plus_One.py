"""
LeetCode 66: Plus One
Companies: Google, Amazon, Microsoft, Meta, Apple
Time Complexity: O(N) - Scans from the rightmost digit and exits early as soon as a non-9 digit is found.
Space Complexity: O(1) - Mutates `digits` in-place.
Intuition: Walk right-to-left: if `digits[i] < 9`, increment `digits[i] += 1` and return immediately; otherwise set `digits[i] = 0` and carry left. If all digits were `9`, return `[1] + digits`.
Why Efficient: Handles carries in-place without string/integer conversion.
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
