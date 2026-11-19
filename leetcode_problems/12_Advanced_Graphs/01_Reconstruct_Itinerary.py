"""
LeetCode 332: Reconstruct Itinerary
Companies: Uber, Netflix, Google, Meta, Amazon, Bloomberg
Time Complexity: O(E log E) - Sorting tickets plus O(E) Hierholzer's Eulerian path traversal.
Space Complexity: O(V + E) - Adjacency list and recursion stack.
Intuition: Sort tickets in reverse lexical order so `adj[src].pop()` always picks the smallest lexical destination in O(1). Use Hierholzer's postorder DFS to build the Eulerian path in reverse.
Why Efficient: Backtracking with edge removals/insertions takes exponential time on dead ends; Hierholzer's postorder DFS visits every ticket edge exactly once in O(E) time!
"""
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        res = []

        def dfs(src: str):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)

        dfs("JFK")
        return res[::-1]
