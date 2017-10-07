import random

print('Welcome to the Dice Rolling Simulator!')

nbrOfDices = input('How many dices do you want to throw? \n')


def roll(nbr_of_dices):

    sum = 0

    while nbr_of_dices > 0:
        i = random.randrange(1, 7)
        sum += i
        print('You rolled {}'.format(i))
        nbr_of_dices -= 1

    print('You rolled a total of: {}'.format(sum))

roll(int(nbrOfDices))
