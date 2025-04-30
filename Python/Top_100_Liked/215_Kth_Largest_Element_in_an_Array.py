"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         c = 1
#
#         while c < k:
#             c += 1
#             nums.remove(max(nums))
#
#         return max(nums)


nums = [3, 2, 1, 5, 6, 4]
k = 2

w = Solution()
print(w.findKthLargest(nums, k))
