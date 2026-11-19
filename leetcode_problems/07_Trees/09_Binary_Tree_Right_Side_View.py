"""
LeetCode 199: Binary Tree Right Side View
Companies: Meta, Amazon, Bloomberg, TikTok, Microsoft, ByteDance
Time Complexity: O(N) - BFS visits each node once.
Space Complexity: O(W) - Queue stores at most the maximum width W of the tree.
Intuition: Perform level-order BFS and record the very last node processed in each level (`i == level_len - 1`).
Why Efficient: Captures the rightmost visible node at every depth even when the right subtree is shorter than the left subtree.
"""
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                if i == level_len - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
