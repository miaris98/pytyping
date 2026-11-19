"""
LeetCode 57: Insert Interval
Companies: Google, LinkedIn, Amazon, Meta, Robinhood, Uber, Apple
Time Complexity: O(N) - Single pass over already-sorted intervals.
Space Complexity: O(N) - Output list of merged intervals.
Intuition: For each interval: if it ends strictly before `newInterval`, append it; if it starts strictly after `newInterval`, append `newInterval` and return with the rest; otherwise merge them via `[min(starts), max(ends)]`.
Why Efficient: Exploits the pre-sorted order to insert and merge in O(N) time without re-sorting.
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (s, e) in enumerate(intervals):
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > e:
                res.append([s, e])
            else:
                newInterval = [min(newInterval[0], s), max(newInterval[1], e)]
        res.append(newInterval)
        return res
