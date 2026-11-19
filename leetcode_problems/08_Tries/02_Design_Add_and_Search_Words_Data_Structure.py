"""
LeetCode 211: Design Add and Search Words Data Structure
Companies: Meta, Amazon, Google, Apple, Rubrik, DoorDash
Time Complexity: O(L) for `addWord` and exact `search`; O(26^W * L) when W wildcard dots `.` appear.
Space Complexity: O(N * L) - Trie storage plus O(L) recursion stack for wildcard branching.
Intuition: Store words in a Trie. During `search`, normal characters step into `curr.children[ch]`, while a wildcard `'.'` recursively branches across all `curr.children.values()`.
Why Efficient: Prunes non-matching prefixes immediately in the Trie instead of scanning every stored word on wildcard queries.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx: int, node: TrieNode) -> bool:
            curr = node
            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    return any(dfs(i + 1, child) for child in curr.children.values())
                if ch not in curr.children:
                    return False
                curr = curr.children[ch]
            return curr.is_end

        return dfs(0, self.root)
