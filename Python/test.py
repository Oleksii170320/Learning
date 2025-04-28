board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]

word = "ABCCED"
l = 0

for i in range(len(board)):
    if word[l] in board[i]:
        j = board[i].index(word[l])
        if word[l + 1] in board[i][int(j + 1)] or word[l + 1] in board[i+1]:
            pass
        l += 1


