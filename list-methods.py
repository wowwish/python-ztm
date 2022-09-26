basket = [1, 2, 3, 4, 5]

# List slicing - returns a sliced copy of the original list. If this sliced copy is stored to a variable,
# any changes to the sliced copy will not be reflected on the original list. Remember in list slicing,
# the element at the start index will be included in the returned copy, but the element at the end index will
# not be returned.
print("The elements between index 0 and 3 in", basket, "are: ", basket[0:4])

# Length of list - number of elements in it
print('basket has', len(basket), 'elements: ', basket)
# adding - append changes the list inplace
# new_list = basket.append(100)
# new_list = basket.insert(4, 100)  # insert modified list inplace
new_list = basket.extend([100, 101])  # extend modifies list inplace as well
print("Basket:", basket)
print(new_list)
print("Extended Basket:", basket)


# removing
print("Pop:", basket.pop())     # pop returns the removed value. It removes the last element by default.
print("Basket:", basket)
print("Pop index 0:", basket.pop(0))    # pop returns the removed value, and index can be specified to remove value
print("Basket:", basket)
basket.remove(4)    # remove works inplace
print("Remove value '4' from Basket:", basket)
basket.clear()  # clear() empties the list inplace
print("Cleared Basket:", basket)



# Other List Operations

basket = ['a', 'b', 'c', 'd', 'e', 'd']
print('Index of value "d" in', basket, 'is', basket.index('d')) # .index() always returns index of first occurrence
# The .index() method can take additional arguments 'start' and 'stop' and will search for the value by 
# subsetting the list first with the given 'start' and 'stop' values.

# This will throw error because the element at the 'stop' index is not included in the list subset and hence, 
# 'c' is not included in the subset that is searched
# print('Index of "c" in', basket, 'when it is subset from 0 to 2 is', basket.index('c', 0, 2))
print('Is "d" in basket ?', "d" in basket)
print('Is "x" in basket ?', "x" in basket)
print('Is "i" in "Hi, I am Ram ?"', "i" in "Ram")

# Add another 'd' to basket and count its occurrence in the list
print('Number of "d" in',basket, 'is', basket.count('d'))

# .sort() method sorts the elements of the list inplace
print('Before Sort: ', basket)
basket.sort() # inplace
print('After Sort: ', basket)

# sorted() function returns the sorted list
new_list2 = ['a', 'b', 'x', 'j', 'w']
print('Unsorted: ', new_list2)
print('Sorted: ', sorted(new_list2))

# .reverse() will reverse the order of elements in the list inplace
print('Basket: ', basket)
basket.reverse() # inplace
print('Reversed Basket: ', basket)

# Remember that this slicing method to reverse a list returns a new reversed copy of the list. It is not inplace.
# basket[:] also simply returns a full copy of basket without any modifications
print('Create a new Re-reversed basket: ', basket, 'using another way basket[::-1] = ', basket[::-1])


# Building list of sequences - Remember, the range() function returns a Range object which need to be converted
# to a list to be viewed.
print('Range object of 1 to 100: ', range(1, 101))
# Remember, the 'stop' value of the range will not be included in the sequence. So if you want to include it, you
# need to set the stop value appropriately. 
print('List of 1 to 100: ', list(range(1, 101)))
# range() can also be used with just the stop value, in which case, it will assume the start as 0 (Default)
print()
print()
print('One to 99:', list(range(100)))

# Join list of strings using a delimiter
print(' ! '.join(['MONKEY', 'NANDAYO', 'JOJO']))
print()
print()
print()


# List unpacking
a, b, c = 1, 2, 3
print('a, b, c = 1, 2, 3')
print('a = ', a)
print('b = ', b)
print('c = ', c)
print()
print()


a, b, c, *other = [1, 2, 3, 4, 5, 6]
print('a, b, c, *other = [1, 2, 3, 4, 5, 6]')
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('other = ', other)
print()
print()

# Only one unpack operation (*other) is allowed per list
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('other = ', other)
print('d = ', d)