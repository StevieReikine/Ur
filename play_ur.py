from board import PrintBoard, EmptyBoard, Winner, CheckMovePossible, player_input, get_index, UpdateV, UpdateBoard
from die_roll import Dice

#initial set up of parameters
board = EmptyBoard()
v1 = [0]*14     #for player 1, initialize to zeros
v2 = [0]*14     #for player 2, initialize to zeros
off_p1 = 0
off_p2 = 0
new_piece = False
game_over = False
player = [1 , 2]
player1 = player[0]
player2 = player[1]
p = 0

while not game_over:
    # show the board
    PrintBoard(board)
    # print player's turn
    print("Player ", player[p])
    # roll the dice
    dice = Dice()
    dice.roll()
    dice.show_roll()
    roll = dice.result_roll()
    # check if move possible
    
    check = CheckMovePossible(v1, v2, roll, player[p])
    if check: 
        row, pos = player_input()
        index, new_piece = get_index(row, pos)
        v1, v2, off_p1, off_p2, is_rosette = UpdateV(v1, v2, player[p], roll, index, off_p1, off_p2, new_piece)
        board = UpdateBoard(v1, v2)
        if is_rosette:
            p = p
        else:
            if p == 0:
                p = 1
            else:
                p = 0
        game_over = Winner(off_p1, off_p2)
    else:
        print('No valid move. :( ')
        if p == 0:
            p = 1
        else:
            p = 0

