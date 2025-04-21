"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        if len(temperatures) == 0:
            res.append(0)
        elif len(temperatures) > 0:
            c = 0
            for i in range(len(temperatures) - 1):
                for t in range(i + 1, len(temperatures)):
                    t1 = temperatures[i]
                    t2 = temperatures[t]
                    if temperatures[i] <= temperatures[t]:
                        c += 1
                        res.append(c)
                        break
                    elif temperatures[i] > temperatures[t]:
                        c += 1
                        if len(temperatures) - i == 2:
                            res.append(0)

                c = 0
            res.append(0)
        return res


temperatures = [73,74,75,71,69,72,76,73]
w = Solution()
print(w.dailyTemperatures(temperatures))