name = 'Dio'
age = 55

# String concatenation approach
print('hi ' + name + '. You are ' + str(age) + ' years old')
 
# Shortcut formatted string - f-string feature specific to python 3
print(f'hi {name}. You are {age} years old')

# Proper string formatting that works in both python 2 and python 3
print('hi {}. You are {} years old'.format('Dio', '55'))
print('hi {}. You are {} years old'.format(name, age)) # Here 'age' is implicitly converted to string type
# We can mix around the variable injection into the string like so
print('hi {1}. You are {0} years old'.format(name, age))
# We can also create new variables on the fly and assign them 
print('hi {new_name}. You are {new_age} years old'.format(new_name = 'Sally', new_age = 100))