# Specialized DataTypes from python modules

from collections import Counter, defaultdict, OrderedDict
# 'Counter' and 'OrderedDict' are classes whereas 'defaultdict' is similar to a function

li = [1, 2, 3, 4, 5, 6, 7, 7]
# 'Counter' creates a dictionary (hashmap) that keeps track of how many times an element occured in an iterable
print("Counter(li) : ", Counter(li))
print("Counter('blah blah blah thinking of python') : ", Counter('blah blah blah thinking of python'))


print()
print()

# 'defaultdict' allows us to create default values for keys not present in the dictionary.
# 'defaultdict' takes a 'default factory' (callable / function without any arguments) that it used to generate the
# value for keys not present in the dictionary.
dictionary = {'a' : 1, 'b': 2}
# print(dictionary['c']) # KeyError

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print("dictionary['c'] : ", dictionary['c'])

# An 'OrderedDict' retains the order in which you insert items into the dictionary.
# Hence, two 'OrderedDict' with different order will not be equal.
# FROM PYTHON 3.7, EVEN REGULAR DICTIONARIES BEHAVE LIKE ORDERED ONES
d = {'a': 1}
d['b'] = 2

d0 = {'b': 2}
d0['a'] = 1

print("dict d : ", d)
print("dict d0 : ", d0)
print("d == d0 : ", d == d0)

print()

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print("OrderedDict d1 : ", d1)
print("OrderedDict d2 : ", d2)
print("d1 == d2 : ", d1 == d2)

print()
print()


# WORKING WITH DATE AND TIME

import datetime

print("Date and Time now = datetime.datetime.now() : ", datetime.datetime.now())
print("datetime.time(5, 45, 2) : ", datetime.time(5, 45, 2))

from time import time
print("time() : ", time())


# lists in python grow in memory as more elements are added. Arrays in python are memory-restricted lists.
# We can set the number of elements that an array can hold and thereby control the storage memory it uses.
# an array is initialized with a 'typecode' that specifies the type of data that the array will hold
from array import array

# arrays are an alternative to generators - for making lists memory efficient
print("array('i', [1, 2, 3]) : ", array('i', [1, 2, 3]))
print("array('i', [1, 2, 3])[1] : ", array('i', [1, 2, 3])[1])