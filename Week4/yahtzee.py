import cv2
import random

ary = []

class Die:
    def __init__(self, sidesOfDie):
        self.sidesOfDie = sidesOfDie

    def roll(self):
        die1 = random.randint(1, self.sidesOfDie)
        die2 = random.randint(1, self.sidesOfDie)
        die3 = random.randint(1, self.sidesOfDie)
        die4 = random.randint(1, self.sidesOfDie)
        die5 = random.randint(1, self.sidesOfDie)

        ary.append(die1)
        ary.append(die2)
        ary.append(die3)
        ary.append(die4)
        ary.append(die5)

    def getCurrentFaceValue(self):
        print(ary)
        
    def showDieFace(self):
        print()
    
    def clearary(self):
        ary.clear()

print("Type '0' if you want to exit.")
getDie = int(input("What dice do you choose? "))
while getDie != 0:
    the_Die = Die(getDie)
    the_Die.roll()
    the_Die.getCurrentFaceValue()
    if (len(set(ary)) != 1):
        getDie = int(input("What dice do you choose? "))
    else:
        print("YAHTZEE")
        break
    the_Die.clearary()