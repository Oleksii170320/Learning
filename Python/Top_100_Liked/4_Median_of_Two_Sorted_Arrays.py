"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)

        if len(nums) % 2 != 0:
            return float(nums[len(nums) // 2])
        else:
            n = len(nums) // 2
            return (nums[n - 1] + nums[n])/2



nums1 = [1, 3, 4]
nums2 = [2]

w = Solution()
print(w.findMedianSortedArrays(nums1, nums2))
