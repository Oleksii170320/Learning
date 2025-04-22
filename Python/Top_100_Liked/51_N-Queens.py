"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
indicate a queen and an empty space, respectively.
"""
from typing import List
from itertools import permutations


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return sol[n]


def solveQueens(n):
    backing = [0] * n
    result = []

    def good(pos):
        i = pos
        bi = backing[pos]
        for j, bj in enumerate(backing[:pos]):
            if bi == bj:
                return False
            if abs(i - j) == abs(bi - bj):
                return False
        return True

    def bkt(pos):
        if pos >= n:
            result.append(generate(backing))
            return

        for i in range(n):
            backing[pos] = i
            if good(pos):
                bkt(pos + 1)

    bkt(0)
    return result


def generate(backing):
    N = len(backing)
    res = [["."] * N for _ in range(N)]
    for i, b in enumerate(backing):
        res[i][b] = "Q"
    return ["".join(d) for d in res]


sol = {d: solveQueens(d) for d in range(1, 10)}

n = 4

w = Solution()
print(w.solveNQueens(n))

