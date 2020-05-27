from classy_ur import *

#initial set up of parameters
board = Board()
player1 = HumanPlayer("Stevie",  1)
player2 = HumanPlayer("Jarek", 2)
dice = Dice()

player = [player1, player2]
p = 0

def nextPlayer(p):
    if p == 0:
        p = 1
    else:
        p = 0
    return p

gameEnd = board.winner()    
while not gameEnd:
    board.display()
    # print player's turn
    print("Player ", player[p].id)
    # roll the dice
    dice = Dice()
    dice.roll()
    dice.show_roll()
    roll = dice.result_roll()
    # check if move possible
    check = board.checkMovePossible(roll = roll, player = player[p].id)
    if check: 
        ind = player[p].makeMove(board)
        check = board.checkMove(player = player[p].id, roll = roll, index = ind)
        if check == False:
            print("This is not a valid move. ")
            p = nextPlayer(p)
        else:
            board.updateV(player = player[p].id, roll = roll, index = ind)
            rosette = board.isRosette(roll = roll, index = ind)
            if rosette == False: 
                p = nextPlayer(p)
                gameEnd = board.winner()
    else:
        print('No valid move. :( ')
        p = nextPlayer(p)
