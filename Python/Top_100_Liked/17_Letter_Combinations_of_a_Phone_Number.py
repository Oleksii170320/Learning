"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""
from typing import List, Dict
import string


def alphaNums(self) -> Dict:
    alpha = string.ascii_lowercase
    d = {}
    c = 0

    for i in range(10):
        if i in (0, 1):
            continue
        else:
            world = str()
            if i in (7, 9):
                for j in range(c, c + 4):
                    world += alpha[j]
                    c += 1
            else:
                for j in range(c, c + 3):
                    world += alpha[j]
                    c += 1
            d[i] = world
    return d

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         a = alphaNums(self)
#         lett_list = []
#         res = []
#
#         for i in digits:
#             lett_list.append(a[int(i)])
#
#         if len(digits) == 0:
#             return []
#         elif len(digits) == 1:
#             return list(a[int(digits)])
#         elif len(digits) == 2:
#             k = lett_list[0]
#             m = lett_list[1]
#             for i in range(len(k)):
#                 for j in range(len(m)):
#                     res.append(f"{k[i]}{m[j]}")
#         elif len(digits) == 3:
#             k = lett_list[0]
#             m = lett_list[1]
#             l = lett_list[2]
#             for i in range(len(k)):
#                 for j in range(len(m)):
#                     for p in range(len(l)):
#                         res.append(f"{k[i]}{m[j]}{l[p]}")
#         elif len(digits) == 4:
#             k = lett_list[0]
#             m = lett_list[1]
#             l = lett_list[2]
#             f = lett_list[3]
#             for i in range(len(k)):
#                 for j in range(len(m)):
#                     for p in range(len(l)):
#                         for g in range(len(f)):
#                             res.append(f"{k[i]}{m[j]}{l[p]}{f[g]}")
#         return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = alphaNums(self)

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb[:])
                return

            for letter in digit_to_letters[int(digits[int(idx)])]:
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")

        return res

digits = "23"

w = Solution()
print(w.letterCombinations(digits))

