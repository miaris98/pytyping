"""
LeetCode 239: Sliding Window Maximum
Companies: Amazon, Google, Meta, Citadel, Uber, Microsoft, DoorDash
Time Complexity: O(N) - Every index is pushed and popped from the monotonic deque at most once.
Space Complexity: O(K) - Deque stores at most K indices from the current window.
Intuition: Maintain a Monotonic Decreasing Deque of indices: pop smaller elements from the back before pushing `right`, and pop out-of-window indices from the front.
Why Efficient: Scanning each window takes O(N * K) and a heap takes O(N log K). A monotonic deque keeps the window maximum at `dq[0]` in amortized O(1) time per step.
"""
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for right, val in enumerate(nums):
            while dq and nums[dq[-1]] < val:
                dq.pop()
            dq.append(right)
            if dq[0] <= right - k:
                dq.popleft()
            if right >= k - 1:
                res.append(nums[dq[0]])
        return res
