from board import PrintBoard, EmptyBoard, Winner, CheckMovePossible, CheckMove, player_input, get_index, UpdateV, UpdateBoard
from die_roll import Dice
from itertools import cycle

#initial set up of parameters
board = EmptyBoard()
v1 = [0]*14     #for player 1, initialize to zeros
v2 = [0]*14     #for player 2, initialize to zeros
off_p1 = 0
off_p2 = 0
new_p1 = 7
new_p2 = 7
new_piece = False
game_over = False
player = [1 , 2]
p = 0

def NextPlayer(p):
    if p == 0:
        p = 1
    else:
        p = 0
    return p
    

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
    check = CheckMovePossible(v1, v2, roll, player[p],new_p1, new_p2)
    if check: 
        row, pos = player_input()
        index, new_piece = get_index(row, pos)
        check = CheckMove(v1, v2, player[p], roll, index, new_p1, new_p2)
        if check == False:
            print("This is not a valid move. ")
            p = NextPlayer(p)
        else:
            v1, v2, new_p1, new_p2, off_p1, off_p2, is_rosette = UpdateV(v1, v2, player[p], roll, index, new_p1, new_p2, off_p1, off_p2, new_piece)
            board = UpdateBoard(v1, v2)
            if is_rosette == False: 
                p = NextPlayer(p)
            game_over = Winner(off_p1, off_p2)
    else:
        print('No valid move. :( ')
        p = NextPlayer(p)

