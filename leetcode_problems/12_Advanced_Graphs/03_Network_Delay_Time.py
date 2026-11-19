"""
LeetCode 743: Network Delay Time
Companies: Amazon, Google, Akuna Capital, Uber, Microsoft
Time Complexity: O(E log V) - Dijkstra's shortest-path algorithm with a min-heap.
Space Complexity: O(V + E) - Adjacency list, `visit` set, and priority queue.
Intuition: Use Dijkstra's algorithm with a Min-Heap `(accumulated_time, node)` from source `k`. The time when the last unvisited node is popped is the total network delay.
Why Efficient: Dijkstra's min-heap guarantees the first time each node is popped is its true shortest path from `k`.
"""
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        min_heap = [(0, k)]
        visit = set()
        t = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        return t if len(visit) == n else -1
