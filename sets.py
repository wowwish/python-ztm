# Sets are unordered collections of unique objects
my_set = {1, 2, 3, 4, 5, 5}

# Sets will never have duplicates, it will only hold unique elements
print("my_set = {1, 2, 3, 4, 5, 5}: ", my_set)

# The .add() method adds elements to the set if they are unique. It is an inplace operation
my_set.add(100) # inplace
print("my_set.add(100): ", my_set)
my_set.add(2) # inplace
print("my_set.add(2): ", my_set)

# We can use set() function to convert a list to a set and remove duplicate elements
my_set = set([1, 2, 3, 4, 5, 5, 1, 3])
print("my_set = set([1, 2, 3, 4, 5, 5, 1, 3]): ", my_set)

# Sets elements cannot be accessed using index - it will throw error
# print("my_set[0]: ", my_set[0])

# However, we can check if an element is present in a set using the 'in' keyword
print("2 in my_set: ", 2 in my_set)

print("len(my_set): ", len(my_set))

# We can also use the .copy() method to create a copy of the set
new_set = my_set.copy()
my_set.clear() # clearing the old set
print("new_set = my_set.copy(): ", new_set)
print()
print()

my_set = {1, 2, 3, 4, 5,}
your_set = {4, 5, 6, 7, 8, 9, 10}

print("my_set: ", my_set)
print("your_set: ", your_set)

# Sets can be used to perform unions, difference and intersections similar to mathematical sets

# A.difference(B) will return elements in 'A' that are not in 'B'
print("my_set.difference(your_set): ", my_set.difference(your_set)) 

# .discard() removes elements from a set inplace
my_set.discard(5) # inplace
print("'my_set' after discarding the value '5' from it: ", my_set)

# A.difference_update(B) will remove elements of 'B' from 'A' inplace
my_set.difference_update(your_set) # inplace
print("'my_set' after removing elements of 'your_set' from it : ", my_set)

# A.intersection(B) returns common elements between set 'A' and set 'B'
print("{1, 2, 3, 4, 5,}.intersection(your_set): ", {1, 2, 3, 4, 5,}.intersection(your_set))
# The ampersand operator '&' is a shortcut operator to find the intersection of set 'A' and 'B'
print("{1, 2, 3, 4, 5} & your_set : ", {1, 2, 3, 4, 5} & your_set)

# A.isdisjoint(B) returns 'True' if set 'A' and set 'B' have no common elements, 'False' when they don't
print("{1, 2, 3, 4, 5,}.isdisjoint(your_set): ", {1, 2, 3, 4, 5,}.isdisjoint(your_set))
print("{1, 2, 3}.isdisjoint(your_set): ", {1, 2, 3}.isdisjoint(your_set))

# A.union(B) returns a set that has the combined unique elements of both set 'A' and set 'B'
print("{1, 2, 3}.union({4, 5, 6, 7, 8, 9, 10}): ", {1, 2, 3}.union({4, 5, 6, 7, 8, 9, 10}))
# The pipe operator '|' is a shortcut operator to find the union of two sets
print("{1, 2, 3} | {4, 5, 6, 7, 8, 9, 10}: ", {1, 2, 3} | {4, 5, 6, 7, 8, 9, 10})

# A.issubset(B) returns 'True' if all elements of set 'A' is also in 'B', and 'False' if any element of 'A' is
# absent in set 'B'
print("{1, 2, 3, 4, 5}.issubset(your_set): ", {1, 2, 3, 4, 5}.issubset(your_set))
print("{4, 7, 10}.issubset(your_set): ", {4, 7, 10}.issubset(your_set))


# A.issuperset(B) returns 'True' if all elements of set 'B' are also in set 'A', and 'False' if any element of 'B'
# is absent in set 'A'
print("your_set.issuperset({1, 2, 3}): ", your_set.issuperset({1, 2, 3}))
print("your_set.issuperset({4, 7, 10}): ", your_set.issuperset({4, 7, 10}))

