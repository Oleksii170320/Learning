"""
You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = max(height)
        water = 0

        while left < right:
            water = max(water, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            if water > max_height*(right-left):
                return water
        return water


height = [1,8,6,2,5,4,8,3,7]

w = Solution()
print(w.maxArea(height))
