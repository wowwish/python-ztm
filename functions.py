# Functions can be defined using the 'def' keyword and can be named using the same convention as variables
def say_hello(): # The paranthesis pairs indicate this is a function that performs an action
    print('Hello') # The code block within a function should also be indented

# The defined function lives somewhere in memory, but it will not yet be executed. To use the function, we need
# to call the function 
say_hello()

# If you do a function call without the paranthesis, nothing will happen because the interpreter will not run it
say_hello

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# REMEMBER: a function cannot be called before it is defined or imported in python
# because python uses an interpreter that checks code line by line
def show_tree():
    for row in picture:
        for col in row:
            if col:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Multiple function calls to perform the same action
show_tree()
show_tree()
show_tree()


print()
print()
print()

print("Function show_tree and its memory location: ", show_tree)



# Arguments and Parameters

# Functions can be made dynamic by giving it parameters in its definition. A function can take any number of 
# parameters of any python data type
def say_hello(name, emoji): # 2 parameters
    print(f"hello {name}{emoji}")

# Arguments are the actual values we provide to the function call.

# These calls use positional arguments - The corresponding parameter name is assumed by the function based
# on the position of the argument in the function call.
say_hello('Dio', '😁') # 2 arguments to the function
say_hello('Jotaro', '😁') # 2 arguments to the function
say_hello('😁', 'Speedwagon') # 2 arguments to the function - twist on argument position


# Using keyword arguments
say_hello(emoji= '😁', name='Bibi')

# Setting default parameter values in the function Definition can also be done and these default values will be used
# in the function when no arguments are given to the function. If any arguments are given to the function, they will
# override the default parameter values of the function
def say_hello_default(name = 'Darth Vader', emoji= '🤡'):
    print(f"hello {name}{emoji}")

# Testing the default parameters
say_hello_default()
# Overriding the default parameter values
say_hello_default(name="Crypto", emoji="👽")


# Functions that return values - the 'return' statement
# By default, functions return 'None' when they don't have any 'return' statement
# REMEMBER: any code below the 'return' statement will not be run when you return something, in the function using
# the 'return' statement
def total(num1, num2):
    num1 + num2

print("No return - total(4, 5): ", total(4, 5))

# GOOD PRACTICE: A function should do only one thing, really well and return something

# Function with return
def total(num1, num2):
    return num1 + num2
    print("Im a hidden ninja!") # this code comes below the return statement. Hence, It will not be run.
    # The 'return' statement automatically exits the function.

total = total(10, total(4, 5)) # Nested call of total()
print("With return, total(4, 5): ", total)


# NESTED FUNCTIONS

# Function inside a function - No return statement for the primary function
def total(num1, num2):
    def another_function(num1, num2):
        return num1 + num2 # return statement of sub-function will not exit the primary function. The primary 
        # function total() in this case will return 'None' by Default due to the lack of a 'return' statement 
        # corresponding to it.

total = total(10, total(4, 5))
print("calling total(10, total(4, 5)) when 'total' contains the definition of another function inside it.")
print("total() does not contain a return statement for itself, but a return statement for the function\m \
    defined inside of it is present")
print("Total: ", total) # 'total' is 'None' here because nothing is returned by total() due to lack of return statment


# The primary function can return any auxilliary functions defined inside of it
def total(num1, num2):
    def another_function(num1, num2):
        return num1 + num2
    return another_function

total = total(10, total(4, 5))
print("The primary function total() now returns the auxilliary function defined inside of it and also has its own \n \
'return'\n statement now")
print("total(10, total(4, 5)): ", total) # Note that a function is returned now, not a value


# The primary function can run auxilliary functions defined inside of it, within itself and return values
def total(num1, num2):
    def another_function(n1, n2):
        return n1 + n2
    return another_function(num1, num2) # calling defined sub-function within the primary function

total = total(10, total(4, 5))
print("The primary function total() can define and run a sub-function within itself, it can also return the \n \
    call to the sub-function with proper arguments to it. This will return the value returned by the sub-function")
print("total(10, total(4, 5)): ", total)


# Check Driver Age
def checkDriverAge(age=0):
    if (int(age) < 18):
        print("Sorry, you are too young to drive this car. Powering off")
    elif (int(age) > 18):
        print("Powering On. Enjoy the ride!")
    elif (int(age) == 18):
	    print("Congratulations on your first year of driving. Enjoy the ride!")


# Methods Vs Functions
# A method is owned by a python object. However functions are not.
# Function
def get_string():
    pass
# Method
print('Method .capitalize() is owned by string objects in python')
print('hello'.upper())


# Docstrings
def test(a):
    '''
    Info: This function tests and prints param a
    '''
    print(a)

test('!!!')
# We can get the docstring of a function to get information about the function using help()
help(test)
print('Docstring of function "test": ', test.__doc__)


# Clean Code
def is_even(num):
    return num % 2 == 0

print(is_even(51))


# IMPORTANT: *args and **kwargs
def super_func(zero, *args, i='hi', **kwargs): # here, '*args' tells that 'args' can accept any number of positional arguments
    # and '**kwargs' can accept any number of keyword arguments
    print("positional arguments '*args' inside the function: ", *args)
    print("keyword arguments '*kwargs' inside the function: ", *kwargs)
    print("'args' inside function: ", args) # 'args' contains a tuple of all the positional arguments
    print("'kwargs' inside function: ", kwargs) # 'kwargs' contains a dictionary of all the keyword arguments
    total = 0
    for item in kwargs.values():
        total += item
    print("zero: ", zero)
    return "sum(args) = " + str(sum(args) + total)

print(super_func(0, 1, 2, 3, 4, 5, num1=5, num2=10)) # 5 positional arguments and 2 keyword arguments

# REMEMBER: *args is a standard name used for positional argument variable, but this variable can have any valid
# variable name. Same goes for *kwargs which can also be *kw or *kargs or any other valid python variable name

# RULE OF ORDERING PARAMS: params, *args, default parameters, **kwargs



def highest_even(li):
    max = 0
    for i in li:
        if ((i % 2 == 0) and (i > max)):
            max = i
    return max

print(highest_even([10, 2, 3, 4, 8, 11]))