"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example,
[1, 2] and [2, 3] are non-overlapping.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cur, count = float('-inf'), 0

        for x in intervals:
            if x[0] >= cur:
                cur = x[1]
            else:
                count += 1
        return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]


w = Solution()
print(w.eraseOverlapIntervals(intervals))
