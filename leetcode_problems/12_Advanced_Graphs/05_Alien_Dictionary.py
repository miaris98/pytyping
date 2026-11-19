"""
LeetCode 269: Alien Dictionary
Companies: Airbnb, Meta, Google, Amazon, Uber, Pinterest, Microsoft
Time Complexity: O(C) - Total characters C across all words to build graph and topologically sort.
Space Complexity: O(U) - At most 26 unique letters in adjacency sets.
Intuition: Compare adjacent words `w1, w2` to find the first differing character `w1[j] -> w2[j]`, then run topological sort (with cycle and invalid-prefix detection).
Why Efficient: Only adjacent word pairs are needed because transitivity covers all non-adjacent pairs, building the graph in linear O(C) time.
"""
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {ch: set() for w in words for ch in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []

        def dfs(ch: str) -> bool:
            if ch in visit:
                return visit[ch]
            visit[ch] = True
            for nei in adj[ch]:
                if dfs(nei):
                    return True
            visit[ch] = False
            res.append(ch)
            return False

        for ch in adj:
            if dfs(ch):
                return ""
        return "".join(reversed(res))
