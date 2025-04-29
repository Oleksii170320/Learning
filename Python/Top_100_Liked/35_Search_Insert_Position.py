"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List

# class Solution:
#     def searchInsert(self, nums, target):
#         n = len(nums)
#         low = 0
#         high = n-1
#         ans = n
#         while(low <= high):
#             mid = (low+high)//2
#             if nums[mid] >= target :
#                 ans = mid
#                 high = mid-1
#             else:
#                 low = mid+1
#         return ans


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target < min(nums):
            return 0
        elif len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        else:
            if target in nums:
                return nums.index(target)
            else:
                if max(nums) > target:
                    for i in range(0, len(nums)):
                        r = nums[i]
                        if nums[i] > target:
                            return i
                else:
                    return len(nums)


nums = [1, 3, 5, 6]
target = 2

w = Solution()
print(w.searchInsert(nums, target))
