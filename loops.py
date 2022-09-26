# Loops allow us to run the same lines of code lines multiple times over and over
# Here, the variable 'item' is created for each item in the iterable after the 'in'
# An iterable is an object or collection of objects that is able to get looped over or
#  allows to iterate over its items

for item in 'STRING':  # strings are iterables
    print(item)

print()
print()

for item in [1, 2, 3, 4, 5]:  # iterables can be lists, tuples, dictionaries or sets
    # iterables can be inter-converted using functions like list(), dict(), tuple(), set()
    # iterating -> one by one, check each item in the collection
    print(item)
print("item after loop ends: ", item)

# Iterating over dictionary
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
print()
print()

print("Dictionary: ", user)
print("Iterating over (key, value) pairs of a dictionary: ")
for item in user.items():
    print(item)
print("Iterating over only values of dictionary")
for item in user.values():
    print(item)
print("Iterating over only keys of dictionary")
for item in user:  # or user.keys()
    print(item)

# Common pattern with dictionary
print("using for k,v in user.items():")
for key, value in user.items():
    print([key, value])

print()
print()


# Nested loops
print("Nested Loops")
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)


print()
print()

# Counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0  # initialize the total to 0 outside the loop, if this is inside the loop, everytime the value will
# be reset to 0 .. so your total will become 10 instead of 55.
for item in my_list:
    total += item
print("Counter: ", total)

print()
print()


# range() returns a special type of iterable object in python that returns a sequence of integers from a start value
# to a stop value. range() also takes a third parameter that specifies the step over size (Default is 1).
# REMEMBER: range(start, stop, step) will include the start value in the sequence, but the stop value will be
# excluded from the number sequence
# range(0, 10, 2) will return all even numbers between 0 and 99
# The default start of range is 0. If only one argument is used in the range() call
print("range(100): ", range(100))
# the value is assigned to stop.
for number in range(0, 100):
    print(number)  # We can do any operation on each number of the sequence
    # We can also simply perform an action 100 times

print()
print()

# You can tell the loop how many times to run using the range object
for _ in range(0, 10):
    print("Sending Email")

print()
print()

nums = []
for num in range(0, 10, 2):
    nums.append(num)
print("Even numbers between 0 and 10: ", nums)

# Negative step size - reverse sequence of numbers - stop > start
# range objects can be converted to a list of numbers using list() like most iterables
reverse = list(range(10, 0, -1))
print("Reverse: ", reverse)

print()
print()

# Create many lists of number sequences quickly
for _ in range(2):
    print(list(range(10)))


print()
print()


# enumerate() - takes an iterable object and returns an index as well as the item at the index in the iterable
# at every iteration
print("Enumerate index counter and char in a string:")
for i, char in enumerate('Hello'):
    print(i, char)
print("Enumerate index counter and number in a string:")
for i, num in enumerate(list(range(100))):
    print(i, num)
    if (num == 50):
        print(f"The index of 50 is: {i}")


# While Loops
# while condition is true, do something
# Without a termination condition, while loops will run infinitely. Hence, a termination condition is neccessary,
# especially in while loops
i = 0
while i < 50:
    print(i)
    i += 1  # Helps in loop termination
else:  # execute the lines below when the while loop executes completely without any 'break' statements
    # this else block will not run if the while loop is terminated used a 'break' statement
    print("done!")

# While loops are more flexible in the actions that can be performed within the loop, whereas for loops are really
# simple and does not require terminations specific actions

print()
print()
print("While loop to iterate over a list of elements: ")
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


print()
print()

# while True: # Non-termination condition
#     response = input("say something ('bye' to quit): ")
#     if (response == "bye"):
#         break # break out of the loop after performing action


# break - terminate the loop within which the 'break' keyword is used
# continue - stop the current iteration (any code lines below this 'continue' statement) and move to the next
# iteration of the loop
# pass - Used as placeholder for future code / dummy execution

print("Using 'continue' to skip code execution within a loop: ")
my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item)  # this line will never be executed in any of the iterations

print("'pass' does nothing. it is just a placeholder for empty code: ")
i = 0
while (i < len(my_list)):
    pass  # dummy / placeholder to prevent errors from empty code
    i = i + 1  # termination condition to prevent infinite loop
