"""
LeetCode 787: Cheapest Flights Within K Stops
Companies: Amazon, Airbnb, Google, Uber, Bloomberg, Meta
Time Complexity: O(K * E) - Bellman-Ford relaxation over `k + 1` rounds across E flights.
Space Complexity: O(N) - Two price arrays of length `n`.
Intuition: Run `k + 1` iterations of Bellman-Ford edge relaxation using a `tmp_prices` copy so each round only extends paths by at most 1 flight edge.
Why Efficient: Standard Dijkstra can discard a more expensive path that uses fewer stops. Bellman-Ford with `k + 1` rounds strictly enforces the stop limit in O(K * E) time.
"""
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, w in flights:
                if prices[u] != float("inf") and prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp
        return prices[dst] if prices[dst] != float("inf") else -1
