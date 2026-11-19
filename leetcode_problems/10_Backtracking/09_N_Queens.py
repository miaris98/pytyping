"""
LeetCode 51: N-Queens
Companies: Amazon, Meta, Google, Microsoft, Apple, Bloomberg
Time Complexity: O(N!) - Places one queen per row while pruning occupied columns and diagonals.
Space Complexity: O(N²) - Board state and 3 constraint sets (`cols`, `pos_diag`, `neg_diag`).
Intuition: Place one queen per row `r`. All cells on the same positive diagonal share `r + c`, and all cells on the same negative diagonal share `r - c`—allowing O(1) conflict checks with three Sets!
Why Efficient: Checking board diagonals by scanning takes O(N) per cell; tracking `r + c` and `r - c` in sets makes conflict checks O(1).
"""
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos_diag, neg_diag = set(), set(), set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
