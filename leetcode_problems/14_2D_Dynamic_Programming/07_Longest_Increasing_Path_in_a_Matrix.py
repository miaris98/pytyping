"""
LeetCode 329: Longest Increasing Path in a Matrix
Companies: Google, DoorDash, Amazon, Meta, TikTok, Apple
Time Complexity: O(M * N) - Memoized DFS computes each cell's longest path once.
Space Complexity: O(M * N) - 2D memoization dictionary `dp[(r, c)]`.
Intuition: Because paths must be strictly increasing, the graph is a DAG (no cycles can exist!). Run DFS with memoization `dp[(r, c)]` from every cell.
Why Efficient: Memoizing `dp[(r, c)]` ensures every cell's 4 neighbors are explored only once across the entire run, achieving O(M * N) linear time.
"""
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            val = matrix[r][c]
            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, val),
                dfs(r - 1, c, val),
                dfs(r, c + 1, val),
                dfs(r, c - 1, val),
            )
            return dp[(r, c)]

        return max(dfs(r, c, -1) for r in range(rows) for c in range(cols))
