"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def back(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                back(i + 1, path)
                path.pop()

        back(0, [])
        return res


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         def backtrack(curr):
#             res.append(curr[:])
#
#             for num in nums:
#                 if len(curr)==0 or curr[-1]>num:
#                     curr.append(num)
#                     backtrack(curr)
#                     curr.pop()
#         current = []
#         backtrack(current)
#         return res


nums = [1, 2, 3]

w = Solution()
print(w.subsets(nums))
