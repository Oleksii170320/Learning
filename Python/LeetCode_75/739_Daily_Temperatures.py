"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        ind = temperatures[-1]
        for i in range(len(temperatures) -2, -1, -1):
            t1 = temperatures[i]
            if temperatures[i] >= ind:
                ind = temperatures[i]
                continue
            j = i+1
            while temperatures[j] <= temperatures[i]:
                j += res[j]
            res[i] = j-i
        return res


temperatures = [73,74,75,71,69,72,76,73]
w = Solution()
print(w.dailyTemperatures(temperatures))
