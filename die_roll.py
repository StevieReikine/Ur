from numpy import random

class Dice:
    def __init__(self):
        self.dice = []
    
    def roll(self):
        self.dice = random.randint(1, 4, size= 4)
        for i in range(len(self.dice)):
            if self.dice[i] != 1:
                self.dice[i] =0

    def show_roll(self):    
        print(self.dice)

    def result_roll(self):    
        roll = sum(self.dice)
        return roll

dice = Dice()
dice.roll()
dice.show_roll()
print(dice.result_roll())