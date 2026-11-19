"""
LeetCode 155: Min Stack
Companies: Amazon, Bloomberg, Microsoft, Google, Apple, Meta
Time Complexity: O(1) - Constant time for `push`, `pop`, `top`, and `getMin`.
Space Complexity: O(N) - Parallel `min_stack` stores the running minimum at each stack depth.
Intuition: Maintain two synchronized stacks: `stack` for values and `min_stack` where each slot stores the minimum value at or below that depth.
Why Efficient: Avoids O(N) scans when the minimum element is popped, guaranteeing strict O(1) worst-case time for all four operations.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
