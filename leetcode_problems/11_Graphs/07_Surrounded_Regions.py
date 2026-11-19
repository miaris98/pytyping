"""
LeetCode 130: Surrounded Regions
Companies: Amazon, Google, Meta, TikTok, Bloomberg
Time Complexity: O(M * N) - Border DFS plus single grid sweep.
Space Complexity: O(M * N) - Worst-case recursion stack.
Intuition: Any `'O'` region connected to the border can NEVER be surrounded. Run DFS from all border `'O'` cells to mark them `'T'` (safe), flip remaining interior `'O'`s to `'X'`, and restore `'T'`s back to `'O'`.
Why Efficient: In-place `'T'` marking distinguishes border-connected `'O'`s from captured interior `'O'`s without an extra visited matrix.
"""
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == "O":
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
