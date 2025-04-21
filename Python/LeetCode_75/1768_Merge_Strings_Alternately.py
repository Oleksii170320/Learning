"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end
of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''

        for i in range(max(len(word1), len(word2))):
            if i >= len(word2):
                res += word1[i]
            elif i >= len(word1):
                res += word2[i]
            else:
                res += word1[i]
                res += word2[i]

        return res

word1 = str(input("Введіть перше слово: "))
word2 = str(input("Введіть друге слово: "))

w = Solution()
print(w.mergeAlternately(word1, word2))
