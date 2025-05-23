"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to
target is less than 150 combinations for the given input.
"""
from typing import List


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#
#         def backtrack(pat, target, start):
#             if target == 0:
#                 res.append(list(pat))
#                 return
#             elif target < 0:
#                 return
#             else:
#                 for i in range(start, len(candidates)):
#                     pat.append(candidates[i])
#                     backtrack(pat, target - candidates[i], i)
#                     pat.pop()
#
#         backtrack([], target, 0)
#
#         return res



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        def thing(curr, total, startFrom):
            nonlocal res
            nonlocal target
            nonlocal candidates
            for count in range(startFrom, len(candidates)):
                item = candidates[count]
                if total + item == target:
                    res.append(curr + [item])
                elif total + item < target:
                    thing(curr + [item], total + item, count)
                else:
                    break
        thing([], 0, 0)
        return res


candidates = [2, 3, 6, 7]
target = 7

w = Solution()
print(w.combinationSum(candidates, target))

