import random

print('Welcome to Black Jack! The coolest casino game ever!')

card_sum = 0

print('Your sum is {}'.format(card_sum))
print('Do you want to draw another card?')




def draw_card():
    cardValue = random.randint(1, 11)
    return cardValue

card_sum = draw_card()

print(card_sum)