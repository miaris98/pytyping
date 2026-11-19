"""
LeetCode 567: Permutation in String
Companies: Microsoft, Amazon, Meta, Google, Oracle, Uber
Time Complexity: O(N) - Fixed-size sliding window updates in O(1) per character.
Space Complexity: O(1) - Two fixed-size frequency arrays of length 26.
Intuition: Slide a window of length `len(s1)` across `s2`, maintaining character counts for `'a'..'z'` and checking when both frequency profiles match.
Why Efficient: Generating permutations takes O(N!) and sorting each window takes O(N * M log M). Fixed 26-slot frequency arrays run in O(N) time and O(1) space.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
        if c1 == c2:
            return True
        for i in range(len(s1), len(s2)):
            c2[ord(s2[i]) - ord('a')] += 1
            c2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if c1 == c2:
                return True
        return False
