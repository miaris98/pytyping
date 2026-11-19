"""
LeetCode 20: Valid Parentheses
Companies: Amazon, Meta, Google, Bloomberg, Microsoft, Apple, Spotify
Time Complexity: O(N) - Single pass pushing and popping each character at most once.
Space Complexity: O(N) - Stack holds up to N opening brackets in the worst case.
Intuition: Use a LIFO Stack for open brackets. When encountering a closing bracket, verify the top of the stack matches its required opening partner.
Why Efficient: Processes nested brackets in one O(N) pass with O(1) per-character stack operations.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
