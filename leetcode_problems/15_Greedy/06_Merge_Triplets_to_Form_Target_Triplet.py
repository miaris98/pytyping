"""
LeetCode 1899: Merge Triplets to Form Target Triplet
Companies: Google, Amazon
Time Complexity: O(N) - Single filter and match pass over N triplets.
Space Complexity: O(1) - Set of at most 3 matched coordinate indices `{0, 1, 2}`.
Intuition: Any triplet with a value exceeding `target` in ANY position is unusable (since `max` can never shrink it). Among usable triplets, check if `target[0]`, `target[1]`, and `target[2]` each appear at least once.
Why Efficient: Single O(N) pass with O(1) space.
"""
from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
