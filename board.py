empty = '\u25A2'
rosette = '\u22A0'

row1 = rosette + empty*3 + '_' + '_' + rosette + empty
row2 = empty*3 + rosette + empty*4
row3 = row1
board = [list(row1),list(row2),list(row3)]
board[0][4] = ' '
board[0][5] = ' '
board[2][5] = ' '
board[2][4] = ' '
print("".join(board[0]) + '\n' + "".join(board[1]) + '\n' + "".join(board[2]))
#print(board)
