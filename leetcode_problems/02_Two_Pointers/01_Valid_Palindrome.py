"""
LeetCode 125: Valid Palindrome
Companies: Meta, Amazon, Microsoft, Apple, Google, Bloomberg
Time Complexity: O(N) - Left and right pointers cross after visiting each character once.
Space Complexity: O(1) - Compares characters in-place without allocating a filtered copy.
Intuition: Walk two pointers inward from both ends of the string, skipping non-alphanumeric characters and comparing lowercase characters.
Why Efficient: Building a new filtered string and reversing it allocates O(N) extra memory. Two pointers validate the string in-place in O(1) space.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
