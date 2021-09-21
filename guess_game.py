"""
guess_game.py

This program prompts the user to guess the random value selected.

"""
import random

def main():

    str_rand_num = str(random.randint(1, 5))

    while input('Enter a number between 1 and 5: ') != str_rand_num:
        print('Sorry, your guess is incorrect. Try again!')
    else:
        print('You guessed correctly! Thank you for playing. Bye!')

if __name__ == '__main__':
    main()
