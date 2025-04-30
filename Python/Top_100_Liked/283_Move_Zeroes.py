"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        else:
            en = 0
            for st in range(len(nums)):
                if nums[en] != 0:
                    en += 1
                elif nums[st] != 0:
                    nums[st], nums[en] = nums[en], nums[st]
                    en += 1

        return nums



nums = [0,1,0,3,12]

w = Solution()
print(w.moveZeroes(nums))
