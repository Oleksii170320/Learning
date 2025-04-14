"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in
the array if you can flip at most k 0's.
"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for num in nums:
            if num == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return len(nums)-left


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

w = Solution()
print(w.longestOnes(nums, k))
