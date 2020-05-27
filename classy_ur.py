from numpy import random

class Player:
    def __init__(self,  name,  id):
        self.name = name    #name of the player
        self.id = id                #the id also used to mark pieces on the board
    
    # perform a play action   
    def play(self,  board):
        return 0

class HumanPlayer(Player):
    def makeMove(self, board):
        # get player input
        piece_row = input("Which piece do you want to move? First enter row (A or B):  ")
        piece_pos = 100
        possiblePosition = list(range(1,9))
        while piece_pos not in possiblePosition:
            piece_pos = int(input("Which piece do you want to move? Now enter position (1-8):  "))
        # get index of the piece to move
        index = piece_pos
        if piece_row == 'A':
            if piece_pos < 5:
                index = 5 - index
            if piece_pos == 5:
                index = 0 # new piece
            if piece_pos > 6:
                index = 21 - index
        if piece_row == 'B':
            index = index + 4
        return index

class Dice:
    def __init__(self):
        self.dice = []
    
    def roll(self):
        self.dice = random.randint(1, 4, size= 4)
        for i in range(len(self.dice)):
            if self.dice[i] != 1:
                self.dice[i] =0

    def show_roll(self):    
        print('dice rolled: ', self.dice)

    def result_roll(self):    
        roll = sum(self.dice)
        return roll

class Board:
    def __init__ (self):
        self.v1 = [0]*16
        self.v1[0] = 7
        self.v2 = [0]*16
        self.v2[0] = 7

    def _mapVtoBoard(self, board, vector, player):
        # get indices of '1' values in vector
        vector = vector[1:16]
        piecePos = [i for i, val in enumerate(vector) if val]   

        # if board is empty, return
        if len(piecePos) == 0:
            return

        for piece in piecePos:
            # define indices for pieces in row 'B'
            if piece >3 & piece < 12:
                ind1 = 1
                ind2 = piece - 4

            # define indices for pieces placed and not yet in 'B'
            if piece < 4:
                ind2 = -1*(piece - 3)
                if player == 1:
                    ind1 = 0
                if player == 2:
                    ind1 = 2

            # define infices for pieces moved off of 'B'
            if piece > 11:
                ind2 = -1*(piece - 19)
                if player == 1:
                    ind1 = 0
                if player == 2:
                    ind1 = 2
            
            # add player labels (as defined in PlayPiece for each player, eg '1' and '2')
            if player == 1:
                board[ind1][ind2] = '1'
            if player == 2:
                board[ind1][ind2] = '2'
        return 
    
    def display(self):
        # first, construct an empty representation of the board
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

        # now, fill it with the board state based on v1, v2

        # place marker for places where player 1 has pieces
        self._mapVtoBoard(board, self.v1, player=1)
        # place marker for places where player 2 has pieces
        self._mapVtoBoard(board, self.v2, player=2)

        num = [str(i) for i in range(1,9)]
        print('A ' + "".join(board[0]) + '\n' + 'B ' + "".join(board[1]) + '\n' + 'A ' + "".join(board[2]) + '\n' + '  ' + "".join(num))
    
    def winner(self):
        game_over = False
        if self.v1[15] == 7:
            print('Player 1 wins. Hurrah! ')
            self.game_over = True
        if self.v2[15] == 7:
            print('Player 2 wins. Hurrah! ')
            game_over = True
        return game_over

    def _safeOccupied(self, player):
        safe = 200
        if player == 1:
            occupied = [i for i, val in enumerate(self.v1[0:16]) if val]
            if self.v2[8]:
                safe = 8
        if player == 2:
            occupied = [i for i, val in enumerate(self.v2[0:16]) if val]
            if self.v1[8]:
                safe = 8
        return safe, occupied

    def checkMove(self, player, roll, index):
        # This method checks that a played move is allowed
        # It is also used in checkMovePossible method
        check = False
        safe, occupied = self._safeOccupied(player)
        # check that there is a piece to play at given index
        if player == 1 and self.v1[index] == 0:
            return check
        if player == 2 and self.v2[index] == 0:
            return check
        # if the board is empty, a new piece can be played
        if index == 0 and occupied == []:
            check = True
            return check
        # if there are pieces on the board
        else:
            # if the move over-shoots the board
            if (index + roll) < 15: 
                # check if the move hits own piece
                if (index + roll) not in occupied:
                    # and check if it hits the 'safe' piece of the opponent
                    if (index + roll) == safe:
                        check = False
                    else:
                        check = True
            # check if the move takes the piece of the board
            if (index + roll) == 15:
                check = True
        return check

    def checkMovePossible(self, roll, player):
        # This method checks whether there is a possible move to make.
        check = False
        if roll == 0:
            check = False
            return check
        safe, occupied = self._safeOccupied(player)
        if occupied == []:
            check = True
        else:
            for i in occupied:
                check = self.checkMove(player, roll, i)
                if check == True:
                    break
        return check

    def updateV(self, player, roll, index):
        # move piece already on board
        if index > 0 :
            if player == 1:
                self.v1[index] = 0
                self.v1[index + roll] = 1
            if player == 2:
                self.v2[index] = 0
                self.v2[index + roll] = 1
            # check if other player bumped
            if (index + roll) > 4 and (index + roll) < 13:
                if player == 1:
                    if self.v2[index + roll] == 1:
                        self.v2[index + roll] = 0
                if player == 2:
                    if self.v1[index + roll] == 1:
                        self.v1[index + roll] = 0
        # move new piece onto board
        else:
            if player == 1:
                self.v1[index] -= 1
                self.v1[roll + index] = 1
            if player == 2:
                self.v2[index] -= 1
                self.v2[roll + index] = 1 
        return

    def isRosette(self, roll, index):   
        is_rosette = False 
        rosette = [4, 8, 14]   
        if (index + roll) in rosette:
            is_rosette = True
        return is_rosette

