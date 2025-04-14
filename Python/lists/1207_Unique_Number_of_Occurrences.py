"""
Given an array of integers arr, return true if the number of
occurrences of each value in the array is unique or false otherwise.
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        unic = set(d.values())
        return len(unic) == len(d.values())



arr = [1,2,2,1,1,3]

w = Solution()
print(w.uniqueOccurrences(arr))
