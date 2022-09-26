# Tuple - are like immutable lists

my_tuple = (1, 2, 3, 4, 5)
print("Elelemt at index '1' of tuple", my_tuple, "is: ", my_tuple[1])
print("Is the element '5' in tuple:", my_tuple, "?: ", 5 in my_tuple)
# A dictionary can have a tuple as a key
user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print("Dictionary user: ", user)
print("Dictionary elements from 'user' as (key, value) tuples : user.items(): ", user.items())
print("value from 'user' corresponding to the key (1,2) which is a tuple: ", user[(1, 2)])


# tuples can be subset just like lists
new_tuple = my_tuple[1:2]
print("my_tuple = ", my_tuple)
# A tuple with only a single item will have a ',' seperator at the end, but it is still a tuple
print("my_tuple[1:2] = ", my_tuple[1:2])
print("my_tuple[1:4] = ", my_tuple[1:4])
x, y, z, *other = (1, 2, 3, 4, 5, 5)
print("x, y, z, *other = (1, 2, 3, 4, 5)")
print("x = ", x)
print("y = ", y)
print("z = ", z)
# Tuple unpacking automatically puts the elements into a list
print("other = ", other)
print("my_tuple.count(5) = ", my_tuple.count(5))
# .index() Returns the index of the first occurrence of the value in the tuple
print("my_tuple.index(5) = ", my_tuple.index(5))
print("len(my_tuple) = ", len(my_tuple))