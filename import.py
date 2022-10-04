# Importing code from other python scripts
# A __pycache__ directory will be created everytime we run a python script with an import statement or
# everytime we use a module. This __pycache__ directory will contain the compiled versions of your modules/scripts - 
# these will be created when you import them for the first time within a python script.
# Subseqeuent imports will use the cached compiled versions of the code files if there are no changes in the code
# import utility # modules are simply other python scripts - importing the whole module
# from utility import * # BAD PRACTICE - import everythin from utility - always be explicit with your imports
from utility import multiply, divide, max # importing multiple functions from a module directly
# The 'max' function imported here takes precedence over the built-in 'max' function in python
# importing a package - a package is simply a folder containing modules
# import shopping.more_shopping.shopping_cart # import package_name.sub_package_name.module_name
# from shopping.more_shopping import shopping_cart # import entire module in short-form
from shopping.more_shopping.shopping_cart import buy # import specific functions from package_name.sub_package_name.module
# Every package folder should have the __init__.py script (which can be empty) to indicate that the directory
# is part of a python package.

# This is a way to execute actions only when the correct script is run in large projects
print("__name__ : ", __name__) # This will be '__main__' - The environment where top-level code is run. 
if __name__ == '__main__': 
    # The dunder variable '__name__' given to the code file that is running will be '__main__'.
    # The code file specifically run through the command prompt/terminal will by default have '__name__' set to '__main__'
    print('please run this!')


# print("utility : ", utility)
# print("shopping.more_shopping.shopping_cart : ", shopping.more_shopping.shopping_cart)
# use functions from the imported code files
# print("utility.multiply(2, 3) : ", utility.multiply(2, 3))
print("multiply(2, 3) : ", multiply(2, 3)) # 'multiply' was imported specifically from 'utility'
print("divide(5, 2) : ", divide(5, 2)) # 'divide' was imported specifically from 'utility'
# print("shopping.more_shopping.shopping_cart.buy('apple')", shopping.more_shopping.shopping_cart.buy('apple'))
print("but('apple') : ", buy('apple')) # 'buy' was imported specifically from 'shopping.more_shopping.shopping_cart'
# print("max([1, 2, 3]) : ", max([1, 2, 3])) 
# # 'max' from 'utility' will be used as it is imported here instead of python's build-in 'max'


# This '__main__' based name for the script being run can be seen in classes and Objects as well
class Student():
    pass

st1 = Student()
print(st1)

print()
print()
# Python in-built modules index: https://docs.python.org/3/py-modindex.html
import random
print(random) # imported built-in 'random' module
# help(random) # helpful documentation of the module
print("dir(random) : ", dir(random)) # shows all the methods available in this module / package

print()
print()
# Print a random number between 0 and 1
print("random.random() : ", random.random())
print("random.random(1, 10) : ", random.randint(1, 10)) # random integer between 1 and 10.
print("random.choice([1, 2, 3, 4, 5]) : ", random.choice([1, 2, 3, 4, 5])) # randomly pick an element from the 
# given iterable
# Shuffle the elements in the given iterable inplace
my_list = [1, 2, 3, 4, 5]
print("my_list : ", my_list)
random.shuffle(my_list) # happens inplace
print("After random.shuffle(my_list) happens inplace : ", my_list)

# We can also give an alias to the imported module
import random as oulala
print("oulala.random() : ", oulala.random())

# REMEMBER - ONLY IMPORT THE FUNCTIONS YOU WANT ... NOT THE WHOLE MODULE / PACKAGE - TO SAVE MEMORY

