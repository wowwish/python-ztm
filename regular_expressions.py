# reeeeeeeee
import re # built-in python module for regular-expressions

string = 'search this inside of this text please!'

print('search' in string)

# re.search(<pattern>, string) returns an object if there was a pattern match and 'None' otherwise
a = re.search('this', string)

print("a.start() : ", a.start()) # start of the first match
print("a.end() : ", a.end()) # end of the first match
print("a.group() : ", a.group()) # the matched parts of the string as a tuple

print()
print()

# We can also create a pattern that we want to check for useing re.compile()
pattern = re.compile('this') # now this compiled pattern can be used to search

a = pattern.search(string)
b = pattern.findall(string) # finds all the instances of the match
c = pattern.fullmatch(string) # The full 'string' should match with the pattern for this to be a match
print("pattern = re.compile('this')")
print("pattern.search(string) : ", a)
print("pattern.findall(string) : ", b)
print("pattern.fullmatch(string) : ", c) # will be none because the pattern is not the full 'string'
print("re.search('search this inside of this text please!', string) : ", re.search('search this inside of this text please!', string))
# The below code will again return none because of an extra '!' after the second occurrence of 'this'
print("re.search('search this inside of this! text please!', string) : ", re.search('search this inside of this! text please!', string))
# The line of code below produces a match object because re.match() will return a match object if the 
# string starts with the given pattern
print("re.match('search this inside', string) : ", re.match('search this inside', string))
print("re.match('this inside of', string) : ", re.match('this inside of', string)) # returns None (pattern does not match
# to the start of the string)


print()
print()

pattern2 = re.compile(r"([a-zA-Z]).([a])") # here 'r' stands for raw string as '\'s in python strings have special
# meaning - but not in raw strings
print("re.compile(r'([a-zA-Z]).([a])') : ", pattern2)
print("pattern2.search(string).group(0) : ", pattern2.search(string).group(0)) # The entire match
# Match within the first parantheses pair within the pattern
print("pattern2.search(string).group(1) : ", pattern2.search(string).group(1)) 
# Match within the second patantheses pair within the pattern
print("pattern2.search(string).group(2) : ", pattern2.search(string).group(2)) 

print()
print()

# pattern for checking email addressed
pattern3 = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
print("re.compile(r'^[a-zA-Z0-9_-.+]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9-.]+$') : ", pattern3)
email = 'admin@udemy.com'
print("pattern3.search(email) : ", pattern3.search(email))

print()
print()

# Regex for Password Validation
# password must be atleast 8 characters long
# password can contain any letters, any numbers and only these symbols: $%#@
# password has to end with a digit

passwd = re.compile(r'^[a-zA-Z0-9$%#@]{7,}\d$')
print("re.compile(r'^[a-zA-Z0-9$%#@]{7,}\d$') : ", passwd)
print("passwd.fullmatch('hdjk') : ", passwd.fullmatch('hdjk'))
print("passwd.fullmatch('a2%flojjas@4') : ", passwd.fullmatch('a2%flojjas@4'))

# A FUN REGEX TUTORIAL: https://regexone.com/