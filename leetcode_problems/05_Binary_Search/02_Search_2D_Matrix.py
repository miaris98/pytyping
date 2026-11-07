"""
LeetCode 74: Search a 2D Matrix
You are given an m x n integer matrix matrix with the properties that integers in each row are sorted from left to right, and the first integer of each row is greater than the last integer of the previous row.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
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
        return False\n