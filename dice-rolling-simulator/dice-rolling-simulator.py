import random

print('Welcome to the Dice Rolling Simulator!')

nbrOfDices = input('How many dices do you want to throw? \n')


def roll(nbr_of_dices):

    sum = 0

    while nbr_of_dices > 0:
        i = random.randrange(1, 7)
        sum += i
        print('You rolled ' + str(i))
        nbr_of_dices -= 1

    print('You rolled a total of: ' + str(sum))

roll(int(nbrOfDices))
