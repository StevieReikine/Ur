board = []
def EmptyBoard(board):
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
    return board

def PrintBoard(board):
    num = [str(i) for i in range(1,9)]
    #print(num)
    print('A ' + "".join(board[0]) + '\n' + 'B ' + "".join(board[1]) + '\n' + 'A ' + "".join(board[2]) + '\n' + '  ' + "".join(num))
    #print(board)

board = EmptyBoard(board)
#PrintBoard(board)

#define variables for two players
player = [1 , 2]
player1 = player[0]
player2 = player[1]

#define vectors for each players board position
v1 = [0]*14     #for player 1, initialize to zeros
v2 = [0]*14     #for player 2, initialize to zeros
v1[1] = 1       #add 1 piece in test postiion
v1[7] = 1
v2[12] = 1       #add 1 piece in test position
v2[0] = 1
#print(v1, v2)

def PlayPiece(player, board, ind1, ind2):
    if player == 1:
        board[ind1][ind2] = '1'
    if player == 2:
        board[ind1][ind2] = '2'
    return board

def MapVtoBoard(vector, board, player):
    PiecePos = [i for i, val in enumerate(vector) if val]   #get indices of '1' values in vector
    print(PiecePos, player)
    if len(PiecePos) == 0:
        return board
    for Piece in PiecePos:
        if Piece >3 & Piece < 12:
            ind1 = 1
            ind2 = Piece - 4
        if Piece < 4:
            ind2 = -1*(Piece - 3)
            if player == 1:
                ind1 = 0
            if player == 2:
                ind1 = 2
        if Piece > 11:
            ind2 = -1*(Piece - 19)
            if player == 1:
                ind1 = 0
            if player == 2:
                ind1 = 2
        board = PlayPiece(player, board, ind1, ind2)
    return board

def UpdateBoard(v1, v2, board):
    board = MapVtoBoard(v1, board, 1)
    board = MapVtoBoard(v2, board, 2)
    return board

board = UpdateBoard(v1, v2, board)
PrintBoard(board)

