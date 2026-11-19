"""
LeetCode 621: Task Scheduler
Companies: Meta, Amazon, Google, Uber, Microsoft, DoorDash, Rubrik
Time Complexity: O(N) - Counts task frequencies and simulates cooldown cycles using a max-heap and queue.
Space Complexity: O(1) - At most 26 uppercase task types in the heap and cooldown queue.
Intuition: Always schedule the most frequent available task first (via a Max-Heap), then place its remaining count into a cooldown `deque` `(remaining_count, available_time)` until `time + n`.
Why Efficient: Greedily picking the highest-frequency task prevents getting stuck with identical tasks at the end, minimizing idle CPU cycles in O(N) time.
"""
from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
