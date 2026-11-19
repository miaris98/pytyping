"""
LeetCode 212: Word Search II
Companies: Amazon, Uber, Karat, Microsoft, Google, Meta, Cisco
Time Complexity: O(M * N * 4 * 3^(L-1)) - Simultaneous Trie-guided DFS across the grid.
Space Complexity: O(W * L) - Trie storing W words of max length L.
Intuition: Insert all target words into a single Trie, then run DFS from each board cell stepping only into board neighbors that exist in the current `TrieNode.children`.
Why Efficient: Running separate Word Search for W words repeats grid traversals W times. A shared Trie searches for all W words simultaneously and prunes dead-end prefixes on the first mismatched letter.
"""
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for ch in w:
                curr = curr.children.setdefault(ch, TrieNode())
            curr.word = w

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, parent: TrieNode):
            ch = board[r][c]
            curr = parent.children.get(ch)
            if not curr:
                return
            if curr.word:
                res.append(curr.word)
                curr.word = None
            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr.children:
                    dfs(nr, nc, curr)
            board[r][c] = ch
            if not curr.children:
                parent.children.pop(ch)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return res
