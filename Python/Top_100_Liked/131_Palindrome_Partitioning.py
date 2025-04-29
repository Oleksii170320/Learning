"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
"""
from functools import cache
from typing import List


# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         res = []
#
#         def recursion(item: int, current: list):
#             if item >= n:
#                 res.append(current)
#
#             p = ''
#             for i in range(item, n):
#                 p += s[i]
#                 if p == p[::-1]:
#                     recursion(i + 1, current + [p])
#
#         recursion(0, [])
#         return res


class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0 : return []
        if len(s) == 1 : return ((s,),)

        res = []

        for i in range(1, len(s) + 1):
            a = s[:i]
            b = s[i:]
            if a == a[::-1]:
                if len(b) == 0:
                    res.append((a,))
                else:
                    for x in self.partition(b):
                        res.append((a,) + x)
        return res

s = "aab"

w = Solution()
print(w.partition(s))
