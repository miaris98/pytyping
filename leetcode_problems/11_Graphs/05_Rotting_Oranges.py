"""
LeetCode 994: Rotting Oranges
Companies: Amazon, Microsoft, Meta, Google, TikTok, Bloomberg, Uber
Time Complexity: O(M * N) - Multi-source BFS across the grid.
Space Complexity: O(M * N) - BFS queue of rotten orange coordinates.
Intuition: Count `fresh` oranges and push all initially rotten oranges (`2`) into a queue. Expand level-by-level (1 minute per BFS level), decrementing `fresh` as neighbors rot.
Why Efficient: Multi-source BFS simulates simultaneous rot spreading from multiple sources in a single O(M * N) pass.
"""
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
