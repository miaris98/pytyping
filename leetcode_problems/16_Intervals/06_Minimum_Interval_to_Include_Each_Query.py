"""
LeetCode 1851: Minimum Interval to Include Each Query
Companies: Google, Amazon, Bloomberg
Time Complexity: O(N log N + Q log Q) - Offline sorted queries with a min-heap of active intervals.
Space Complexity: O(N + Q) - Min-heap of `(size, right_end)` and query answers.
Intuition: Sort both `intervals` and `queries`. For each query `q`, push all intervals starting `<= q` into a Min-Heap keyed by `(interval_size, right_end)`, and pop expired intervals where `right_end < q`.
Why Efficient: Offline sorting + min-heap processes all Q queries and N intervals in a single pass instead of O(N * Q) brute force.
"""
from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]
