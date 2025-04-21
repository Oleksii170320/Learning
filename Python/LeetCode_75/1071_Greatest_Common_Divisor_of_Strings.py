"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # if str1+ str2 is not equal to str2 + str1 that means we are not same, so we return an empty str
            return ""
        size = math.gcd(len(str1), len(str2)) # calculating gcd and storing it in size
        return str1[:size] # returning str1 till size non inclusive because we're using ':'


str1 = str(input("Введіть перше слово: "))
str2 = str(input("Введіть друге слово: "))

w = Solution()
print(w.gcdOfStrings(str1, str2))
