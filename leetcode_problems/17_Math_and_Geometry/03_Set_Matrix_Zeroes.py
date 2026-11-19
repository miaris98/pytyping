"""
LeetCode 73: Set Matrix Zeroes
Companies: Amazon, Microsoft, Meta, Bloomberg, Apple, Oracle
Time Complexity: O(M * N) - Two passes over the matrix.
Space Complexity: O(1) - Uses the first row and first column of `matrix` itself as markers.
Intuition: Use `matrix[r][0]` and `matrix[0][c]` as in-place boolean flags to mark which rows and columns must be zeroed, plus a single boolean `row_zero` for row 0.
Why Efficient: Eliminates O(M + N) row/column marker arrays by storing the markers inside row 0 and col 0 in O(1) space.
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
