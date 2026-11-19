"""
LeetCode 323: Number of Connected Components in an Undirected Graph
Companies: Amazon, LinkedIn, Google, Meta, Microsoft, Pinterest
Time Complexity: O(V + E * alpha(V)) - Union-Find with path compression and union by rank.
Space Complexity: O(V) - `parent` and `rank` arrays of size `n`.
Intuition: Start with `n` isolated components. For every edge `(a, b)`, if `find(a) != find(b)`, union their roots and decrement the component count by 1.
Why Efficient: Union-Find with path compression processes edges in near-constant O(alpha(N)) time without building adjacency lists.
"""
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        res = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                if rank[ra] < rank[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                rank[ra] += rank[rb]
                res -= 1
        return res
