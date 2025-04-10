"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        result = []
        if product == 1:
            return nums
        elif product != 0:
            for i in range(len(nums)):
                result.append(product//nums[i])
            return result
        else:
            for i in range(len(nums)):
                result.append(math.prod(nums[:i]+nums[i+1:]))
            return result


nums = [-1,1,0,-3,3]

w = Solution()
print(w.productExceptSelf(nums))
