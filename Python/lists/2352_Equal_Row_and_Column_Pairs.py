"""
Given a 0-indexed n x n integer matrix grid, return the number of
pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same
elements in the same order (i.e., an equal array).
"""
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hash = {}
        pairs = 0

        for i in range(n):
            row = tuple(grid[i])
            hash[row] = hash.get(row, 0) + 1

        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            if column in hash:
                pairs += hash[column]

        return pairs


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

w = Solution()
print(w.equalPairs(grid))
