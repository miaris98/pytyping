"""
LeetCode 4: Median of Two Sorted Arrays
Companies: Google, Amazon, Meta, Goldman Sachs, Microsoft, Apple, Bloomberg
Time Complexity: O(log(min(M, N))) - Binary searches the partition point on the smaller array.
Space Complexity: O(1) - Only index and boundary variables used.
Intuition: Binary search the partition cut `i` in the smaller array `A` (which automatically fixes cut `j = half - i` in `B`) until `A_left <= B_right` and `B_left <= A_right`.
Why Efficient: Merging both arrays takes O(M + N) time. Binary searching the partition on the shorter array achieves the theoretical optimal O(log(min(M, N))) time and O(1) space.
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        low, high = 0, len(A) - 1
        while True:
            i = (low + high) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return float(min(Aright, Bright))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1
