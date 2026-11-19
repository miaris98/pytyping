"""
LeetCode 695: Max Area of Island
Companies: Amazon, Meta, Google, DoorDash, Bloomberg, Microsoft
Time Complexity: O(M * N) - Each cell is visited at most once by DFS.
Space Complexity: O(M * N) - Recursion stack depth in the worst case.
Intuition: Run DFS on each unvisited land cell `'1'`, sinking it to `0` and summing `1 + area_of_4_neighbors`.
Why Efficient: In-place sinking (`grid[r][c] = 0`) counts each island's area in O(M * N) total time without extra visited storage.
"""
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        return max((dfs(r, c) for r in range(rows) for c in range(cols)), default=0)
