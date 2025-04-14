"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
ny answer with a calculation error less than 10-5 will be accepted.
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: list, k: int) -> float:
        cur_avg = sum(nums[:k])
        max_avg = cur_avg
        for i in range(k,len(nums)) :
            cur_avg += nums[i] - nums[i-k]
            if cur_avg > max_avg :
                max_avg = cur_avg
        return max_avg/k


nums = [1,12,-5,-6,50,3]
k = 4

w = Solution()
print(w.findMaxAverage(nums, k))
