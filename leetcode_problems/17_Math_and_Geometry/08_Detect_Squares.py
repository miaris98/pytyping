"""
LeetCode 2013: Detect Squares
Companies: Google, Amazon, Goldman Sachs
Time Complexity: O(1) for `add`, O(N) for `count` by checking diagonal points.
Space Complexity: O(N) - Counter map of `(x, y)` point frequencies.
Intuition: To count axis-aligned squares with query point `(px, py)`, iterate over each stored point `(x, y)`: if it forms a valid non-zero square diagonal (`abs(py - y) == abs(px - x)` and `x != px`), multiply the counts of the other two required corners `(x, py)` and `(px, y)`.
Why Efficient: Iterating only over diagonal candidates fixes the side length immediately, reducing 3-corner search to O(1) hash lookups per point.
"""
from typing import List
from collections import Counter

class DetectSquares:
    def __init__(self):
        self.pts_count = Counter()

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in self.pts_count.items():
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            res += cnt * self.pts_count[(x, py)] * self.pts_count[(px, y)]
        return res
