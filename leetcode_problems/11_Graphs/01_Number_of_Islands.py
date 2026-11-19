"""
LeetCode 200: Number of Islands
Companies: Amazon, Bloomberg, Meta, Google, Microsoft, Uber, Apple
Time Complexity: O(M * N) - Visits each grid cell a constant number of times.
Space Complexity: O(M * N) - Worst-case recursion stack depth when grid is all land.
Intuition: Scan the grid; whenever `'1'` is found, increment `islands` and run DFS flood-fill to sink connected `'1'`s to `'0'`.
Why Efficient: Sinking visited land cells to `'0'` in-place avoids allocating an O(M * N) `visited` set.
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands
