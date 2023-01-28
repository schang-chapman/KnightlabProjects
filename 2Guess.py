import random as rand
from datetime import date


def lesser_greater(number):
    while 1 == 1:
        lo_lim = rand.randint(0, 102)
        hi_lim = lo_lim + 30
        if lo_lim < number < hi_lim:
            break
        else:
            continue
    return lo_lim, hi_lim


def even_test(number):
    if number % 2 == 0:
        return True
    else:
        return False


def factor_find(number):
    factors = []
    for n in range(1, number + 1):
        if number % n == 0 and n <= number:
            factors.append(n)
    return factors


def prime_test(number):
    factors = factor_find(number)
    if len(factors) == 2:
        return True
    else:
        return False


def factor_pull(number):
    smol_factors = []
    all_factors = factor_find(number)
    for n in all_factors:
        if n < 10:
            smol_factors.append(n)
    while True:
        one_factor = rand.choice(smol_factors)
        if one_factor != 2:
            break
        if prime_test(number):
            if one_factor == 1:
                break
    return one_factor


def hints_compile(number):
    hints = {}
    for n in range(1, 5):
        hint_round = 'hint' + str(n)
        if n == 1:
            lo_num, hi_num = lesser_greater(number)
            hints[hint_round] = ['The number is between ' + str(lo_num) + ' and ' + str(hi_num) + '.', lo_num, hi_num]
        elif n == 2:
            if even_test(number):
                hints[hint_round] = ['It is an even number.', True]
            else:
                hints[hint_round] = ['It is an odd number.', False]
        elif n == 3:
            factor = factor_pull(number)
            hints[hint_round] = ['The number is divisible by ' + str(factor) + '.', factor]
        elif n == 4:
            if prime_test(number):
                hints[hint_round] = ['It is a prime number.', True]
            else:
                hints[hint_round] = ['It is a composite number.', False]
    return hints


def farm(hints_dict, hints_given, wrong_ans):
    num_list = []
    for h in range(1, hints_given+1):
        if h == 1:
            num_range = range(hints_dict['hint1'][1], hints_dict['hint1'][2]+1)
            for n in num_range:
                num_list.append(n)
        elif h == 2:
            if hints_dict['hint2'][1]:
                for n in num_list:
                    if not even_test(n):
                        num_list.remove(n)
            else:
                for n in num_list:
                    if even_test(n):
                        num_list.remove(n)
        elif h == 3:
            for n in num_list:
                if n % hints_dict['hint3'][1] != 0:
                    num_list.remove(n)
        elif h == 4:
            if hints_dict['hint4'][1]:
                for n in num_list:
                    if not prime_test(n):
                        num_list.remove(n)
            else:
                for n in num_list:
                    if prime_test(n):
                        num_list.remove(n)
        for n in num_list:
            if n in wrong_ans:
                num_list.remove(n)
    print(num_list)


def start_up(breaker):
    if not breaker:
        return False
    while 1 == 1:
        start = input('Are you ready to start?\n').lower()
        if start == 'yes':
            return True
        elif start == 'no':
            print('Goodbye.')
            return False
        else:
            print('This is a yes or no question.')


def restart():
    while 1 == 1:
        start = input('Do you want to play again?\n').lower()
        if start == 'yes':
            print('The game will now restart with a new number.')
            return True
        elif start == 'no':
            print('Goodbye.')
            return False
        else:
            print('This is a yes or no question.')


def win_rec(number, guesses, hints, limes, file='2Guess.txt', confirm=''):
    while True:
        if confirm == 'yes':
            break
        name = input('Enter a name for the leaderboards.\n')
        while True:
            confirm = input('Are you sure you want your name to be "' + name + '"?\n').lower()
            if confirm == 'yes':
                break
            elif confirm == 'no':
                break
            else:
                print('This is a yes or no question')
    record = open(file, 'a')
    record.write('#########################\n' +
                 'Name: ' + name + '\n' +
                 'Date: ' + str(date.today()) + '\n' +
                 'Number: ' + str(number) + '\n' +
                 'Guesses: ' + str(guesses) + '\n' +
                 'Hints Given: ' + str(hints) + '\n' +
                 'Limes Harvested: ' + str(limes) + '\n')
    record.close()


go = True
print('Welcome to the Number Guessing Game.\n'
      'We will pick a number from 1 to 100. You will guess it.\n'
      'Every 3 wrong guesses, you will be given a hint.\n'
      'There are 4 hints total. After you are given the 4th hint, those will be your last 3 guesses.\n'
      'That means you have 15 guesses total. When you run out of guesses, you lose.\n'
      'If you want to give up, type [quit].')

while True:
    go = start_up(go)
    if not go:
        break

    rand_num = rand.randint(1, 101)
    print(rand_num)
    num_hints = hints_compile(rand_num)
    guess_count = 0
    wrong_guess = []
    hint_count = 0
    harvest = 0

    while go:
        try:
            guess = input('Guess a whole number.\n')
            if guess.lower() == 'quit':
                print('You have quit the game. The number was', rand_num, '.')
                go = False
                break
            elif guess.lower() == 'farm' and hint_count > 0:
                print('Here are your limes.')
                farm(num_hints, hint_count, wrong_guess)
                harvest += 1
                continue
            else:
                guess = int(guess)
        except ValueError:
            print('That is not a whole number.')
            continue

        if guess != rand_num and type(guess) == int:
            print('That is not the number.')
            guess_count += 1
            wrong_guess.append(guess)
            if guess_count == 13:
                print('You have 2 guesses remaining.')
            elif guess_count == 14:
                print('This is your last guess. If you guess wrong, you lose.')
        elif guess == rand_num:
            print('Congratulations! You correctly guessed the number!\n'
                  'It took you', guess_count, 'guess(es) and', hint_count, 'hint(s).')
            if harvest > 0:
                print('You also cheated', harvest, 'times. Cheater.')
            while True:
                enter_board = input('Do you want to enter the leaderboard?\n')
                if enter_board == 'yes':
                    win_rec(rand_num, guess_count, hint_count, harvest)
                    break
                elif enter_board == 'no':
                    print('Okay.')
                    break
                else:
                    print('This is a yes or no question.')
            if restart():
                break
            else:
                go = False
                break
        try:
            if guess_count % 3 == 0:
                hint_count += 1
                print("Here's a hint:\n", num_hints['hint'+str(hint_count)][0])
                if hint_count == 4:
                    print('WARNING! That was your last hint. You are down to your last 3 guesses.')
        except KeyError:
            print('You have used up all of your guesses. The number was', rand_num, '.')
            if restart():
                break
            else:
                go = False
                break
