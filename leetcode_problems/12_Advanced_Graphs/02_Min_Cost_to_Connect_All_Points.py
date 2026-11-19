"""
LeetCode 1584: Min Cost to Connect All Points
Companies: Amazon, Microsoft, Meta, Directi
Time Complexity: O(N² log N) - Prim's Minimum Spanning Tree algorithm across N points.
Space Complexity: O(N²) - Min-heap and visited set.
Intuition: Run Prim's Minimum Spanning Tree (MST) algorithm starting from point `0`: greedily pop the cheapest edge `(cost, u)` to an unvisited point until all N points are connected.
Why Efficient: Connects all N points with minimum Manhattan distance without building and sorting all N(N-1)/2 edges upfront.
"""
from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visit = set()
        min_heap = [(0, 0)]
        total_cost = 0
        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            visit.add(i)
            total_cost += cost
            x1, y1 = points[i]
            for j in range(n):
                if j not in visit:
                    x2, y2 = points[j]
                    heapq.heappush(min_heap, (abs(x1 - x2) + abs(y1 - y2), j))
        return total_cost
