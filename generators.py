# Generators - how to pause and resume functions ?
# Generators are functions that return values in a memory-efficient way without taking up too much space
# Generators can remember the iteration state
range(100) # An example of a generator - creates the elements one-by-one
list(range(100)) # Creates a giant list of 100 elements in computer memory

# A function to use range() - a generator, to create a list in memory
def make_list(n):
    result = []
    for i in range(n): # Here, range(n) gives one element for each iteration - It does not store the entire 
        # 'n' elements in memory like creating a list does
        result.append(i * 2)
    return result

my_list = make_list(100) # my_list is taking up space in memory, it is poiting to a location in memory
print("my_list", my_list)


# Iterables - any object in python which we are able to loop/iterate through because of its '__iter__()' 
# dunder method that works underneath the hood
# Generators are iterables - everything that is a generator is a iterable, but everything that is iterable is not
# a generator
# range() is a generator (because it is a function) whereas list() is an iterable (because it uses up memory)

def generator_function(num):
    for i in range(num):
        yield i # 'yield' pauses the function and retruns the next element when we come back to it using 'next'

for item in generator_function(1000):
    print(item)

print()
print()

# create a generator function as a variable and iterate over it
g = generator_function(100)
print(next(g)) # returns first item from generator
print(next(g)) # returns second item from generator

# When we exhaust the generator using next() calls, it throws a StopIteration Error which is automatically
# taken care of when we loop through generators, but can be seen when we use more next() calls that elements in the
# generator
print()
print()
two = generator_function(2)
print(next(two))
print(next(two))
# print(next(two)) # StopIteration error

print()
print()

from re import A
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1} s')
    return wrapper

# Must be much faster than than the other version
@performance
def long_time():
    print('I')
    for i in range(10000000): # A generator
        i * 5

@performance
def long_time2():
    print('II')
    for i in list(range(10000000)): # A list
        i * 5

long_time()
long_time2()

print()
print()

# An example generator
def gen_func(num):
    for i in range(num):
        yield i

# Implementing a for loop - The for loop actually creates an iterator object and executes the next() method 
# for each loop.
def special_for(iterable):
    # Lists, tuples, dictionaries, strings and sets are all iterable objects. 
    # They are iterable containers which you can get an iterator from.
    iterator = iter(iterable) # iter() returns an iterator object from an iterable
    # Converting the iterable to an iterator allows us to use the next() function on the iterator to get the
    # next element from the iterable
    while True:
        try:
            print(iterator)
            print(next(iterator)) # next() calls the __next__() dunder method of the iterator under the hood
        except StopIteration: # break the while loop when the next() call on the iterator throws StopIteration Error
            break

special_for([1, 2, 3])

print()
print()

# Implementing range() function
# Generators remember their iteration state. One way to achieve this is by using a class variable to track the
# iteration steps
class MyGen():
    current = 0 # iteration tracker
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self): # __iter__() is the dunder method that allows us to create an iterable
        return self
    def __next__(self): # for the next() call on an object of this class
        if (MyGen.current < self.last):
            num = MyGen.current
            MyGen.current += 1 # increment the iteration tracker
            return num
        raise StopIteration # when we reach current > self.last



gen = MyGen(0, 100)
for i in gen:
    print(i)

print()
print()
print('Fibonacci : ')
# Fibonacci Number using Generator
def fib(number):
    i = 0
    j = 1
    for n in range(number + 1):
        yield i # this 'yield' keyword indicates this function to be a generator to python
        temp = i
        i = j
        j = j + temp 

print(fib(100)) # The function call produces a generator object because of the 'yield' keyword within 
for x in fib(100):
    print(x)

print()
print()

# Generators with Comprehension
# Just like list comprehension, we can also produce generator objects by replacing the square prackets with
# parantheses
print('Generator Comprehension : ')
print((i for i in range(100))) # generator for natural numbers < 100
print((i for i in range(100) if i % 2 == 0)) # generator for even numbers within 100
