"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
from collections import defaultdict
from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = []
#         lists = set()
#
#         for word in strs:
#             item = ''.join(sorted(word))
#             lists.add(item)
#
#         for _ in range(len(lists)):
#             res.append([])
#
#         set_list = list(lists)
#
#         for word in strs:
#             sort_word = ''.join(sorted(word))
#             index = set_list.index(sort_word)
#
#             if sort_word in set_list:
#                 res[index].append(word)
#
#         return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = defaultdict(list)

        for st in strs:
            sortedst = "".join(sorted(st))
            hashed[sortedst].append(st)

        return [ss for ss in hashed.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

w = Solution()
print(w.groupAnagrams(strs))
