"""
LeetCode 684: Redundant Connection
Companies: Amazon, Google, Apple, Microsoft, Meta
Time Complexity: O(N * alpha(N)) - Single pass over N edges with Union-Find.
Space Complexity: O(N) - Disjoint set `parent` and `rank` arrays.
Intuition: Process edges in order using Union-Find. The first edge `(u, v)` whose endpoints already share the same root (`find(u) == find(v)`) closes a cycle and is the redundant edge!
Why Efficient: Repeatedly running DFS for each edge takes O(N²). Union-Find detects the cycle-closing edge in near-linear O(N) time.
"""
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u, v]
            parent[ru] = rv
        return []
