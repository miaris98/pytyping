"""
LeetCode 104: Maximum Depth of Binary Tree
Companies: Amazon, LinkedIn, Meta, Google, Microsoft, Apple
Time Complexity: O(N) - Visits all N nodes once.
Space Complexity: O(H) - Call stack depth equals tree height H.
Intuition: The depth of a tree is `1 + max(maxDepth(root.left), maxDepth(root.right))`.
Why Efficient: Optimal O(N) divide-and-conquer DFS.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
