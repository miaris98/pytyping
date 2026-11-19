"""
LeetCode 62: Unique Paths
Companies: Amazon, Google, Meta, Microsoft, Cisco, Bloomberg
Time Complexity: O(M * N) - Computes each grid cell once.
Space Complexity: O(N) - Single 1D row array updated in-place.
Intuition: Paths to `(r, c)` equal `paths(r-1, c) + paths(r, c-1)`. Maintain a single row `row[c] += row[c - 1]`.
Why Efficient: Compresses the 2D `M × N` DP table into a single 1D row of length N.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[-1]
