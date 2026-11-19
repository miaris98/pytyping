"""
LeetCode 167: Two Sum II - Input Array Is Sorted
Companies: Amazon, Google, Meta, Apple, Microsoft, Bloomberg
Time Complexity: O(N) - Each step moves either `left` forward or `right` backward at most N times.
Space Complexity: O(1) - Zero auxiliary data structures used.
Intuition: Start pointers at the smallest (`left = 0`) and largest (`right = n - 1`) values. If their sum is too small, increment `left`; if too large, decrement `right`.
Why Efficient: Exploits the sorted property to achieve O(N) runtime with O(1) constant memory instead of an O(N) hash table.
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                return [left + 1, right + 1]
            elif cur < target:
                left += 1
            else:
                right -= 1
        return []
