"""
LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
Companies: Amazon, Microsoft, Bloomberg, Google, Meta
Time Complexity: O(N) - Pre-maps inorder indices in a dict and builds each of the N nodes in O(1).
Space Complexity: O(N) - Dictionary of N inorder indices plus O(H) recursion stack.
Intuition: The next element in `preorder` is always the root of the current subtree, and its index in `inorder` splits the remaining elements into the left and right subtrees.
Why Efficient: Slicing lists and calling `inorder.index()` on every call takes O(N²) time. Pre-building an `inorder_idx` hash map and passing index bounds reduces construction to O(N) time!
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_idx[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)
