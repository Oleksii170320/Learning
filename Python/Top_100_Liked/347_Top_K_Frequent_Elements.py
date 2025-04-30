"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
from collections import Counter
from heapq import heapify, heappush, heappop
from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_dict = {}
#
#         for el in set(nums):
#             nums_dict[el] = nums.count(el)
#
#         l = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)
#         res = []
#
#         for key in range(k):
#             res.append(l[key][0])
#
#         return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        heapify(heap)
        for i in c:
            heappush(heap, (-c[i], i))
        ans = []
        while k:
            ans.append(heappop(heap)[1])
            k-=1
        return ans


nums = [1, 1, 1, 2, 2, 5]
k = 2

w = Solution()
print(w.topKFrequent(nums, k))
