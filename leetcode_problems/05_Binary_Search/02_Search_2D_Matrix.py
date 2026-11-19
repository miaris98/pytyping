"""
LeetCode 74: Search a 2D Matrix
Companies: Amazon, Microsoft, Meta, Google, Apple, Bloomberg
Time Complexity: O(log(M * N)) - Binary search across M * N virtual 1D indices.
Space Complexity: O(1) - Maps 1D index to 2D `(row, col)` using `divmod(mid, n)` in-place.
Intuition: Treat the M × N sorted matrix as a virtual 1D sorted array of length `M * N`, converting any 1D midpoint `mid` to `(mid // n, mid % n)`.
Why Efficient: Achieves logarithmic O(log M + log N) time without flattening or copying the matrix.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
