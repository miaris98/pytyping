"""
LeetCode 79: Word Search
Companies: Amazon, Bloomberg, Karat, Uber, Microsoft, Meta, Snap
Time Complexity: O(M * N * 4 * 3^(L-1)) - DFS from each grid cell up to word length L.
Space Complexity: O(L) - Recursion stack of depth L; marks visited cells in-place on `board`.
Intuition: From each cell matching `word[0]`, run 4-directional DFS. Temporarily overwrite `board[r][c] = '#'` to mark it visited on the current path, then restore it on backtrack.
Why Efficient: In-place `#` marking avoids allocating a `visited` set and checks visited status in O(1) array indexing.
"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp, board[r][c] = board[r][c], "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = tmp
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
