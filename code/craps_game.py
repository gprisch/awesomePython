"""
You roll two six-sided dice, each with faces containing one, two, three, four, five
and six spots, respectively. When the dice come to rest, the sum of the spots on the
two upward faces is calculated.

If the sum is 7 or 11 on the first roll, you win.

If the sum is 2, 3 or 12 on the first roll (called_fn “craps”), you lose (i.e., the “house”
wins).

If the sum is 4, 5, 6, 8, 9 or 10 on the first roll, that sum becomes your
“point.” To win, you must continue rolling the dice until you “make your point”
(i.e., roll that same point value). You lose by rolling a 7 before making your point.
"""

import random


def roll_dices(number_of_dices=2):
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2


def display_result(dices):
    die1, die2 = dices
    print(f'You got {die1} and {die2} for a total of {sum(dices)}')


def play():
    win_list = [7, 11]
    lose_list = [2, 3, 12]
    dices = roll_dices()
    dices_total = sum(dices)
    display_result(dices)

    if dices_total in win_list:
        print('You win !! wawww !!!')
    elif dices_total in lose_list:
        print('You lose !!!!!!')
    else:
        point = dices_total
        number_of_rolls = 1
        print(f'Your point is {point} - shoot again !!')

        while True:
            dices = roll_dices()
            roll_total = sum(dices)
            display_result(dices)
            number_of_rolls += 1

            if roll_total == point:
                print(f'You win in {number_of_rolls} times')
                break
            elif roll_total == 7:
                print(f'OMG, you lose after {number_of_rolls} times')
                break


if __name__ == '__main__':
    play()
