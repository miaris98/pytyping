"""
LeetCode 253: Meeting Rooms II
Companies: Amazon, Bloomberg, Meta, Google, Uber, Microsoft, Apple, Snap
Time Complexity: O(N log N) - Sorts separate start and end arrays and sweeps with two pointers.
Space Complexity: O(N) - Sorted `starts` and `ends` lists.
Intuition: Separate all `starts` and `ends` into two sorted arrays. Walk through chronologically: each start before the earliest end increments active rooms (`count += 1`), while an end frees a room (`count -= 1`).
Why Efficient: Two-pointer chronological sweep avoids heap push/pop overhead while tracking the exact peak concurrent meetings.
"""
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        res = count = s = e = 0
        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
