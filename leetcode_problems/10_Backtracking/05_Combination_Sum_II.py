"""
LeetCode 40: Combination Sum II
Companies: Amazon, TikTok, Airbnb, Meta, Google, Microsoft
Time Complexity: O(2^N) - Backtracking with duplicate and sum pruning.
Space Complexity: O(N) - Recursion stack depth.
Intuition: Sort `candidates`, prune immediately when `candidates[i] > remain`, and skip duplicate siblings (`if i > start and candidates[i] == candidates[i - 1]: continue`).
Why Efficient: Sorting enables both duplicate skipping and early break pruning when the current number exceeds the remaining sum.
"""
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def backtrack(start: int, remain: int):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return res
