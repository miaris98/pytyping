"""
LeetCode 846: Hand of Straights
Companies: Google, Amazon, Straights, Rubrik
Time Complexity: O(N log N) - Frequency map plus min-heap of unique card values.
Space Complexity: O(N) - Counter dictionary and min-heap.
Intuition: The smallest remaining card `first = min_heap[0]` MUST be the start of a consecutive run `first, first+1, ..., first+groupSize-1`. Greedily decrement counts and pop exhausted values from the min-heap.
Why Efficient: Using a min-heap over unique values always anchors each group at the smallest available card in O(N log N) time.
"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]
            for card in range(first, first + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True
