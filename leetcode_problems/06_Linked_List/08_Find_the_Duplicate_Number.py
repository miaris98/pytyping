"""
LeetCode 287: Find the Duplicate Number
Companies: Amazon, Meta, Microsoft, Google, Apple, Bloomberg
Time Complexity: O(N) - Two-phase Floyd's cycle detection.
Space Complexity: O(1) - Zero array modification and zero extra memory.
Intuition: Treat array values in `[1..n]` as `.next` pointers (`i -> nums[i]`). A duplicate value means two indices point to the same node, creating a cycle whose entrance is the duplicate!
Why Efficient: Sorting mutates the array and sets use O(N) space. Floyd's Tortoise & Hare finds the cycle entrance in O(N) time and O(1) space without modifying `nums`.
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
