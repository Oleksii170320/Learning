"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not target in nums:
            return [-1, -1]
        else:
            res = [0, 0]
            count_target = nums.count(target)

            if count_target == 1:
                res[0] = res[1] = nums.index(target)
            else:
                res[0] = nums.index(target)
                cur = 0
                for i in range(0, len(nums)):

                    if nums[i] == target:
                        cur += 1
                        if cur == count_target: res[1] = i
            return res


nums = [5, 7, 7, 8, 8, 10]
target = 8

w = Solution()
print(w.searchRange(nums, target))
