grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
n = len(grid)
hash = {}
pairs = 0

for i in range(n):
    row = tuple(grid[i])
    hash[row] = hash.get(row, 0) + 1

for j in range(n):
    column = tuple(grid[i][j] for i in range(n))
    print(column)

