"""
LeetCode 778: Swim in Rising Water
Companies: Google, Amazon, Meta, DoorDash, Uber
Time Complexity: O(N² log N) - Modified Dijkstra minimizing the maximum elevation along the path.
Space Complexity: O(N²) - Min-heap and `visit` set.
Intuition: Run Dijkstra where the cost of stepping onto `(nr, nc)` is `max(current_max_height, grid[nr][nc])`. Always expand the frontier cell with the lowest bottleneck elevation.
Why Efficient: Finds the minimax bottleneck path directly in O(N² log N) time.
"""
from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = {(0, 0)}
        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))
        return -1
