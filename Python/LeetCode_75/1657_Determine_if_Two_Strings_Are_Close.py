"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another
existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wrd1 = set(word1)
        wrd2 = set(word2)
        if wrd1 != wrd2:
            return False
        sorted_wrd1 = sorted([word1.count(ch) for ch in wrd1])
        sorted_wrd2 = sorted([word2.count(ch) for ch in wrd2])
        return sorted_wrd1 == sorted_wrd2


word1 = "abc"
word2 = "bca"

w = Solution()
print(w.closeStrings(word1, word2))
