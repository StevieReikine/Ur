#board = []
def EmptyBoard():
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

"""
board = EmptyBoard(board)
#PrintBoard(board)

#define variables for two players
player = [1 , 2]
player1 = player[0]
player2 = player[1]

#define vectors for each players board position
v1 = [0]*14     #for player 1, initialize to zeros
v2 = [0]*14     #for player 2, initialize to zeros

v1[3] = 1       #add 1 piece in test postiion
v1[12] = 1
v1[8] = 1
v2[13] = 1       #add 1 piece in test position
v2[4] = 1
v2[7] = 1
#print(v1, v2)
"""

def PlayPiece(player, board, ind1, ind2):
    if player == 1:
        board[ind1][ind2] = '1'
    if player == 2:
        board[ind1][ind2] = '2'
    return board

def MapVtoBoard(vector, player):
    board = EmptyBoard()
    PiecePos = [i for i, val in enumerate(vector) if val]   #get indices of '1' values in vector
    #print(PiecePos, player)
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

def UpdateBoard(v1, v2):
    board = MapVtoBoard(v1, 1)
    board = MapVtoBoard(v2, 2)
    return board

"""
def DisplayBoard(v1, v2):
    board = EmptyBoard()

    print(board)
    return
"""

#dice = 1 # for now, set value of dice roll here

def CheckMovePossible(v1, v2, roll, player):
    check = True
    safe = 0
    if roll == 0:
        check = False
        return check
    if player == 1:
        SpacesOccupied = [i for i, val in enumerate(v1) if val]
        if v2[7]:
            safe = 7
    if player == 2:
        SpacesOccupied = [i for i, val in enumerate(v2) if val]
        if v1[7]:
            safe = 7
    if SpacesOccupied == []:
        check = True
    else:
        SpacesOccupied.append(-1)
        for i in SpacesOccupied:
            if (i + roll) < 14: 
                if (i + roll) not in SpacesOccupied:
                    if i + roll == safe:
                        check = False
                    else:
                        check = True
            if (i + roll) == 14:
                check = True
    return check
    

#check = CheckMovePossible([0]*8, [0]*8, dice, 1)
#print(check)

def player_input():
    piece_row = input("Which piece do you want to move? First enter row (A or B):  ")
    piece_pos = int(input("Which piece do you want to move? Now enter position (1-8):  "))
    return piece_row, piece_pos

#piece_row, piece_pos = player_input()

def get_index(piece_row, piece_pos):
    #get index of the piece to move
    new_piece = False
    index = piece_pos
    #print(index)
    if piece_row == 'A':
        if piece_pos < 5:
            index = 4 - index
            #print(index)
        if piece_pos == 5:
            new_piece = True
            index = 14 #just in case
            #print(index)
        if piece_pos > 6:
            index = 20 - index
            #print(index)
    if piece_row == 'B':
        index = index + 3
        print(index)
    return index, new_piece

#index, new_piece, is_rosette = get_index(piece_row, piece_pos)
##print(index, new_piece, is_rosette)

#off_p1 = 0
##off_p2 = 0

def UpdateV(v1, v2, player, roll, index, off_p1, off_p2, new_piece):
    #move piece already on board
    if new_piece is False:
        #check if moving off board
        if (index + roll) == 14:
            if player == 1:
                v1[index] = 0
                off_p1 += 1
            if player == 2:
                v2[index] = 0
                off_p2 += 1
        else:
            if player == 1:
                v1[index] = 0
                v1[index + roll] = 1
            if player == 2:
                v2[index] = 0
                v2[index + roll] = 1
            #check if other player bumped
            if player == 1:
                if v2[index + roll] == 1:
                    v2[index + roll] = 0
            if player == 2:
                if v1[index + roll] == 1:
                    v1[index + roll] = 0
    else:
        if player == 1:
            v1[roll - 1] = 1
        if player == 2:
            v2[roll - 1] = 1    
    rosette = [3, 7, 13]
    is_rosette = False    
    if (index + roll) in rosette:
        is_rosette = True
    return v1, v2, off_p1, off_p2, is_rosette

#print(v1, v2)
#v1, v2, off_p1, off_p2 = UpdateV(v1, v2, 1, dice, index, off_p1, off_p2)
#print(v1, v2, off_p1, off_p2)

def Winner(off_p1, off_p2):
    game_over = False
    if off_p1 == 7:
        print('Player 1 wins. Hurrah! ')
        game_over = True
    if off_p2 == 7:
        print('Player 2 wins. Hurrah! ')
        game_over = True
    return game_over
