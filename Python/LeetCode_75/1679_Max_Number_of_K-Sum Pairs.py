"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1
        operation = 0

        while l < r:
            if ((nums[l] + nums[r]) == k):
                operation += 1
                l +=1
                r -=1
            elif((nums[l] + nums[r]) < k):
                l += 1
            else:
                r -= 1
        return operation


nums = [1,2,3,4]
k = 5

w = Solution()
print(w.maxOperations(nums, k))
