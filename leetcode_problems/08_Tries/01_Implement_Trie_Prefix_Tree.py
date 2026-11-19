"""
LeetCode 208: Implement Trie (Prefix Tree)
Companies: Google, Amazon, Microsoft, Meta, Apple, Twitter, Uber
Time Complexity: O(L) - Insert, search, and startsWith each take O(L) where L is word length.
Space Complexity: O(N * L) - Total characters across inserted words stored as shared tree nodes.
Intuition: Each `TrieNode` holds a `children` dictionary mapping `{char: TrieNode}` and an `is_end` boolean flag marking complete words.
Why Efficient: Hash sets cannot answer prefix queries (`startsWith`) in O(L) without storing every prefix of every word. A Trie shares common prefixes and answers both exact and prefix queries in O(L) time.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
