"""
LeetCode 210: Course Schedule II
Companies: Amazon, Google, Meta, Microsoft, Robinhood, TikTok, DoorDash
Time Complexity: O(V + E) - Postorder topological sort visits each vertex and edge once.
Space Complexity: O(V + E) - Adjacency list plus `visited` and `cycle` sets.
Intuition: Run Postorder DFS: a course can only be appended to the topological order AFTER all of its prerequisites have been appended. Detect cycles via a `cycle` active-path set.
Why Efficient: Produces a valid topological ordering and detects cycles in a single O(V + E) DFS pass.
"""
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visit, cycle = set(), set()

        def dfs(crs: int) -> bool:
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
