"""
LeetCode 853: Car Fleet
Companies: Google, Amazon, Uber, Stripe, Microsoft
Time Complexity: O(N log N) - Dominated by sorting cars by starting position.
Space Complexity: O(N) - Stack/list stores arrival times of distinct car fleets.
Intuition: Sort cars from closest-to-target to farthest. Compute each car's arrival time `(target - pos) / speed`; if a car behind arrives sooner or equal to the fleet ahead, it merges into that fleet.
Why Efficient: Processing from front to back turns collision simulation into a simple arrival-time comparison on a stack.
"""
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in pairs:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
