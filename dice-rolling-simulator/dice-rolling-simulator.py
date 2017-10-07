import random

print('Welcome to the Dice Rolling Simulator!')

nbrOfDices = input('How many dices do you want to throw? \n')


def roll(nbr_of_dices):
    while nbr_of_dices > 0:
        i = random.randrange(1, 7)
        print('You rolled ' + str(i))
        nbr_of_dices -= 1


roll(int(nbrOfDices))
