"""
LeetCode 124: Binary Tree Maximum Path Sum
Companies: Meta, Amazon, DoorDash, Google, Microsoft, Bloomberg
Time Complexity: O(N) - Single postorder DFS visiting each node once.
Space Complexity: O(H) - Recursion call stack proportional to tree height H.
Intuition: At each node, compute max non-negative gains from left and right (`max(dfs(child), 0)`). Update global `max_sum` with the split path `node.val + left_gain + right_gain`, and return the single-branch max `node.val + max(left_gain, right_gain)` to the parent.
Why Efficient: Simultaneously considers every node as the 'highest apex' of a split path while passing only valid extendable single paths upward in O(N) time.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum
