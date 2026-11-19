"""
LeetCode 417: Pacific Atlantic Water Flow
Companies: Google, Amazon, Meta, Microsoft, Bloomberg, Uber
Time Complexity: O(M * N) - Two ocean-inward DFS traversals visit each cell at most twice.
Space Complexity: O(M * N) - Two reachability sets (`pac` and `atl`) plus recursion stack.
Intuition: Instead of flowing downhill from every cell, start at the Pacific border and Atlantic border and walk UPHILL (`height >= prev_height`) to find all cells reachable from each ocean, then return `pac & atl`.
Why Efficient: Reversing the flow from borders inward reduces O((M*N)²) per-cell searches to just two O(M * N) traversals.
"""
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visit: set, prev_h: int):
            if (
                (r, c) in visit
                or r < 0 or r >= rows or c < 0 or c >= cols
                or heights[r][c] < prev_h
            ):
                return
            visit.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        return [[r, c] for r, c in pac & atl]
