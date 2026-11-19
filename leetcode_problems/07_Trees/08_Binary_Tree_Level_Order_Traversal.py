"""
LeetCode 102: Binary Tree Level Order Traversal
Companies: Amazon, Meta, Microsoft, Bloomberg, LinkedIn, Apple, Google
Time Complexity: O(N) - Every node is enqueued and dequeued exactly once.
Space Complexity: O(N) - Queue holds at most one full level (up to N/2 nodes).
Intuition: Use Breadth-First Search (BFS) with a `deque`. At the start of each iteration, `len(q)` tells us the exact number of nodes in the current level.
Why Efficient: `collections.deque.popleft()` operates in O(1) time (unlike `list.pop(0)` which is O(N)), ensuring true O(N) level-order traversal.
"""
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
