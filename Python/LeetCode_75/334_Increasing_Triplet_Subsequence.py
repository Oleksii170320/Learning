"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        min_num = float('inf')
        min_num2 = float('inf')

        for i in range(len(nums)):
            if nums[i] <= min_num:
                min_num = nums[i]
            elif nums[i] <= min_num2:
                min_num2 = nums[i]
            else:
                return True
        return False

nums = [20,100,10,12,5,13]

w = Solution()
print(w.increasingTriplet(nums))
