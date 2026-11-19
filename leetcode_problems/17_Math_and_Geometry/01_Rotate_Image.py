"""
LeetCode 48: Rotate Image
Companies: Amazon, Cisco, Microsoft, Apple, Meta, Google, Bloomberg
Time Complexity: O(N²) - Visits each matrix cell once.
Space Complexity: O(1) - In-place transpose followed by horizontal row reversal.
Intuition: A 90-degree clockwise rotation is mathematically equivalent to: 1) Transposing the matrix across its main diagonal (`matrix[r][c] <-> matrix[c][r]`), then 2) Reversing each row.
Why Efficient: Rotates the matrix in-place in O(1) space without complex 4-corner index arithmetic.
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()
