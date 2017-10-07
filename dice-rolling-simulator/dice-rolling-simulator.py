import random

print('Welcome to the Dice Rolling Simulator!')

def roll():
    i = random.randrange(1, 7)
    print('You rolled ' + str(i))
