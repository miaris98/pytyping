"""
LeetCode 36: Valid Sudoku
Companies: Amazon, Apple, Microsoft, Google, Uber, Nvidia, Karat
Time Complexity: O(1) - Fixed 9x9 board (81 cells) scanned once.
Space Complexity: O(1) - Hash sets hold at most 81 entries across 9 rows, 9 cols, and 9 boxes.
Intuition: Track seen digits for each row `r`, column `c`, and 3x3 sub-box `(r // 3, c // 3)` using hash sets.
Why Efficient: Instead of 27 separate passes over the board, integer-dividing `(r // 3, c // 3)` maps any cell to its 3x3 box in O(1) time during a single pass.
"""
from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
        return True
