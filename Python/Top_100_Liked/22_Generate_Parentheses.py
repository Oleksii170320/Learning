"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def backtrack(op, cl):
            if len(sol) == 2 * n:
                res.append("".join(sol))
                return

            if op < n:
                sol.append('(')
                backtrack(op + 1, cl)
                sol.pop()

            if cl < op:
                sol.append(')')
                backtrack(op, cl+1)
                sol.pop()


        backtrack(0, 0)
        return res


n = 3

w = Solution()
print(w.generateParenthesis(n))

