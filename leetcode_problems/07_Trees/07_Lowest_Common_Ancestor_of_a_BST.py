"""
LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
Companies: LinkedIn, Meta, Amazon, Microsoft, Google, Bloomberg
Time Complexity: O(H) - Walks down one path of height H in the BST.
Space Complexity: O(1) - Iterative pointer traversal uses zero call stack memory.
Intuition: In a BST, if both `p` and `q` are greater than `curr.val`, move right; if both are smaller, move left. The first node where they split (or equal `curr`) is the LCA!
Why Efficient: Exploits the BST ordering property to walk directly down one path in O(H) time and O(1) space without visiting the rest of the tree.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
