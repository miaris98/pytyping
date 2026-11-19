"""
LeetCode 230: Kth Smallest Element in a BST
Companies: Uber, Amazon, Meta, Microsoft, Google, Apple
Time Complexity: O(H + k) - Walks down to the smallest leaf in O(H) and pops `k` nodes.
Space Complexity: O(H) - Iterative stack holds at most H ancestor nodes.
Intuition: Inorder traversal (`Left -> Node -> Right`) of a BST visits values in strictly sorted ascending order. Use an explicit stack to stop immediately at the `k`-th popped node.
Why Efficient: Iterative inorder stops as soon as the `k`-th element is found in O(H + k) time without traversing the entire N-node tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        return -1
