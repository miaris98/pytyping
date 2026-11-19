"""
LeetCode 261: Graph Valid Tree
Companies: LinkedIn, Amazon, Google, Meta, Microsoft
Time Complexity: O(V + E) - Union-Find with path compression and rank.
Space Complexity: O(V) - Parent array for N nodes.
Intuition: An undirected graph of `n` nodes is a valid tree iff it has exactly `n - 1` edges and contains no cycles (so all `n - 1` edges unite two previously disconnected components).
Why Efficient: Checking `len(edges) == n - 1` plus Union-Find cycle detection validates both connectivity and acyclicity in nearly O(N) time.
"""
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
        return True
