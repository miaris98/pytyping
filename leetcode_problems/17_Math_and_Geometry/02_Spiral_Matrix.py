"""
LeetCode 54: Spiral Matrix
Companies: Amazon, Microsoft, Apple, Meta, Google, Cisco, Bloomberg
Time Complexity: O(M * N) - Visits every cell in the matrix exactly once.
Space Complexity: O(1) - Four boundary pointers `left`, `right`, `top`, `bottom`.
Intuition: Maintain four shrinking boundaries (`top`, `bottom`, `left`, `right`). Sweep right across `top`, down along `right`, left across `bottom`, and up along `left`, shrinking each boundary after its sweep.
Why Efficient: Cleanly handles non-square matrices in O(1) auxiliary space.
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
