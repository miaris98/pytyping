"""
LeetCode 226: Invert Binary Tree
Companies: Google, Amazon, Meta, Apple, Microsoft, Bloomberg
Time Complexity: O(N) - Visits every node in the tree once.
Space Complexity: O(H) - Recursion call stack proportional to tree height H.
Intuition: Recursively swap the left and right child pointers of every node in the tree.
Why Efficient: Visits each node once in O(N) time with a single clean tuple swap.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
