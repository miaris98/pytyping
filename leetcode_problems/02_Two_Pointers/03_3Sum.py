"""
LeetCode 15: 3Sum
Companies: Meta, Amazon, Google, Microsoft, Apple, Bloomberg, Uber, Adobe
Time Complexity: O(N²) - O(N log N) sort plus N iterations of an O(N) two-pointer sweep.
Space Complexity: O(1) - In-place duplicate skipping without a hash set (excluding output list).
Intuition: Sort the array, fix the first number `nums[i]`, and run a Two-Pointer search on `i+1..n-1` for `-nums[i]`, skipping adjacent duplicates.
Why Efficient: Reduces O(N³) triple-loop brute force to O(N²) and avoids high-memory hash sets by skipping duplicate adjacent sorted elements.
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
