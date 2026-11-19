"""
LeetCode 763: Partition Labels
Companies: Amazon, Meta, Google, LinkedIn, Nvidia
Time Complexity: O(N) - One pass to record last indices, one pass to cut partitions.
Space Complexity: O(1) - Dictionary of at most 26 lowercase character last-occurrence indices.
Intuition: Precompute `last[ch]` for every character. As we scan `i`, extend the current partition's right boundary `end = max(end, last[s[i]])`. When `i == end`, close the partition!
Why Efficient: Finds all minimal self-contained partitions in two O(N) passes with O(1) space.
"""
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        size = end = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, last[ch])
            if i == end:
                res.append(size)
                size = 0
        return res
