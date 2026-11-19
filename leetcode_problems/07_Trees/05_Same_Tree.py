"""
LeetCode 100: Same Tree
Companies: Amazon, Google, Apple, Microsoft, LinkedIn
Time Complexity: O(N) - Visits corresponding nodes of both trees once.
Space Complexity: O(H) - Recursion stack depth of height H.
Intuition: Two trees are identical if their roots share the same value and their left and right subtrees are recursively identical.
Why Efficient: Short-circuits on the first structural or value mismatch in O(N) time.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
