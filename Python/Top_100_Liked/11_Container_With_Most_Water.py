"""
You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        marea=0
        l=0
        r=len(height)-1
        while(l<r):
            mn=min(height[l],height[r])
            marea=max(marea,mn*(r-l))
            while l<r and height[l]<=mn:
                l+=1
            while l<r and height[r]<=mn:
                r-=1
        return marea



height = [1,8,6,2,5,4,8,3,7]

w = Solution()
print(w.maxArea(height))
