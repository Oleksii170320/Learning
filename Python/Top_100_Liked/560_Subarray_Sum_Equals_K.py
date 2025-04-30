"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from collections import defaultdict
from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res = 0
#
#         if not nums:
#             return 0
#         elif k in nums:
#             res += nums.count(k)
#             while k in nums:
#                 nums.remove(k)
#             while max(nums) >= k:
#                 nums.remove(max(nums))
#             nums = sorted(nums)
#
#         print(nums)
#         return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_dict = defaultdict(int)
        curr = 0
        res = 0
        sums_dict[0] = 1

        for num in nums:
            curr += num
            res += sums_dict[curr - k]
            sums_dict[curr] += 1

        return res


nums = [2, 1, 1, 1, 2, 3, 3, 4, 5]
k = 3

w = Solution()
print(w.subarraySum(nums, k))
