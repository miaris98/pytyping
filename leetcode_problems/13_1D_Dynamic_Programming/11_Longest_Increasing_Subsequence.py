"""
LeetCode 300: Longest Increasing Subsequence
Companies: Google, Amazon, TikTok, Microsoft, Meta, Oracle
Time Complexity: O(N log N) - Patience sorting with binary search (`bisect_left`).
Space Complexity: O(N) - `tails` array storing the smallest tail of all increasing subsequences of each length.
Intuition: Maintain a sorted `tails` list where `tails[k]` is the smallest ending value of an increasing subsequence of length `k + 1`. Use binary search (`bisect_left`) to replace or append each number.
Why Efficient: Standard DP takes O(N²) time. Binary searching the `tails` array reduces runtime to O(N log N)!
"""
from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)
