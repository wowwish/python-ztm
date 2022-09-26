# Short Circuiting and Implicit Type Conversions 

# Using 'or' is more efficient than using 'and' in conditions
is_Friend = True
is_User = True

# Here, is_Friend is first checked. If is_Friend is truthy, the if block is executed and is_User is ignored.
# If is_Friend is falsy, only then is_User will be checked.
if is_Friend or is_User:
    print('Friends')

# Similarly here with the 'and' operator, if is_Friend is False, the second expression is_User will not be checked
# as the condition will be falsy anyways 
if is_Friend and is_User:
    print('Best Friends')


# Logical operators
# '=' is used to assign values (it acts like a keyword), '==' is used to check equality
print("4 > 5: ", 4 > 5)
print("4 < 5: ", 4 < 5)
print("4 == 5", 4 == 5)
# The relational operators compare the Unicode values of the characters of the strings from the zeroth index till 
# the end of the string. It then returns a boolean value according to the operator used.
print("'hello' == 'hello'", 'hello' == 'hello')
# when comparing two characters, the character is converted implicitly to unicode value using 'ord(<char>)'
print("'a' > 'b': ", 'a' > 'b') # ordinal value of 'a' is 97 and ordinal value of 'b' is 98, so this is false
# Capital letters have lower ordinal value than small case letters
print("'a' > 'A': ", 'a' > 'A') # ordinal value of 'a' is 97, ordinal value of 'A' is 65

# Here, booleans are converted implicitly to int. True becomes 1 and False becomes 0. Hence The expression becomes:
# True < 3 < 4
# 1 < 3 < 4
# True < 4
# 1 < 4
# True
print("1 < 2 < 3 < 4: ", 1 < 2 < 3 < 4)
# Here, the expression returns False because 1 is not greater than 3 
print("1 < 2 > 3 < 4: ", 1 < 2 > 3 < 4)
print("1 >= 1: ", 1 >= 1)
print("1 <= 1: ", 1 <= 1)
print("1 != 1: ", 1 != 1)


# 'not' operator - returns the opposite boolean value of the operand it is used on
print("1 == 1: ", 1 == 1)
print("not 1 == 1: ", not 1 == 1) 

is_magician = False
is_Expert = True

if is_magician and is_Expert:
    print("you are a master magician")
elif is_magician and not is_Expert:
    print("al least you're getting there")
elif not is_magician:
    print("you need magic powers")


print()
print()

# 'is' Vs '=='
# With '==', python does implicit type conversions when comparing values
print("True == 1: ", True == 1) # 1 is implicitly converted to boolean True and compared
print("'' == 1: ", '' == 1) # '' is falsy which is then converted to 0 and compared
print("'1' == 1: ", '1' == 1) # REMEMBER: string numbers will not be implicitly converted to int when comparing
print("[] == 1: ", [] == 1) # Empty list is falsy, converted to 0 and compared
print("10 == 10.0: ", 10 == 10.0) # 10 is implicitly converted to float and 10.0 == 10.0
print("[] == []: ", [] == []) # 0 == 0
print("[1, 2, 3] == [1, 2, 3]: ", [1, 2, 3] == [1, 2, 3]) # True - same type, elements are same across each index in both 
print("[1, 3, 2] == [1, 2, 3]: ", [1, 3, 2] == [1, 2, 3]) # False - elements from both lists are different for index 1 and 2

print()
print()

# 'is' does not perform type conversions to compare the two operands. 
# REMEMBER: 'is' checks if the location in memory where the operand values are stored is the same
# the 'is' operator is best suited for check equality of literal values of the same type
print("True is True: ", True is True) # True - boolean true has the same memory location and value
print("True is 1: ", True is 1) # False - values of different types are not stored in same location
print("'1' is 1: ", '' is 1) # False - values of different types are not stored in same location
print("'1' is '1': ", '1' is '1') # True - same type and same value, hence stored in same memory location
print("[] is 1: ", [] is 1) # False - values of different types are not stored in same location
print("10 is 10.0: ", 10 is 10.0) # False - int and float are not same type and their memory locations are different
print("[] is []: ", [] is []) # False - every time a list is created, it is created in different memory locations 
print("[1, 2, 3] is [1, 2, 3]: ", [1, 2, 3] is [1, 2, 3]) # True - type and values are same
print("[1, 2, 3] is [1, 3, 2]: ", [1, 2, 3] is [1, 3, 2]) # True - type and values are same
# REMEMBER: literals like string and numbers with the same value will be created once and referenced when
# used/assigned subsequently. But data structures like list, dictionary and sets are newly created every time
# they are declared/assigned even if the underlying values are same. Hence, their memory locations will be
# different.  
