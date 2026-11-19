"""
LeetCode 127: Word Ladder
Companies: Amazon, Meta, LinkedIn, Google, Microsoft, Uber, Box
Time Complexity: O(N * M²) - N words of length M indexed by wildcard patterns.
Space Complexity: O(N * M²) - Pattern adjacency dictionary `{*ot: [hot, dot, lot]}`.
Intuition: Group words by wildcard patterns (e.g. `h*t`, `*ot`, `ho*`), then run unweighted BFS from `beginWord` to find the shortest transformation sequence to `endWord`.
Why Efficient: Comparing all pairs of N words takes O(N² * M). Grouping by M wildcard patterns reduces neighbor lookup to O(M²) per word!
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                nei[word[:j] + "*" + word[j + 1 :]].append(word)
        visit = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                for next_word in nei[pattern]:
                    if next_word not in visit:
                        visit.add(next_word)
                        q.append((next_word, steps + 1))
                nei[pattern].clear()
        return 0
