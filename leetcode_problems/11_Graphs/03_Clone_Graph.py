"""
LeetCode 133: Clone Graph
Companies: Meta, Amazon, Google, Bloomberg, Microsoft, Pinterest
Time Complexity: O(V + E) - Visits every vertex V and edge E once.
Space Complexity: O(V) - Hash map `old_to_new` stores cloned nodes and prevents infinite cycles.
Intuition: Use a hash map `old_to_new` during DFS: if `node` is already cloned, return `old_to_new[node]`; otherwise create its clone, register it in the map, and recursively clone its neighbors.
Why Efficient: Registering the clone in `old_to_new` BEFORE recursing on neighbors breaks undirected graph cycles immediately.
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old_to_new = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in old_to_new:
                return old_to_new[curr]
            copy = Node(curr.val)
            old_to_new[curr] = copy
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
