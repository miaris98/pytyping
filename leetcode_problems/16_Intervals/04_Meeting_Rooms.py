"""
LeetCode 252: Meeting Rooms
Companies: Amazon, Google, Meta, Bloomberg, Microsoft
Time Complexity: O(N log N) - Sorts intervals by start time and checks adjacent pairs.
Space Complexity: O(1) - In-place sort and constant comparison.
Intuition: Sort meetings by start time and verify that every meeting finishes before or when the next meeting begins (`intervals[i-1][1] <= intervals[i][0]`).
Why Efficient: Reduces O(N²) all-pairs overlap checks to N - 1 adjacent checks after sorting.
"""
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
