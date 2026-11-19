"""
LeetCode 217: Contains Duplicate
Companies: Amazon, Google, Apple, Microsoft, Meta, Bloomberg
Time Complexity: O(N) - Single pass over N elements with O(1) average hash set lookups.
Space Complexity: O(N) - Hash set stores up to N unique elements in the worst case.
Intuition: Use a Hash Set to remember seen numbers and answer membership queries in O(1) time.
Why Efficient: Brute-force takes O(N²) and sorting takes O(N log N). A hash set runs in O(N) time and terminates early on the first duplicate.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
