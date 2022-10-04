# Some Built-in python Errors

# SyntaxError
# def hoohoo()
#     pass

# NameError
# print(name)

# IndexError
# li = [1, 2, 3]
# print(li[5])

# KeyError
# di = {'a': 1}
# print(di['b'])

# ZeroDivisionError
# print(1/0)

# Programs constantly interact with the outside world and they must be able to handle inputs that they donot expect
# If such situations are not handled, the user can break the program


# Error Handling - how to let the program run even if it encounters an Error
# while True: # Keep the program running until the user enters something valid
# try - except
    # try:
        # age = int(input('what is your age ?')) # convert string input to integer
        # 10/age # age could be a alphanumeric or non-digit since it is taken in as a string from the user
    # If anything errors out in the 'try' block, the code from the 'except' block is used to handle it
    # This except block without any specific errors specified will be triggered for any error. ValueError and
    # ZeroDivisionError both will trigger this 'except' block along with other errors.

    # except:
    #     print('please enter a number')

    # except ValueError: # We can be more specific and specify which type of python Errors should trigger the 'except' block
        # print('please enter a number') 
    # except ZeroDivisionError: # This 'except' block is specific to ZeroDivisionError
        # print('please enter age higher than zero')
    # except ValueError: # This 'except' block will never run because we already defined the handling of ValueError in a previous 'except' block
        # print('!!!!')
    # else: # If no error is thrown from the code in the 'try' block, run the code in this 'else' block
        # print('thank you!')
        # break
    # The 'finally' code block runs after either the 'except' block or the 'else' block is executed
    # The 'finally' block is useful to log the user behaviour and intrusions
    # finally:    
        # print('ok, I am finally done!')

# The except block does not provide us any information on what type of error triggered it, unless we specify one for
# each type of error. A better way to handle this is to include the caught error in the message.

def sum(num1, num2):
    try:
        return num1/num2
    # We can also catch multiple python Errors and respond to them like this:
    except (ZeroDivisionError, TypeError) as err: 
        # we can catch the error type and print the error along with a message in the 'except' block.
        return f'Whoopsie {err}'

print()
print()

print("sum(1, 0) : ", sum(1, 0))
print("sum('1', 2) : ", sum(1, 0))


# Exercise
while True: 
    try:
        age = int(input('what is your age ?')) # convert string input to integer
        10/age 
    except ValueError: # if input is a non-digit string
        print('please enter a number')
        continue # next iteration of while loop
    except ZeroDivisionError: # if the input age is 0
        print('please enter age higher than zero')
        # without this break statement, 'can you hear me?' from the last print statement will be printed
        # but the loop will not terminate
        break
    else: # if 'try' block is executed successfully
        print('thank you!')
        # without this break statement, 'can you hear me?' from the last print statement will be printed
        # but the loop will not terminate
        break
    finally: # run everytime after 'except' or 'try' block successfully executes .. even if there is a break
        # statement in the 'except' or 'else' block
        print('ok, I am finally done!')
    print('can you hear me?') # This code will never run because 


# Raising an error in situations where an Error has to be triggered
# while True: 
#     try:
#         age = int(input('what is your age ?'))
#         10/age
#         # We can raise a python Error on our own using the 'raise' keyword
#         raise ValueError('hey, cut it out!') 
#     except ZeroDivisionError: 
#         print('please enter age higher than zero')
#         break
#     else: 
#         print('thank you!')
#         break
#     finally: 
#         print('ok, I am finally done!')