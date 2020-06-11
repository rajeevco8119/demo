import numpy as np
from scipy.stats.mstats import gmean, hmean

x = gmean([1, 3, 9])
y = hmean([1, 3, 9])

#Lambda functions
lm1 = lambda a: a + 10
lm2 = lambda a, b: a * b


print(lm1(5))
print(lm2(2,3))

def lm3(n):
    return lambda a: a * n


lm4 = lm3(4)
print(lm4(11))

from functools import reduce

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61, 73]
final_list = list(map(lambda x: x * 2, li))
sum1 = reduce((lambda x, y: x + y), li)

odd_time = reduce((lambda a, b: a ^ b), li)
print(odd_time)

list2 = ["geeks", "geeg", "keek", "practice", "aa"]

# Given a list of strings, find all palindromes
result = list(filter(lambda x: (x == "".join(reversed(x))), list2))


print(result)

# Intersection of 2 arrays in python
def intersection(arr1, arr2):
    result1 = list(filter(lambda x: x in arr1, arr2))
    print(result1)

a1 = [5,6,7,9,8]
a2 = [7,9,3]

print(intersection(a1,a2))
#List anagrams (Counter checks the frequencies of letters)
from collections import Counter

def angram_chck1(arr1, arr2):
    return Counter(arr1) == Counter(arr2)

# nested lambda
square = lambda x: x**2
product = lambda f,n:lambda x:f(x)*n

answer = product(square,2)(10)
print(answer) #200

# Method overloading in Python
class Person:
    def Hello(self,name=None):
        if name is not None:
            print('Hello '+name)
        else:
            print('Hello')

obj = Person()
obj.Hello()
obj.Hello('Rajeev')

class AreaCompute:
    def area(self,x=None,y=None):
        if x!= None and y!= None:
            return x*y
        elif x!= None:
            return x*x
        else:
            return 0

# method Overriding
class Parent:
    def __init__(self):
        self.value = 'Inside Parent'

    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        self.value = 'Inside Child'
    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


# Python overriding in multiple inheritence
# When a class is derived from more than one base class it is called multiple inheritence

class Parent1():
    def show(self):
        print('Inside Parent1')

class Parent2():
    def display(self):
        print('Inside parent2')

class Child(Parent1,Parent2):
    def show(self):
        #Parent1.show(self)  # This line is used to show if the function of Parent is needed to be called
        print('Inside Child')

obj = Child()
obj.show()
obj.display()



# Multilevel Inheritence

class Parent():

    # Parent's show method
    def display(self):
        print("Inside Parent")

    # Inherited or Sub class (Note Parent in bracket)


class Child(Parent):

    # Child's show method
    def show(self):
        print("Inside Child")

    # Inherited or Sub class (Note Child in bracket)


class GrandChild(Child):

    # Child's show method
    def show(self):
        print("Inside GrandChild")

    # Driver code


g = GrandChild()
g.show()
g.display()


class GFG1:
    def __init__(self):
        print('Hey GFG I am initialised(CLASS GFG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:',b)

class GFG2(GFG1):
    def __init__(self):
        print('Hey GFG I am initialised(CLASS GFG2)')
        super.__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:',b)
        super.sub_GFG(b+1)

class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)
if __name__=='__main__':
     obj = GFG3()
     obj.sub_GFG(10)

# Set operations
set1 = {0,2,4,6,8}
set2 = {1,2,3,4,5}

print('Union: ', set1|set2)
print('Intersection',set1 & set2)
print('Difference', set1-set2)
print('Symmetric difference', set1^set2)

# decorators

#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate. In this tutorial, we'll show the reader how they can use decorators in their Python functions.

# In Python, functions are the first class objects, which means that –
#
# Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
# Functions can be defined inside another function and can also be passed as argument to another function.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
#
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
     return 'hello there'

# Nested decorators
print(say_hi())
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())

def decorators_with_arguments(function):
    def wrapper_accepting_arguments(arg1,arg2):
        print('My arguments are: {0},{1}'.format(arg1,arg2))
        function(arg1,arg2)
    return wrapper_accepting_arguments

@decorators_with_arguments
def cities(c1,c2):
    print("Cities I love are {0} and {1}".format(c1, c2))


cities("Nairobi", "Accra")

# class variable vs Static Variable
class CSStudents:
    stream = 'cse'  # class variable
    def __init__(self, name, roll):
        self.name = name  # instance variable
        self.roll = roll  # instance variable

a = CSStudents('Geek',1)
b = CSStudents('Nerd',2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)    # prints "Geek"
print(b.name)    # prints "Nerd"
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"

class sample(object):
    objectNo = 0
    def __init__(self, name1):
        self.name = name1
        sample.objectNo = sample.objectNo + 1 #static variable increment
        self.objNumber = sample.objectNo

    def myFunc(self):
        print('My name is',self.name,
              "from object", self.objNumber)

    def alterIt(self, newName):
        self.name = newName

    @staticmethod
    def myFunc2():
        print("I am not a bound method !!!")


samp1 = sample('A')
samp1.myFunc()

samp2 = sample('B')
samp2.myFunc()
samp2.alterIt('C')
samp2.myFunc()
samp1.myFunc()
samp1.myFunc2()

# Encapsulation in Python

#Encapsulation describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those type of variables are known as private variable.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc

class Base:
    def __init__(self):
        self._a = 2 # protected variable

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print('Calling protected member of base class:')
        print(self._a)
obj1 = Derived()
obj2 = Base()
print(obj2._a)

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__a)
    # Driver code


obj1 = Base()
print(obj1.a)

# Abstract method

from abc import ABC,abstractmethod
class Polygon(ABC):
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")
class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")
class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 4 sides")

R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()


# Getter and Setter for the user defined types (list of objects)
class Books:
    def setBooks(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def getBooks(self):
        return str(self.id)+ ' '+ self.name + ' ' + str(self.price)

c = [{'id':1,'name':'Raj','price':224},
    {'id':2,'name':'Anuj','price':1220},
     {'id': 3, 'name': 'Akshat', 'price': 1224}, ]

books = dict()
for i in range(0,3):
    books[i] = Books()
    books[i].setBooks(c[i]['id'],c[i]['name'],c[i]['price'])

for i in range(0,3):
    print(books[i].getBooks())

# Why we don't use getter and setter in python? Because python gives the encapsulation prpperty in its own way using __init__ method (But for private variables we need getter and setter methods to access the data)

# Property method is used if we want to have some conditions to set the value of an attribute in the SampleClass.
class sampleClass1:
    def __init__(self,a ):
        self.set_a(a)

    def get_a(self):
        return self.__a

    def set_a(self,a):
        if a>0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2
obj = sampleClass1(16)
print(obj.get_a())

# Same implementation using the property class
class Property:
    def __init__(self, var):
        self.a = var

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self,var):
        if var>0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

obj = Property(23)
print(obj.a)
