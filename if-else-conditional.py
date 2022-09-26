# Conditional statements alter the flow of the program
# The python interpreter runs code line by line, but using conditional statements like if, for etc. we 
# can make it run specific lines multiple times or skip specific lines of code

# is_old  = True
is_old = False
is_licensed = True

# The if statement runs all the indented statements below it only when the condition supplied to it evaluates to 
# 'True'. In this case, 'is_old' is 'True', so the interpreter executes the indented print statement under the if
# statement. Note the semi-colon (':') next to the if <condition> statement which indicates it is a conditional.
if is_old:
    print('you are old enough to drive!')
elif is_licensed: # else if - you can have multiple elif conditionals and corresponding code block to run
    print('you can drive now!')
else: # The 'else' block only runs when the 'if' and 'elif'code blocks condition ('is_old' and 'is_licensed') 
      # evaluate to false
    print('you are not of age!!')
print('okok') # Completely new line, not part of the if code block or the else code block
# due to lack of indentation. This statement will print irrespective of the if condition evaluating 
# to 'True' or 'False' and irrespective of the 'else' code block


# The condition to the 'if' statement can itself be an expression that needs to be evaluated ... like 
# is_old and is_licensed
if is_old and is_licensed:
    print('you are old enough and licensed to drive!')
else:
    print('you are not allowed to drive!!')


# NOTE: the standard indentation is four spaces in python


# Truthy and Falsy - Truthy value evaluates to True when converted to boolean. Falsy values evaluate to false.

is_old = 'hello' # python interpreter implicitly converts this to 'True' (boolean) when used as an if condition
is_licensed = 5  # python interpreter implicitly converts this to 'True' (boolean) when used as an if condition
if is_old and is_licensed:
    print("Inside if block!")
    print("is_old: ", bool(is_old), "is_licensed: ", bool(is_licensed))
print("Falsy values: ", "bool('') is", bool(''), "and bool(0) is", bool(0), "and bool(None) is", bool(None))

"""
We use "truthy" and "falsy" to differentiate from the bool values True and False. A "truthy" value will satisfy 
the check performed by if or while statements. As explained in the documentation, all values are considered 
"truthy" except for the following, which are "falsy":

    None
    False
    Numbers that are numerically equal to zero, including:
        0
        0.0
        0j
        decimal.Decimal(0)
        fraction.Fraction(0, 1)
    Empty sequences and collections, including:
        [] - an empty list
        {} - an empty dict
        () - an empty tuple
        set() - an empty set
        '' - an empty str
        b'' - an empty bytes
        bytearray(b'') - an empty bytearray
        memoryview(b'') - an empty memoryview
        an empty range, like range(0)
    objects for which
        obj.__bool__() returns False
        obj.__len__() returns 0, given that obj.__bool__ is undefined

"""

password = '123'
username = 'Dio Brando'

# easy way to check if a user entered something in for username and password
if username and password:
    print('LOGGED IN!')