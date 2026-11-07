"""
LeetCode 20: Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
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
        return len(stack) == 0\n