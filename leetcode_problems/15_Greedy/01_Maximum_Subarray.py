"""
LeetCode 53: Maximum Subarray
Companies: LinkedIn, Amazon, Apple, Microsoft, Meta, Google, Bloomberg, Cisco
Time Complexity: O(N) - Kadane's single-pass algorithm.
Space Complexity: O(1) - Two scalar variables `cur_sum` and `max_sub`.
Intuition: Kadane's Algorithm: whenever the running prefix sum `cur_sum` becomes negative, reset it to `0` because a negative prefix can only hurt any future subarray.
Why Efficient: Solves maximum contiguous sum in a single O(N) pass with O(1) memory instead of O(N²) prefix scans.
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(max_sub, cur_sum)
        return max_sub
