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

def PlayPiece(player, board, ind1, ind2):
    if player == 1:
        board[ind1][ind2] = '1'
    if player == 2:
        board[ind1][ind2] = '2'
    return board

def MapVtoBoard(board, vector, player):
    # get indices of '1' values in vector
    PiecePos = [i for i, val in enumerate(vector) if val]   
    # if board is empty, return
    if len(PiecePos) == 0:
        return board
    for Piece in PiecePos:
        # define indices for pieces in row 'B'
        if Piece >3 & Piece < 12:
            ind1 = 1
            ind2 = Piece - 4
        # define indices for pieces placed and not yet in 'B'
        if Piece < 4:
            ind2 = -1*(Piece - 3)
            if player == 1:
                ind1 = 0
            if player == 2:
                ind1 = 2
        # define infices for pieces moved off of 'B'
        if Piece > 11:
            ind2 = -1*(Piece - 19)
            if player == 1:
                ind1 = 0
            if player == 2:
                ind1 = 2
        # add player labels (as defined in PlayPiece for each player, eg '1' and '2')
        board = PlayPiece(player, board, ind1, ind2)
    return board

def UpdateBoard(v1, v2):
    # place all the boxes and rosettes as for an empy board
    board = EmptyBoard()
    # place marker for places where player 1 has pieces
    board = MapVtoBoard(board, v1, 1)
    # place marker for places where player 2 has pieces
    board = MapVtoBoard(board, v2, 2)
    return board

def safe_occupied(v1, v2, player):
    safe = 200
    if player == 1:
        SpacesOccupied = [i for i, val in enumerate(v1) if val]
        if v2[7]:
            safe = 7
    if player == 2:
        SpacesOccupied = [i for i, val in enumerate(v2) if val]
        if v1[7]:
            safe = 7
    return safe, SpacesOccupied

def CheckMove(v1, v2, player, roll, index, new_p1, new_p2):
    check = False
    safe, SpacesOccupied = safe_occupied(v1, v2, player)
    # if placing a new piece, check that there are pieces to play
    if index == -1:
        if player == 1 and new_p1 == 0:
            return check
        if player == 2 and new_p2 == 0:
            return check
    # if the board is empty, any piece can be played
    if SpacesOccupied == []:
        check = True
    # if there are pieces on the board
    else:
        # if the move over-shoots the board
        if (index + roll) < 14: 
            # check if the move hits own piece
            if (index + roll) not in SpacesOccupied:
                # and check if it hits the 'safe' piece of the opponent
                if (index + roll) == safe:
                    check = False
                else:
                    check = True
        # check if the move takes the piece of the board
        if (index + roll) == 14:
            check = True
    return check

def CheckMovePossible(v1, v2, roll, player, new_p1, new_p2):
    check = False
    if roll == 0:
        check = False
        return check
    safe, SpacesOccupied = safe_occupied(v1, v2, player)
    if SpacesOccupied == []:
        check = True
    else:
        SpacesOccupied.append(-1)
        for i in SpacesOccupied:
            check = CheckMove(v1, v2, player, roll, i, new_p1, new_p2)
            if check == True:
                break
    return check

def player_input():
    piece_row = input("Which piece do you want to move? First enter row (A or B):  ")
    piece_pos = int(input("Which piece do you want to move? Now enter position (1-8):  "))
    return piece_row, piece_pos

def get_index(piece_row, piece_pos):
    # get index of the piece to move
    new_piece = False
    index = piece_pos
    if piece_row == 'A':
        if piece_pos < 5:
            index = 4 - index
        if piece_pos == 5:
            new_piece = True
            index = -1 #just in case
        if piece_pos > 6:
            index = 20 - index
    if piece_row == 'B':
        index = index + 3
    return index, new_piece

def UpdateV(v1, v2, player, roll, index, new_p1, new_p2, off_p1, off_p2, new_piece):
    # move piece already on board
    is_rosette = False 
    if new_piece is False:
        # check if moving off board
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
            # check if other player bumped
            if (index + roll) > 3 and (index + roll) < 12:
                if player == 1:
                    if v2[index + roll] == 1:
                        v2[index + roll] = 0
                if player == 2:
                    if v1[index + roll] == 1:
                        v1[index + roll] = 0
    # move new piece onto board
    else:
        if player == 1:
            v1[roll + index] = 1
            new_p1 -= 1
        if player == 2:
            v2[roll + index] = 1  
            new_p2 -= 1
    rosette = [3, 7, 13]   
    if (index + roll) in rosette:
        is_rosette = True
    return v1, v2, new_p1, new_p2, off_p1, off_p2, is_rosette

def Winner(off_p1, off_p2):
    game_over = False
    if off_p1 == 7:
        print('Player 1 wins. Hurrah! ')
        game_over = True
    if off_p2 == 7:
        print('Player 2 wins. Hurrah! ')
        game_over = True
    return game_over
