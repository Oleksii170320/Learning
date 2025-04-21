"""
Given a string s and an integer k, return the maximum number of
vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""
from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        cur_v = max_v = sum([1 for x in s[:k] if x in vowels])
        for i in range(0, len(s) - k):
            cur_v += (s[i + k] in vowels) - (s[i] in vowels)
            if cur_v > max_v:
                max_v = cur_v
        return max_v


s = "tyqfwxeejdgqs"
k = 3

w = Solution()
print(w.maxVowels(s, k))
