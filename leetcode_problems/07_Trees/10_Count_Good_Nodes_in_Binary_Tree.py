"""
LeetCode 1448: Count Good Nodes in Binary Tree
Companies: Microsoft, Amazon, Meta, Google, Apple
Time Complexity: O(N) - Preorder DFS visits each node once.
Space Complexity: O(H) - Call stack depth equals tree height H.
Intuition: Pass the maximum value seen along the path from root (`max_so_far`) down the DFS recursion. A node is 'good' if `node.val >= max_so_far`.
Why Efficient: Carrying `max_so_far` as a scalar parameter avoids storing or re-scanning ancestor paths, solving the problem in O(N) time.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)
