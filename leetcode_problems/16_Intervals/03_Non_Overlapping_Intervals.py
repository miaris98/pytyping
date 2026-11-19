"""
LeetCode 435: Non-overlapping Intervals
Companies: Amazon, Meta, Google, JPMorgan, Microsoft
Time Complexity: O(N log N) - Sort by start/end time plus O(N) greedy sweep.
Space Complexity: O(1) - Tracks only `prev_end` and `removals`.
Intuition: When two intervals overlap (`start < prev_end`), greedily remove the interval with the LARGER end time (`prev_end = min(prev_end, end)`) so it is less likely to collide with future intervals.
Why Efficient: Greedy earliest-end selection is provably optimal and runs in O(N log N) time with O(1) extra space.
"""
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)
        return res
