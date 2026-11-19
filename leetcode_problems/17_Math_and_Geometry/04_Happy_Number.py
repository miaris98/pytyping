"""
LeetCode 202: Happy Number
Companies: Amazon, Google, Apple, Uber, Bloomberg, PayPal
Time Complexity: O(log N) - Digit-square transitions quickly drop below 243 and terminate or cycle.
Space Complexity: O(1) - Floyd's Tortoise and Hare cycle detection.
Intuition: Repeatedly replace `n` with the sum of squares of its digits. Use `slow` and `fast` pointers to detect whether the sequence reaches `1` or enters a cycle.
Why Efficient: Floyd's cycle detection avoids storing seen numbers in a hash set, running in O(1) memory.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            total = 0
            while x:
                x, d = divmod(x, 10)
                total += d * d
            return total

        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1
