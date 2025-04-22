"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(acc):
            if len(acc) == len(nums):
                result.append(acc.copy())
                return
            for num in nums:
                if num not in acc:
                    acc.append(num)
                    backtrack(acc)
                    acc.pop()
            return

        backtrack([])

        return result

nums = [1, 2, 3]

w = Solution()
print(w.permute(nums))

