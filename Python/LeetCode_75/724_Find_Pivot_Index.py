"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the i
ndex is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are
no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s, count = sum(nums), 0

        for i in range(len(nums)):
            count += nums[i]
            if count == s:
                return i
            s -= nums[i]

        return -1



nums = [1, 7, 3, 6, 5, 6]


w = Solution()
print(w.pivotIndex(nums))
