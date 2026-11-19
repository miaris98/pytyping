"""
LeetCode 70: Climbing Stairs
Companies: Amazon, Google, Adobe, Apple, Microsoft, Meta, Bloomberg
Time Complexity: O(N) - Single loop from 3 to N.
Space Complexity: O(1) - Rolling Fibonacci state variables.
Intuition: Ways to reach step `i` is `ways(i - 1) + ways(i - 2)`. Track only the last two values.
Why Efficient: Collapses O(2^N) recursion and O(N) DP array space down to O(N) time and O(1) space.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 2, 1
        for _ in range(3, n + 1):
            one, two = one + two, one
        return one
