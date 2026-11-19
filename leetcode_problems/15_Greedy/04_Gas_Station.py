"""
LeetCode 134: Gas Station
Companies: Amazon, Microsoft, Google, Bloomberg, Apple, Goldman Sachs
Time Complexity: O(N) - Single greedy pass over all stations.
Space Complexity: O(1) - Scalar `total` and `start` variables.
Intuition: If `sum(gas) < sum(cost)`, no solution exists. Otherwise, maintain a running `tank`; whenever `tank < 0` at index `i`, none of the stations up to `i` can be the start, so reset `start = i + 1` and `tank = 0`.
Why Efficient: Eliminates the entire failed prefix at once instead of restarting from every station in O(N²) time.
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start
