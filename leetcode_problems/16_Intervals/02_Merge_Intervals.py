"""
LeetCode 56: Merge Intervals
Companies: Meta, Amazon, Google, Bloomberg, Salesforce, Microsoft, Uber, Apple
Time Complexity: O(N log N) - Sort by start time followed by O(N) linear merge.
Space Complexity: O(N) - Output list of merged intervals.
Intuition: Sort intervals by start time. If the current interval's `start` is `<=` the previous merged interval's `end`, extend the previous interval's `end = max(prev_end, end)`.
Why Efficient: Sorting by start time ensures all overlapping intervals become contiguous, allowing a single O(N) merge pass.
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output
