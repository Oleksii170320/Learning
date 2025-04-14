"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing the relative positions of
the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        for i in range(len(s)):
            found = False

            while j < len(t):
                if s[i] == t[j]:
                    found = True
                    j += 1
                    break

                j += 1

            if not found:
                return False

        return True


s = "ab"
t = "baab"

w = Solution()
print(w.isSubsequence(s, t))
