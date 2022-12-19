# Scope - what variables do I have access to ?
# Scope allows use to make judicious use of the compute resources
# If every variable was in the global scope, we will fill up the memory pretty fast and makes larger programs inefficient
# Once a function call is finished, all the local variables created by the function will be destroyed by the 
# python interpreter - Garbage Collection (emptying memory)

# global scope
total1 = 100


if True:
    # global scope
    x = 10

# A new scope is created inside functions - anything created inside functions belongs only within the function.
def some_func():
    print("x: ", x)
    # local scope
    total2 = 100

some_func()

print("total1: ", total1)
# print("total2: ", total2) # error


a = 1
def confusion():
    a = 5
    return a

def parent():
    a = 10 # parent scope of confusion will be used inside confusion() if no 'a' is available in confusion's 
    # local scope
    def confusion():
        print(sum)
        return a
    return confusion() # return value from confusion() call

print()
print()

print(a)
print(confusion())

print()
print()

print(confusion())
print(a)

print()
print()

print(parent())
print(a)

# PYTHON SCOPING RULES:
#1 - start with local scope variable
#2 - Parent scope 
#3 - global scope
#4 - built-in python variables and functions

# FUNCTION PARAMETERS HAVE LOCAL SCOPE WITHIN THE FUNCTION

def confusionb(b):
    print(b)
    a = 90

print()
print()

total = 0 # global scope - set total to 0
def count():
    # total = 0 # everytime you run the function, the count will be reset to 0 because of this statement
    # total += 1 # local scope - will give unassigned local variable referenced before assignment
    global total # use the global variable 'total' if it exists - BAD PRACTICE
    total += 1
    return total

count()
count()
print("total after three counts: ", count())

print()
print()

# NONLOCAL - a new keyword in python 3 used to refer to the variable of the same name in the parent local scope.
def outer():
    x = "local"
    def inner():
        nonlocal x # x in inner() is now a reference to the x in the parent scope of function outer() - BAD PRACTICE
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)

outer()

# DEPENDENCY INJECTION - GOOD PRACTICE FOR CLEAN CODE
total = 0
def count(total): # here, total is the dependency injected into the function
    total += 1
    return total

print("total after three counts using dependency injection: ", count(count(count(total))))

print()
print()

# Get Dictionary of global variables
print(global())

# Get dictionary of local variables
def func():
    mylocal = 3
    print(local())
    print(local['mylocal'])

 func()


