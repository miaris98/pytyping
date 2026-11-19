"""
LeetCode 543: Diameter of Binary Tree
Companies: Meta, Amazon, Google, Microsoft, Apple, Bloomberg
Time Complexity: O(N) - Computes height and updates diameter in a single bottom-up DFS pass.
Space Complexity: O(H) - Recursion stack depth of height H.
Intuition: At every node, the longest path passing through that node is `left_height + right_height`. Track the global maximum while returning `1 + max(left_height, right_height)` upward.
Why Efficient: Recomputing `maxDepth` at every node would take O(N²) time. Computing height and diameter simultaneously in bottom-up DFS runs in O(N) time.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter
