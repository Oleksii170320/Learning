"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        b=[]
        d=1
        for i in range(1,len(chars)):
            if(chars[i]==chars[i-1]):
                d+=1
            else:
                b.append(chars[i-1])
                if(d>1):
                    n=str(d)
                    for p in n:
                        b.append(p)
                    d=1
        b.append(chars[-1])
        if d > 1:
            for p in str(d):
                b.append(p)
        chars.clear()
        for i in b:
            chars.append(i)
        return len(chars)


chars = ["a", "a", "b", "b", "c", "c", "c"]

w = Solution()
print(w.compress(chars))
