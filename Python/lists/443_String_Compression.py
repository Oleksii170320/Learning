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
        i = 0
        cnt = 1

        for j in range(1, len(chars)):
            if chars[i] != chars[j]:
                if cnt > 1:
                    for c in str(cnt):
                        i += 1
                        chars[i] = c

                i += 1
                chars[i] = chars[j]
                cnt = 1
            else:
                cnt += 1

        if cnt > 1:
            for c in str(cnt):
                i += 1
                chars[i] = f"{c}"

        return i + 1


chars = ["a", "a", "b", "b", "c", "c", "c"]

w = Solution()
print(w.compress(chars))
