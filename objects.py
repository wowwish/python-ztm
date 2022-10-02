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
class User: # PARENT CLASS / BASE CLASS
    # __init__ method (constructor) is missing because we don't want to assign any attribute/variable to the
    # class User
    def sign_in(self):
        print("Logged In!")

    def attack(self): # super-class attack() method
        print('do nothing!')


class Wizard(User): # Wizard inherits 'sign_in' from User - CHILD CLASS / SUB CLASS
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self): # This definition of attack() will override the definition of attack() in the 'User' parent class
        User.attack(self) # However, we can still call the parent class method within this class
        print(f"attacking with power of {self.power}")

class Archer(User): # Archer inherits 'sign_in' from User - CHILD CLASS / SUB CLASS
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows 
    def attack(self): # This definition of attack() will override the definition in the 'User' super-class / parent class
        # User.attack(self) # However, we can still call the parent class method within this class
        print(f"attacking with arrows: arrows left - {self.num_arrows}")

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
# both wizard1 and archer1 will have a common sign_in() method an a unique implementation of the attack() method
print("wizard1 : ", wizard1)
print("archer1 : ", archer1)
# Power of Inheritance (and also Polymorphism):
wizard1.attack()
archer1.attack()
wizard1.sign_in()
archer1.sign_in()


print()
print()
# isinstance() is a built-in function in python to check if an object is the instance of a class
print("isinstance(wizard1, Wizard) : ", isinstance(wizard1, Wizard))
print("isinstance(wizard1, Archer) : ", isinstance(wizard1, Archer))
print("isinstance(wizard1, User) : ", isinstance(wizard1, User)) # True, wizard1 is an instance of its parent class
# Check if one Class is the child / sub class of another Class
print("issubclass(Wizard, User) : ", issubclass(Wizard, User)) # True

# EVERY OBJECT IN PYTHON INHERITS FROM ITS BUILT-IN BASE CLASS CALLED 'object'
# THIS 'object' CLASS PROVIDES A SET OF UNIVERSAL DUNDER METHODS THAT EVERY PYTHON PBJECT WILL HAVE.
print("isinstance(wizard1, object) : ", isinstance(wizard1, object)) 

# Hence, the 'wizard1' object inherits from 'object', 'User' and 'Wizard'.


#  4. POLYMORPHISM: Two classes can have the same method name, but their methods can perform different actions/output.
#   A good example for this are the 'wizard1.attack()' and 'archer1.attack()' methods.  


# Examples showing how same method of two different objects performs different actions or provides different output
# The same method can be customized according to our needs in two different Classes.
def player_attack(character):
    character.attack()

print()
print()
print("player_attack(wizard1) : ", player_attack(wizard1))
print("player_attack(archer1) : ", player_attack(archer1))

for char in [wizard1, archer1]:
    char.attack()


print()
print()
print()


# THE KEYWORD 'super' 
# CHILD CLASS CONSTRUCTORS, (AS WELL AS METHODS AND ATTRIBUTES OF SAME NAME) HAVE PRECEDENCE OVER THE PARENT CLASS.
# We can access the Parent Class constructor (as well as methods and attributes) using the 'super' keyword which
# refers to the Parent Class when used inside the Child Class

# Parent class with Constructor
class User2:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in!')

# Child class with constructor
class Wizard2(User2):
    def __init__(self, name, power, email):
        # Calling the Parent Class constructor directly and passing its corresponding argument
        # User.__init__(self, email) # one way of using Parent Class members
        super().__init__(email) # Using the 'super' keyword to access Parent Class members
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

wizard2 = Wizard2('Merlin', 60, 'merlin@wizardmail.com') # Object Creation
wizard2.attack() # object 'wizard2' has the attack() method from the child class
# print("wizard2.email : ", wizard2.email) # ERROR! - Object 'wizard2' does not have the 'email' attribute because
# it was created using the child class (Wizard2) constructor. This constructor does not require an 'email' argument
# and this argument was not provided during creation of object 'wizard2'



print()
print()
# INTROSPECTION - Determine the type of an Object during Code Runtime

print("dir(wizard2) : ", dir(wizard2))

print()
print()

# DUNDER METHODS / SPECIAL METHODS - They are special methods in-built in python for every object that are not to be touched
# Dunder Method allow Classes to IMPLEMENT OPERATIONS that are INVOKED THROUGH SPECIAL SYNTAX like list slicing 
# and arithmetic operations etc. by performing OPERATOR OVERLOADING. Setting a dunder method to 'None' means that
# object/Class corresponding operation is not available for that Object/Class. Setting '__iter__' to 'None' for
# example, means that the object is not iterable. 
# Another example is the __str__() Dunder method that is used toconvert an object to its string representation.
# len() uses the __len__() dunder method to get the length of an object

class Toy():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
    
action_figure = Toy('Red', 0)
print("\n\nBEFORE OVERLOADING __str__()")
print("action_figure.__str__() : ", action_figure.__str__())
print("str(action_figure) : ", str(action_figure))
# ERRORS because __len__() is not available for user-defined classes like 'Toy' by default
# print("action_figure.__len__() : ", action_figure.__len__())
# print("len(action_figure) : ", len(action_figure))


class Toy2():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            'name': 'Dio',
            'has_pets': False
        }
    # Operator Overloading on a dunder method __str()__ which is used to convert an object to its string representation
    def __str__(self):
        return f'{self.colour}'
    # Declaring additional dunder methods
    def __len__(self):
        return 0
    # THE DESTRUCTOR METHOD
    # BAD PRACTICE TO OVERRIDE THE __del__(). THIS METHOD WILL BE CALLED WHEN AN OBJECT IS ABOUT TO BE DELETED/DESTROYED
    # If a base class has a __del__() method, the derived class’s __del__() method, if any, must explicitly 
    # call it to ensure proper deletion of the base class part of the instance.
    # The __del__() method is called whenever the object is about to be deleted, including when the Program ends.
    def __del__(self):  # BAD PRACTICE - This dunder method can be used to perform pre-deletion actions
        print('deleted') # Will be printed when the Code run ends
    def __call__(self): # This dunder method is invoked when the object/instance is called as a function
        return 'yes?'
    def __getitem__(self, i): # Takes an index and returns the element at the index
        return self.my_dict[i]


print("\n\nAFTER OVERLOADING __str__() and adding __len__(), __del__()")
action_figure2 = Toy2('Blue', 1)
print("action_figure2.__len__() : ", action_figure2.__len__())
print("len(action_figure2) : ", len(action_figure2))
# Note: 'del x' doesn’t directly call 'x.__del__()' — the former decrements the reference count for 'x' by one, 
# and the latter is only called when x’s reference count reaches zero. 
print(action_figure2()) # 'action_figure2()' Invokes the __call__() method declared in its class Toy2.
print("action_figure2['name'] : ", action_figure2['name']) # Calls the __getitem__() method setup in parent class Toy2

