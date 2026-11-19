"""
LeetCode 207: Course Schedule
Companies: Amazon, Meta, Google, Microsoft, TikTok, Palantir, Uber
Time Complexity: O(V + E) - Visits each course V and prerequisite edge E once.
Space Complexity: O(V + E) - Adjacency list and cycle-detection state.
Intuition: Model courses as a directed graph and run DFS cycle detection. Clear `pre_map[crs] = []` once a course is verified cycle-free so it is never re-checked.
Why Efficient: Memoizing verified courses by emptying `pre_map[crs] = []` prevents redundant traversals, running in O(V + E) linear graph time.
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visiting = set()

        def dfs(crs: int) -> bool:
            if crs in visiting:
                return False
            if not pre_map[crs]:
                return True
            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pre_map[crs] = []
            return True

        return all(dfs(c) for c in range(numCourses))
