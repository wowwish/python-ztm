# Decorators are the @classmethod, @staticmethod used in class methods and static methods 
# Functions in python can be passed around as arguments and act just like variables
# Decorators supercharge functions by adding extra functionality to it

# Function stored in memory with its reference name as 'hello'
def hello():
    print('Hello')

greet = hello # greet refers to the function referenced by 'hello'
del hello # the 'hello' reference is deleted
greet() # 'greet()' call will still work even though the 'hello' reference is deleted


# Functions are just like Variables in Python
# Higher Order Function (HOF) is a function that accepts another function as an argument or returns another
# function as the output
def hello(func): # take a function as parameter - Higher Order Function
    func() # call the passed function

def greet():
    print('still here!')

# A higher order function that returns another function
def greet2():
    def func():
        return 5
    return func # A function created within 'greet2' is returned

# map, filter, reduce all are higher-order-functions in python
hello(greet)

print()
print()

# Decorators are higher-order functions
# Decorator definition / Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs): # adding additional functionality in the wrapper function of the decorator function
        print('*******')
        # Unpacking the passed arguments
        func(*args, **kwargs)
        print('*******')
    return wrap_func

# Using a decorator
@my_decorator # this is equivalent to my_decorator(say_hello)
def say_hello(greeting, emoji):
    print(greeting, emoji)

@my_decorator # this is equivalent to my_decorator(bye)
def bye(salutation, emoji):
    print(salutation, emoji)

say_hello('Hello!', ':)') # calling the decorated function
print()
bye('See ya!', ':)')

print()
print()

# Building another Decorator - to test how fast a code block / function runs
# Import additional functions required 
from time import time 

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time() # Time before running the passed function
        result = fn(*args, **kwargs)
        t2 = time() # Time after running the passed function
        print(f'It took {t2 - t1} s') # t2 - t1 is the total time taken by the function to run
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i * 5

long_time()


print()
print()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid'] == True:
            fn(*args, **kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)