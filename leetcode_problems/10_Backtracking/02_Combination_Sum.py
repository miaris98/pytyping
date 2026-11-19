"""
LeetCode 39: Combination Sum
Companies: Amazon, Meta, AirBnB, Google, Microsoft, Apple, Bloomberg
Time Complexity: O(2^(T/M)) - Branches up to target T divided by minimum candidate M.
Space Complexity: O(T/M) - Maximum recursion stack depth.
Intuition: At index `i`, branch into: 1) include `candidates[i]` and stay at `i` (allowing unlimited reuse), or 2) skip `candidates[i]` and move to `i + 1` (preventing duplicate permutations).
Why Efficient: Advancing the index `i` only on the skip branch guarantees unique combinations without needing a set to deduplicate.
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []

        def dfs(i: int, total: int):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, total + candidates[i])
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res
