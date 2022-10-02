# Functonal Programming is another Paradigm of Programming just like OOP
# FP is based on seperation of concerns - each part of the program is concerned with one thing that it is good at
# Just like organization of code into Classes with methods and attributes in OOP, FP seperates Data and Functions
# Unlike OOP, in FP, Data and the Functions that act upon it are not combined together - they remain seperated.
# In FP, functions operate on well-defined data structures like lists, and dictionaries rather than an object.
# Just like OOP, the goal of the FP paradign is also to make code:
#   * Clean + Understandable
#   * Easy to Extend
#   * Easy to Maintain
#   * Memory Efficient
#   * Donot Repeat Yourself



# The main pillar of FP is PURE FUNCTIONS
# PURE FUNCTIONS: 
#   * Everytime the same input is given, the Pure Function should always return the same output
#   * No Side Effects - converts input to output without affecting the outside world - No printing to screen or
#       accessing variables out of the function's scope


# A PURE FUNCTION
def multiply_by2(li):
    # if this empty list was initialized outside this function and accessed here, this function becomes impure
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list # if we print instead of returning, this function becomes impure

print(multiply_by2([1, 2, 3]))

# Pure Functions help to write less buggy code

wizard = {
    'name': 'Merlin',
    'power': 60
}

def attack(wizard):
    return f"attacking with power {wizard['power']}"

print("attack(wizard) :" , attack(wizard))


# COMMON FP FUNCTIONS IN PYTHON
# map, filter, zip, reduce - apply Functions on every element of an iterable and combine the results in a
# meaningful way

# map applies a function of every element of an iterable data object, it returns a map object, leaving the original
# data untouched
def mult(item):
    return item * 2
print("map(mult, [1, 2, 3]) : ", map(mult, [1, 2, 3]))
print("list(map(mult, [1, 2, 3])) : ", list(map(mult, [1, 2, 3])))

print()
print()

# Filter ideally takes a function that returns a boolean and uses it to filter the data and give out only
# the items that return True for the filter function. It also leaves the original data untouched.

def odd(item):
    return item % 2 != 0

print("filter(odd, [1, 2, 3, 4, 5, 6, 7, 8]) : ", filter(odd, [1, 2, 3, 4, 5, 6, 7, 8]))
print("list(filter(odd, [1, 2, 3, 4 ,5 ,6 ,7, 8])) : ", list(filter(odd, [1, 2, 3, 4, 5, 6, 7, 8])))

print()
print()

# zip - zipper that iterates over two or more iterables and returns the next element from each of them as a tuple. 
# The zip function returns the next element from both the iterable until one of the iterable is exhausted
print("zip([1, 2, 3, 4], [5, 6], [3, 2, 1]) : ", zip([1, 2, 3, 4], [5, 6], [3, 2, 1]))
print("list(zip([1, 2, 3, 4], [5, 6], [3, 2, 1])) : ", list(zip([1, 2, 3, 4], [5, 6], [3, 2, 1])))

print()
print()

# reduce - it is not a built-in function in base python. It has to be imported from 'functools' package
from functools import reduce # 'functools' is a functional programming toolbelt that comes with python installation
# reduce takes an accumulator function and applies it with the initial value (which will be 0 by default) and the
# first element of the iterable passed to reduce() call. The result of this operation will be carried forward as 
# the initial value for applying the accumulator function on the second element of the iterable and so on. 
# The reduce() call returns a single value which is the result of applying the accumulator function on the final
# element of the passed iterable, with the initial value carried forward till the final item of the iterable.
def accumulator(acc, item): # An accumulator function for reduce() has to take two parameters
    # The first parameter 'acc' is the initial value and the second parameter is the item from the iterable.
    print(acc, item) # Not ideal for a pure function
    return acc + item

# The reduce() call takes the accumulator function, the iterable and optionally, the initial value to use.
print("reduce(accumulator, [1, 2, 3, 4, 5]) : ", reduce(accumulator, [1, 2, 3, 4, 5]))
print("reduce(accumulator, [1, 2, 3, 4, 5], 10) : ", reduce(accumulator, [1, 2, 3, 4, 5], 10))


# lambda functions - one time anonymous functions
# lambda <params>: <action(params)>
print()
print()
print("USING LAMBDA EXPRESSIONS (anonymous functions):")
print("list(map(lambda x: x * 2, [1, 2, 3])) : ", list(map(lambda x: x * 2, [1, 2, 3])))
print("list(map(lambda x: x ** 2, [5, 4, 3])) : ", list(map(lambda x: x ** 2, [5, 4, 3])))
print("reduce(lambda acc, item: acc + item, [1, 2, 3, 4, 5], 0) : ", reduce(lambda acc, item: acc + item, [1, 2, 3, 4, 5], 0))
# Many other functions python such as sorted() or list.sort() can use lambda expressions
print("sorted([(0, 2), (4, 3), (9, 9), (10, -1)], key = lambda x: x[1])", sorted([(0, 2), (4, 3), (9, 9), (10, -1)], key = lambda x: x[1]))


print()
print()


# List / Set / Dictionary Comprehension

# Shortcuts for creating lists, sets and dictionaries
my_list = []
for char in 'hello':
    my_list.append(char)

print('my_list : ', my_list)

# Using comprehension
# List Comprehension:
print("[char for char in 'hello'] : ", [char for char in 'hello'])
print()
print("[num for num in range(0, 100)] : ", [num for num in range(0, 100)])
print()
print("[num*2 for num in range(0, 100)] : ", [num*2 for num in range(0, 100)])
print()
print("[num*2 for num in range(0, 100) if num % 2 == 0] : ", [num*2 for num in range(0, 100) if num %2 == 0])
print()
print()
print()
# Set Comprehension:
# Works exactly like list comprehension, but will not contain duplicates
print("{char for char in 'hello'} : ", {char for char in 'hello'} )
print()
print()
print()

# Dictionary Comprehension:
print("{key:value**2 for key, value in zip(['a', 'b', 'c'], [1, 2, 3]) if value % 2 == 0} : ", {key:value**2 for key, value in zip(['a', 'b', 'c'], [1, 2, 3]) if value % 2 == 0})
print("{num: num * 2 for num in [1, 2, 3]} : ", {num: num * 2 for num in [1, 2, 3]})

exercise_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print("Duplicates : ", list({char for char in exercise_list if exercise_list.count(char) > 1}))