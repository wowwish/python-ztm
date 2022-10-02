from ast import Pass


print()
print()

class User():
    def sign_in(self):
        print('logged in!')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    def check_arrows(self):
        print(f'{self.arrows} remaining')
    def run(self):
        print('ran really fast!')

# INHERITING FROM MULTIPLE CLASSES
class HybridBorg(Wizard, Archer): # Inherit from Wizard, then from Archer
    # We need to set up a CONSTRUCTOR that handles Inheritance of attributes from both Wizard and Archer
    def __init__(self, name, power, arrows):
        # USING PARENT CLASS CONSTRUCTORS TO BUILD THE CHILD CLASS PROPERLY
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)
        print("super().__init__ : ", super().__init__)
        print("super().check_arrows : ", super().check_arrows)
        print("super().attack : ", super().attack)
        print("super().run : ", super().run)



hb1 = HybridBorg('Borgi', 50, 100)
hb1.sign_in()
hb1.attack()
hb1.check_arrows()


print()
print()
print()


# MRO - Method Resolution Order
# If members are common between the multiple inherited classes, which Class's member is picked, what
# is the precedence followed in such cases ?

class A:
    num = 10

class B(A): # Inherits from A
    pass

class C(A): # Inherits from A and changes the inherited attribute
    num = 1

class D(B, C): # Multiple Inheritance - From B first and then from C
    pass

print("D.mro() : ", D.mro()) # D > B > C > A ? 'object' is the inheritance order/precedence followed by this class
print("D.num : ", D.num) # D.num comes from C
print("D.__str__", D.__str__) # From the in-built base object of python


# MRO IN PYTHON2 FOLLOWS DEPTH-FIRST-LEFT-TO-RIGHT-SEARCH
# MRO IN PYTHON3 FOLLOWS C3 LINEARIZATION APPROACH WHERE:
    # * Children precede their parents
    # * If a class inherits from multiple classes, they are kept in the order specified in the tuple of the base class.

class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A ,Z): pass

print("M.__mro__ : ", M.__mro__) 
# M > B (since B is the first parent class) > A (immediate super-classes precede higher level super-classes) > X > Y > Z > 'object'
# In PYTHON2, this will be M > B > Y > Z > A > X > Z


# There are cases when Python cannot create a MRO
class A:
    def process(self):
        print('A process()')


class B(A):
    def process(self):
        print('B process()')


class C(A, B):
    pass


obj = C()
obj.process()

# The problem comes from the fact that class A is a super class for both C and B. 
# If you construct MRO then it should be like this:

# C -> A -> B -> A

# Then according to the rule (good head) A should NOT be ahead of B as A is super class of B. 
# So new MRO must be like this:

# C -> B -> A 

# But A is also direct super class of C. So, if a method is in both A and B classes then which version 
# should class C call? According to new MRO, the version in B is called first ahead of A and that is not 
# according to inheritance rules (specific to generic) resulting in Python to throw error. 

