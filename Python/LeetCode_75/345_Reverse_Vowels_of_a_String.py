"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in list(s):
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels.append(i)

        result = []
        for i in list(s):
            result.append(i) if i.lower() not in ['a', 'e', 'i', 'o', 'u'] else result.append(vowels.pop())

        return ''.join(result)


s = 'IceCreAm'
print(s)
w = Solution()
print(w.reverseVowels(s))
