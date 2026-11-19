"""
LeetCode 295: Find Median from Data Stream
Companies: Amazon, Google, Meta, Microsoft, Apple, Goldman Sachs, Bloomberg
Time Complexity: O(log N) for `addNum` and O(1) for `findMedian`.
Space Complexity: O(N) - Two heaps (`small` max-heap and `large` min-heap) split the stream in half.
Intuition: Maintain two balanced heaps: `small` (a Max-Heap holding the smaller half of numbers) and `large` (a Min-Heap holding the larger half). Their tops sit right at the median!
Why Efficient: Keeping a sorted array requires O(N) shifts on every insertion. Two heaps balance in O(log N) and expose the median at their roots in O(1) time.
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (-self.small[0] + self.large[0]) / 2.0
