"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in reversed(range(n)):
            output[i] *= right_product
            right_product *= nums[i]

        return output


nums = [1, 2, 3, 4]

w = Solution()
print(w.productExceptSelf(nums))
