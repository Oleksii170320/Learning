"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            nums.sort()
            res = 1
            step = 1
            for i in range(1, len(nums)):
                if nums[i - 1] == nums[i]:
                    continue
                if nums[i - 1] + 1 == nums[i]:
                    step += 1
                else:
                    res = max(res, step)
                    step = 1

            res = max(res, step)
            return res


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]

w = Solution()
print(w.longestConsecutive(nums))
