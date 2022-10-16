# Handling Command-Line Arguments in the Script
# CREATE MODULAR CODE WITH FUNCTIONS TO MAKE TESTING EASY

import sys
from random import randint


def validate_guess(guess, llimit, ulimit):
    try:
        guess = int(guess)
    except (ValueError, NameError):
        return False
    if (guess >= llimit and guess <= ulimit):
        return True
    else:
        return False

def check_guess(guess, answer):
    if (guess < answer):
        return 'low'
    elif (guess > answer):
        return 'high'
    elif (guess == answer):
        return 'correct'


# Only run the main code when this script is run directly - this main code should not interfere with the testing
# of the functions declared in this source file
if __name__ == '__main__':
    # send command-line parameters to the code file using sys.argv
    # command-line: python <script> <first> <second>
    # sys.argv[0] will be the script name
    try:
        first = int(sys.argv[1])
        second = int(sys.argv[2])
    except (ValueError, NameError):
        print('please use valid positive integers as arguments')
    # print(f'hiiii {first} {second}')
    answer = randint(first, second)
    guess = None
    while (guess != answer):
        try:
            guess = input('Guess a number: ')
        except (ValueError, NameError):
            print('please enter a valid integer')
            continue
        else:
            if(validate_guess(guess, first, second)):
                result = check_guess(guess, answer)
                if result == 'correct':
                    print('Correct!')
                    break
                else:
                    print(result)
                    continue
            else:
                print(f'please enter a number within the range {first} - {second}')
                continue
    
