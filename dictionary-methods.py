# Dictionary is a collection of unorderedkey: value pairs
dictionary = {
    'a': [1, 2, 3],
    'b': "Hello",
    'x': True
}

# Accessing dictionary values
print('Value of Key "b" in', dictionary, 'is : ', dictionary['b'])
print('Value of Key "a" in', dictionary, 'is : ', dictionary['a'], 'and its second element is', dictionary['a'][1])


# List of Dictionaries
my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'x': True 
    },
    {
        'a': [4, 5, 6],
        'b': 'Hello',
        'x': True 
    }
]

print('my_list: ', my_list)
print("my_list[0]['a'][2] = ", my_list[0]['a'][2])

# Remember that lists have order whereas a dictionary does not. Dictionary holds more information than a list.


# A dictionary's value can hold any sort of datatype. A dictionary's key should be IMMUTABLE, like strings or
# literal values. 
dictionary = {
    123: [1, 2, 3],
    True: "Hello",
    'isMagic': True
}

print('dictionary = ', dictionary)
print('dictionary[123] = ', dictionary[123])
print('dictionary[True] = ', dictionary[True])



# Dictionary keys must also be UNIQUE. If multiple duplicate keys are given to the dictionary, the value will be
# overwritten when the duplicate key is encountered.
test_dictionary = {
    '123': [1, 2, 3],
    '123': 'Hello'
}
print("test_dictionary = {'123': [1, 2, 3], '123': 'Hello'} will return", test_dictionary)
print("test_dictionary['123'] = ", test_dictionary['123'] )


# use the .get() method on a dictionary to get values from a dictionary when you donot know if the key exists
# in the dictionary. This returns None when the key is absent in the dictionary instead of throwing keyNotFound
# error
user = {
    'basket': [1, 2, 3],
    'greet': 'Hello'
}
print('user = ', user)
print("user.get('age') = ", user.get('age'))
# You can also change the default value returned (None) when the key is not present in the dictionary 
# when using .get()
print("user.get('age', 55) = ", user.get('age', 55))


# Other ways to create dictionaries
user2 = dict(name="JOJO")
print("user2 = dict('JOJO') will create the dictionary: ", user2)

# Check if a Key exists in the dictionary
print("Is the key 'basket' in ", user, "?: ", 'basket' in user)
print("Is the key 'size' in keys of the dictionary", user, "?: ", 'size' in user.keys())

# Check if a value exists in the dictionary
print("Is the Value 'Hello' in values of the dictionary", user, "?: ", 'Hello' in user.values())

# Empty a dictionary inplace using the .clear() method
print('dictionary before clearing: ', user)
user.clear()  # inplace
print('dictionary after clearing: ', user)

# Copy a dictionary into another variable instead of creating a reference of it
user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}
print("Original dictionary user: ", user)
user2 = user.copy()
print("Copied dictionary user2 = user.copy(): ", user2)
# .pop() method removes the key: value pair from the dictionary if the key exists in the dictionary inplace.
# .pop() also returns the value of the popped key: value pair
print("user.pop('age') : ", user.pop('age'))
print("User after popping the key 'age'", user)
# .popitem() removes the last key: value pair from the dictionary and returns that last pair
print("user2 before popitem(): ", user2)
print("user2.popitem(): ", user2.popitem())
print("user2 after popitem(): ", user2.popitem())

# Update a key: value in the dictionary
# The .update() method adds the key: value pair to the dictionary if the key is not present in the dictionary.
# If the key is already present in the dictionary, the .update() methods simply updates the key's value
# Remember, the .update() method works inplace
user2.update({'age': 65})  # inplace
print("user2 after updating it with user2.update({'age': 65})", user2)

# Get an iterable of key: value pairs from the dictionary:
print("user.items() = ", user.items())