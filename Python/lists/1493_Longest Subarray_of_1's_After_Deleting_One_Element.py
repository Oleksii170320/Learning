"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == 0:
            return 0

        if nums.count(0) == 0:
            return len(nums) - 1

        max_len = 0
        prev_len = 0
        now_len = 0

        for i in nums:
            if i == 1:
                now_len += 1
            else:
                max_len = max(max_len, prev_len + now_len)
                prev_len = now_len
                now_len = 0

        max_len = max(max_len, prev_len + now_len)

        return max_len


nums = [0]

w = Solution()
print(w.longestSubarray(nums))
