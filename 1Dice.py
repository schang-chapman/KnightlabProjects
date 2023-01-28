from random import randint


def parser(dice_inp, total_roll=0):
    dice_details = dice_inp.split('d')
    for i in range(1, int(dice_details[0]) + 1):
        dice_roll = randint(1, int(dice_details[1]))
        total_roll += dice_roll
        print('Dice number', i, 'rolled', dice_roll, '.')
        if dice_roll == 1:
            print('Natural 1!')
        elif dice_roll == 20:
            print('Natural 20!')
    return total_roll


def roll_die():
    while 1 == 1:
        try:
            dice = input('Enter how many dice you are rolling, and what range of die.\n'
                         'They should be formatted as "1d4" (Rolling 1 4-sided die.)\n')
            dice = dice.lower()
            roll = parser(dice)
            print('You rolled', roll, 'total.')
            break
        except ValueError:
            print('Formatting error.')


while 1 == 1:
    roll_die()
    while 1 == 1:
        try:
            loop = input('Would you like to roll again?\n'
                         'Answer yes or no.\n')
            loop = loop.lower()
            if loop == 'yes':
                break
            elif loop == 'no':
                break
            else:
                raise RuntimeError
        except RuntimeError:
            print('Invalid response.')
    if loop == 'yes':
        continue
    break
