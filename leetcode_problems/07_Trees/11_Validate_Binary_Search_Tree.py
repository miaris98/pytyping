"""
LeetCode 98: Validate Binary Search Tree
Companies: Amazon, Bloomberg, Microsoft, Meta, Google, Salesforce
Time Complexity: O(N) - Visits every node once with O(1) range comparison.
Space Complexity: O(H) - Recursion stack depth of height H.
Intuition: Every node in a valid BST must fall within a strict open interval `(low, high)` inherited from its ancestors: going left tightens `high = node.val`, going right tightens `low = node.val`.
Why Efficient: Checking only immediate children fails on deeper invalid descendants. Propagating `(low, high)` bounds validates the entire tree in one O(N) pass.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))
