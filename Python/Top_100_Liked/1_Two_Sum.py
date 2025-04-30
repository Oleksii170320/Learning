"""
Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         res = []
#
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if not i == j:
#                     if nums[i] + nums[j] == target:
#                         res.append(i)
#                         res.append(j)
#                         return res


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, num in enumerate(nums):
            if target - num in dp:
                return [i, dp[target - num]]
            else:
                dp[num] = i


nums = [2, 7, 11, 15]
target = 9

w = Solution()
print(w.twoSum(nums, target))
