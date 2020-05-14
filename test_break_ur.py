from board import  EmptyBoard, CheckMovePossible, get_index, UpdateV, UpdateBoard
from die_roll import *

def board_setup_1():
    v1 = [0]*14
    v1[3] = 1
    v1[8] = 1
    v1[12] = 1
    v2 = [0]*14
    v2[4] = 1
    v2[7] = 1
    v2[13] = 1
    return v1, v2

# scenario 1: new piece to be played onto empty board
# expect check = True, index = -1, new_piece = True, is_rosette = False
board = EmptyBoard()
player = 1
row, pos = 'A', 5
roll = 2
v1 = [0]*14
v2 = [0]*14
check = CheckMovePossible(v1, v2, roll, 1, 7, 7)
index, new_piece = get_index(row, pos)
v1, v2, new_p1, new_p2, off_p1, off_p2, is_rosette = UpdateV(v1, v2, player, roll, index, 7, 7, 0, 0, new_piece)
board = UpdateBoard(v1, v2)
if check == False:
    print("S1: Failed check. ")
else:
    if index != -1:
        print("S1: Failed index. ")
    else:
        if new_piece == False:
            print("S1: Failed new_piece. ")
        else:
            if is_rosette == True:
                print("S1: Failed is_rosette. ")
            else:
                print("S1: passed. ")

# scenario 2: no possible move for player 1
# expect check = False
player = 1
v1, v2 = board_setup_1()
board = UpdateBoard(v1, v2)
roll = 4
check = CheckMovePossible(v1, v2, roll, player, 4, 4)
if check == True:
    print("S2: Failed check. ")
else:
    print("S2: passed. ")

# scenario 3: player 2 moves piece off of board
# expect check = True, index = 13, new_piece = False, is_rosette = False, off_p1 = 0, off_p1 = 1
player = 2
v1, v2 = board_setup_1()
board = UpdateBoard(v1, v2)
roll = 1
new_p1 = 4
new_p2 = 4
row, pos = 'A', 7
check = CheckMovePossible(v1, v2, roll, player, new_p1, new_p2)
index, new_piece = get_index(row, pos)
v1, v2, new_p1, new_p2, off_p1, off_p2, is_rosette = UpdateV(v1, v2, player, roll, index, new_p1, new_p2, 0, 0, new_piece)
board = UpdateBoard(v1, v2)
if check == False:
    print("S3: Failed check. ")
else:
    if index != 13:
        print("S3: Failed index. ")
    else:
        if new_piece == True:
            print("S3: Failed new_piece. ")
        else:
            if is_rosette == True:
                print("S3: Failed is_rosette. ")
            else:
                if off_p1 != 0:
                    print("S3: Failed off_p1. ")
                else:
                    if off_p2 != 1:
                        print("S3: Failed off_p2. ")
                    else:
                        print("S3: passed. ")

# scenario 4: player 1 lands on rosette
# expect check = True, index = 12, new_piece = False, is_rosette = True
player = 1
v1, v2 = board_setup_1()
board = UpdateBoard(v1, v2)
roll = 1
new_p1 = 4
new_p2 = 4
row, pos = 'A', 8
check = CheckMovePossible(v1, v2, roll, player, 4, 4)
index, new_piece = get_index(row, pos)
v1, v2, new_p1, new_p2, off_p1, off_p2, is_rosette = UpdateV(v1, v2, player, roll, index, new_p1, new_p2, 0, 0, new_piece)
board = UpdateBoard(v1, v2)
if check == False:
    print("S4: Failed check. ")
else:
    if index != 12:
        print("S4: Failed index. ")
    else:
        if new_piece == True:
            print("S4: Failed new_piece. ")
        else:
            if is_rosette == False:
                print("S4: Failed is_rosette. ")
            else:
                print("S4: passed. ")

# scenario 5: player 2, pieces are on the board, move is possible if roll > 0
# expect check = True if roll >0, or False if roll == 0
player = 2
v1, v2 = board_setup_1()
dice = Dice()
dice.roll()
roll = dice.result_roll()
check = CheckMovePossible(v1, v2, roll, player, 4, 4)
if roll > 0:
    if check != True:
        print("S5: Failed check. ")
    else:
        print("S5: passed. ")
else:
    if check == True:
        print("S5: Failed check. ")
    else:
        print("S5: passed. ")