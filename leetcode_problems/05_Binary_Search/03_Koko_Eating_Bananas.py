"""
LeetCode 875: Koko Eating Bananas
Companies: Google, Amazon, Meta, DoorDash, Airbnb, Salesforce
Time Complexity: O(N log M) - Binary search over speed range `[1..max(piles)]`, spending O(N) per check.
Space Complexity: O(1) - Only scalar boundary variables used.
Intuition: Binary search on the eating speed `k` in `[1, max(piles)]`. Since feasibility is monotonic (faster speed never takes more hours), find the minimum `k` where total hours `<= h`.
Why Efficient: Testing every speed linearly takes O(N * M) where M can be 10^9. Binary search on the answer space reduces M to log₂(M) ≈ 30 checks!
"""
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            k = (low + high) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
        return res
