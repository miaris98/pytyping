"""
LeetCode 572: Subtree of Another Tree
Companies: Amazon, Meta, Microsoft, Google, Ebay
Time Complexity: O(N * M) - Checks `isSame` of size M at nodes of `root` of size N.
Space Complexity: O(H) - Recursion stack depth of `root`.
Intuition: Traverse `root`; at each node, check if the subtree rooted there is identical to `subRoot` using `isSameTree`.
Why Efficient: Clean recursive decomposition with immediate short-circuiting on mismatched root values.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        return False
