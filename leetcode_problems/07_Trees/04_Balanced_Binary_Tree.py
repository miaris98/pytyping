"""
LeetCode 110: Balanced Binary Tree
Companies: Amazon, Google, Meta, Spotify, Adobe
Time Complexity: O(N) - Single bottom-up DFS returning `-1` immediately on imbalance.
Space Complexity: O(H) - Call stack proportional to tree height H.
Intuition: Return the subtree height if balanced, or `-1` as a sentinel value as soon as any subtree has `abs(left - right) > 1`.
Why Efficient: Top-down height checks cost O(N²). Bottom-up DFS with a `-1` sentinel checks balance and height in a single O(N) pass.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) != -1
