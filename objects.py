# Object-Oriented Programming
# Everything in Python is an Object - An instance of a Class
# We are able to achieve different actions on these objects using the methods defined in them
# We are able to access certain values of these objects using the attributes defined in them
# OOP in python allows us to create our own data-types with different attributes and methods
# OOP is a paradigm that allows to write highly maintainable, well oranized, memory efficient code.
# OOP allows us to create models of real world as abstract objects in code with associated attributes
# and methods
from types import ClassMethodDescriptorType


print("type(None) : ", type(None))
print("type(True) : ", type(True))
print("type(5) : ", type(5))
print("type(5.5) : ", type(5.5))
print("type('hi')", type('hi'))
print("type([]) : ", type([]))
print("type(()) : ", type(()))
print("type({}) : ", type({}))
print("type('hi'.upper)", type('hi'.upper)) # method
print("'hi'.upper() : ", 'hi'.upper())
print("'hi'.__doc__ : ", 'hi'.__doc__) # attribute

# Create your own Datatype/Class - The blueprint for an object that abstracts away real world phenomena
# classes abstract away the properties of the real world as attributes and the actions of real world as methods
# The code of the class is stored in memory
class BigObject:        # class name as singular noun in camel-case is a standard practice
    # code
    pass
print()
print()
print("type(BigObject) : ", type(BigObject))
print()
print()
# create an object of class BigObject - instanciate the Class BigObject
obj1 = BigObject()
print(type(obj1))

# Memory for data is allocated when the object is created, not when the class is defined
obj2 = BigObject()
obj3 = BigObject()

print()
print()

class PlayerCharacter: # camel-case for class name
    membership = True # Class Attribute - does not change across instances - can be accessed using 'self' like
    # 'self.membership' or using the class name like 'PlayerCharacter.membership'
    def __init__(self, name='anonymous', age=0): # Constructor method - a special type of dunder method
        # The constructor method gets called automatically, everytime an object is instanciated
        # if (self.membership): # Always True
        # if (PlayerCharacter.membership): # Always True, class attributes can be accessed using 'self' or class name
        if (age > 18): # Object is instanciated only when the age parameter is > 18. This way, we can control
            # object instanciation based on parameter conditions
            self.name = name     # 'name' is a required argument of the constructor to instanciate the class
            # 'self' refers to this class 'PlayerCharacter'. by setting 'self.name' to the 'name' argument of the
            # constructor, we are assigning an attribute to the class using the constructor
            self.age = age

    # Other methods of the class
    def run(self):
        print("Run!")
        return 'done!'

    def shout(self):
        print(f'My name is {self.name}') # object attributes can only be accessed using 'self' parameter 
        # inside methods

    # Class Method - are special type of functions called 'decorators'
    @classmethod
    def adding_things(cls, num1, num2): # 'cls' is similar to 'self' (refers to this class), but is specific
        # to class methods. Whenever a class method is invoked, the class itself will be passed as one of the 
        # arguments in the function call. This is captured using the 'cls' parameter.
        return num1 + num2

    @classmethod
    def create_things(cls, num1, num2):
        # we can also use a class method to instanciate that particular class (Create an object)
        return cls('Teddy', num1 + num2)

    @staticmethod
    # The static method works exactly same as a class method except, you do not have access to 'cls'. The
    # class itself will not be passed as an argument in the method call and hence, it is not part of the 
    # parameter list of a static method
    def add(num1, num2): 
        return num1 + num2

player1 = PlayerCharacter('Dio', 120)    # instanciate with required arguments for constructor
player2 = PlayerCharacter('Jotaro', 20)
player3 = PlayerCharacter()

# Note that player1 and player2 objects are created from the same class but are stored at two different
# memory locations
print("player1 : ", player1)
print("player2 : ", player2)
print("player3 : ", player3)
print()
print()
print("player1.name : ", player1.name) # access class attributes - assigned by the constructor
print("player2.age : ", player2.age) # access class attributes - assigned by the constructor
# print("player3.age : ", player3.age) # ERROR! because object was not instanciated - default age is 0 which
# does not satisfy the condition for instanciation in the constructor
print()
print()
print("player2.run():")
print(player2.run())
print("player2.shout():")
player2.shout()
print()
print()

# We can also set object attributes after object creation
# Each object has a different value for its member attributes - member attributes are dynamic
# However, the class attribute remains same across all instance of the class (objects)
player2.attack = "fire!" # attribute specific to 'player2' object
print("player2.attack : ", player2.attack)
print("player1.membership player2.membership : ", player1.membership, player2.membership)
print()
print()

# print the blueprint of the object
# help(player1)

print("player1.adding_things(2, 3) : ", player1.adding_things(2, 3)) # invoking class method 
# class methods can be invoked even without instanciating the class
print("PlayerCharacter.create_things(2, 3) : ", PlayerCharacter.create_things(2, 3))
# static methods can also be invoked without instantiationg the class
print("PlayerCharacter.add(2, 3) : ", PlayerCharacter.add(2, 3))
player4 = PlayerCharacter.create_things(10, 9) # player4 instanciated using class method
print("player4.age : ", player4.age)

# REMEMBER: 
# We use static methods when we don't care about the class state(class attributes). Hence, it does not
# have access to the class attributes. 
# We use a class methods when we want to modify or change the class state(class attributes)

# SUMMARY:
# Instance Methods: The most common method type. Able to access data and properties unique to each instance.
# Static Methods: Cannot access anything else in the class. Totally self-contained code.
# Class Methods: Can access limited methods in the class. Can modify class specific details.


# 4 Pillars of OOP:

#  1. ENCAPSULATION: Binding data (attributes) and functions (methods) that manipulate that data together

#  2. ABSTRACTION: Hiding information about internal workings, giving access to only neccessary information
# abstraction is important because attributes and methods of the object can be modified by anyone if they are given
# access to it. This is where the 'public' and 'private' access specifier keywords of python help.
print()
print()
print("Before modifying publicly accessible object")
print("player1.name : ", player1.name)
print("player1.shout : ", player1.shout)
player1.name = '!!!'
player1.shout = 'BOOOOOOO'
print("After modifying public access object - note the shout() method being changed to a string")
print("player1.name : ", player1.name)
print("player1.shout : ", player1.shout)


# All member variables and methods are PUBLIC by default in python. The examples we saw till now were all PUBLIC
# declarations - you can access and modify the members from within the class or from anywhere outside the class. 

# In python, there are no true private or protected attributes/methods for a class. Python programmers however
# follow a STANDARD PRACTICE of naming protected class members with '_' as the start of the identifier and private
# class members with '__' as the start of the identifier.


print()
print()

# PRIVATE MEMBERS (will throw 'AttributeError' when accessed outside the class they are declared in)
# PRIVATE MEMBERS ALSO INCLUDE DUNDER METHODS AND ATTRIBUTES.
print("PRIVATE MEMBERS")
class PlayerCharacter2:
    def __init__(self, name, age):
        # private members - accessible only from within this class
        self.__name = name
        self.__age = age
    def run(self):
        print("run!")
        self.__speak()
    # private method 
    def __speak(self):
        print(f"my name is {self.__name}, and I am {self.__age} years old")

p1 = PlayerCharacter2('Kakyoin', 17)
# print("p1.__name : ", p1.__name) # AttributeError
# print("p1.__age : ", p1.__age) # AttributeError
# since python performs 'name mangling' (convert private members to '_object._class__variable' naming), the
# private members can still be accessed - BAD PRACTICE
print("p1._PlayerCharacter2__name : ", p1._PlayerCharacter2__name)
print("p1._PlayerCharacter2__age : ", p1._PlayerCharacter2__age)
print("p1._PlayerCharacter2__speak : ", p1._PlayerCharacter2__speak) # accessing private method
p1.run() # accessing normal method of p1 which calls another private method of p1 inside of it
print()
print()
print()

# PROTECTED MEMBERS (accessed by other members within the class and its sub-classes)
print("PROTECTED MEMBERS")

class PlayerCharacter3:
    def __init__(self, name, age):
        # protected attributes 
        self._name = name
        self._age = age
    def run(self):
        print("run!")
        self._speak()
    # protected method
    def _speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")

p2 = PlayerCharacter3("Avdol", 25)
print()
print()
# BAD PRACTICE TO ACCESS PROTECTED / PRIVATE MEMBERS OUTSIDE THE CLASS
print("p2._name : ", p2._name)
print("p2._age : ", p2._age)
print("p2._speak : ", p2._speak)
print(p2._speak())
print()
print()

#  3. INHERITANCE: Allows new objects to take properties from existing objects (one class inherits another class)
class User:
    # __init__ method (constructor) is missing because we don't want to assign any attribute/variable to the
    # class User
    def sign_in(self):
        print("Logged In!")


class Wizard(User): # Wizard inherits 'sign_in' from User
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User): # Archer inherits 'sign_in' from User
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
# both wizard1 and archer1 will have a common sign_in() method an a unique implementation of the attack() method
print("wizard1 : ", wizard1)