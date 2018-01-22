# Programming with python


# Python is dynamically typed language
# Dynamically typed programming languages do type
# checking at run-time as opposed to Compile-time


# I/O operations


#  Hello World
# "end" is used to describe de-limiter
# default delimiter is "\n" or newline

print("Hello",end=" ")
print("World",end="!! \n ")
print(" Welcome to Python ", end="\n")
print("We will move very fast")

# String Concatenation in variable (link together in chain )
sentence = "Yash" + " is " + " a " + " boy "
print(sentence,end="\n")
# Concatenation in print function is done by comma ","

print("His favourite number is ", 0)
# Input operations

# text = input("Please enter the value of text")
# print(text)

# proof of dynamically typed
# we don't have to worry about the data type of the variable
# while writing the code, in python everything is
# object type which is converted to other data types on the run time

# float
x = 2.1
print(x)

# integer
x = 2
print(x)

# string
x = "Yash"
print(x)

# boolean
x = True
print(x)

# Arrays : data stored at contiguous memory location
# where elements can be accessed if address of 0th index
# is known,
# what does it mean if I write arr[3]?
# arr[0] is known
# arr[3] = value at (address_of(arr[0]) + 3 * sizeof(each_data_type))

# Concept of pointer arithmetic is not available in python
# you can't call any variable by its's address
# like we used to do in C/C++
#
# int *p = 1001; // p can stores address of integer
# *p = *p + 2; is not allowed in python

# So, we don't have to worry about pointer arithmetic and garbage collection
# is also automatic


# Homogeneous Arrays : collections of similar data types stored in
# contiguous memory location, that's why it is possible
# to use index
arr = [1, 2, 3, 4, 5]

# you can directly print the whole array using print function
print(arr)
# print with index, index starts with zero, max index will be size - 1
print(arr[2])
# get the size of an array - using len(arr) function
print("The size of array is ",len(arr))

# Heterogeneous Array : collection of non-similar data types
#  Implemented using Linked Lists(class)

arr2 = ["Hello", 1, True]
print(arr2)


# Array initialization

# 1D Array
arr3 = [5, 6, 7, 8, 9]
print(arr3)

arr4 = [0]*6
print(arr4)

# 2D Array

mat1 = [[1, 2, 3], [4, 5, 6]]
print(mat1)

mat2 = []

for i in range(4):
    temp = [-3]*6
    mat2.append(temp)

print(mat2)


# common methods in arrays
# append : add
# pop : remove, if not defined argument,
#       last elements will be popped out
#       by default otherwise you can define index : arr.pop(index)

arr5 = [1, 2, 3, 4, 5]
print(arr5)
arr5.pop()
print(arr5)
arr5.pop(1)
print(arr5)

# Conditional statements :

# if <-> if
# elif <-> else if
# else <-> else

val = 3

if val == 1:
    print("One")
elif val == 2:
    print("Two")
elif val == 3:
    print("Three")
else:
    print("Enter valid number")

# switch case is not allowed or does not exist

# loops

# for loop

# start value of i = 1
# i < 11, means last iteration value(11) is not included
#  increment by 2 , i += 2

# loop in increment
for i in range(1, 11, 2):
    print(i, end=", ")

print("")
# loop in decrement ,
# i > 3, means last iteration value(3) is not included
# decrement by 1 , i -= 1

for i in range(10, 3, -1):
    print(i, end=", ")

# Shorthands are similar

val = 6
print(val)
# val = val + 6
val += 6
print(val)
# val = val - 4
val += 4
print(val)
# val = val * 2
val *= 2
print(val)
# val = val / 3
val /= 3
print(val)
# val = val % 2
val %= 2
print(val)

# while loop is also similar
counter = 0

while counter < 3:
    print(counter)
    counter += 1

# Fundamentally there are two class of data types

# Primitive (means earliest in evolution): built in the language
# Derived (evolved): derived from the combination of existing primitive data type

# Derived data types can be implemented as a class

# Class in python

# Access Specifications (public, private, protected
# Student class inheriting the object class


class Student(object):
    # sec = A, is called default argument
    # even without defining it you can
    # still create the object
    def __init__(self, name, roll, sec="A"):
        # member variables : variables of class

        # public : anyone can access the information stored inside it
        self.name = name
        self.roll = roll
        self.section = sec

        # protected : defined by single underscore,
        # When you want to restrict the access of
        # the given variable to children of this class
        # and in the same package
        # We will discuss it later

        self._marks = 33

        # private : defined by double underscore
        # When you want to restrict it's usage to
        # this class only

        self.__password = "top secret"

        self.__isPassed = False

    # Member functions : functions of class

    # get_name - getter function

    def get_name(self):
        return self.name

    # set_name - setter function

    def set_name(self, Name):
        self.name = Name

    def get_marks(self):
        return self._marks

    def set_marks(self, Marks):
        self._marks = Marks

    def get_pass(self):
        return self.__password

    def set_pass(self, password):
        self.__password = password

    def isfailed(self,key="111"):
        print("Papa : Pass hua ya nahi ? ")
        text = input("Me : Ek shart p bataunga,\n Papa : nahi maarunga,\n Me: ")

        if text == "batata hu":
            if self.__isPassed == True:
                print("pass ho gaya")
            else:
                print("fail ho gaya")
        else:
            print("kbhi nahi pata chalega")


# Initializing the object
stud1 = Student(" Yash ", 1)
print(stud1.name)
# print(stud1.__password) # unable to access directly, you may find error
# so we have to use the concept of getter and setter
# means private variables can only be accessed by member functions only
print(stud1.get_pass())

# protected member : _marks accessed in the same package but can't be directly
# in another package without member functions (getter, setter)
print("Yash scored ", stud1._marks, " out of 100 in his exam")

# stud1.isfailed()
# print(stud1.__isPassed) , # again you can't access members outside the class directly

# Inheritance (biological term) : as name suggests we are going to inherit the features

print("\nInheritance\n")
print("Single Inheritance : Dog inherit feature of Animal class\n")


# Single inheritance
class Animal:
    # every class inherit object class even if it is not defined
    def eat(self):
        print('Eating...')


class Dog(Animal):
   def bark(self):
        print('Barking...')


d = Dog()
d.eat()
d.bark()

# Multilevel inheritance
print("Multilevel Inheritance : Baby Dog inherit feature of Dog class\n")
print("Dog inherit feature of Animal class, ultimately Baby dog inherit features ")
print("of both classes Animal and Dog \n")


class BabyDog(Dog):
    def weep(self):
        print('Weeping...')


bd = BabyDog()
bd.eat()
bd.bark()
bd.weep()


# Multiple inheritance
class First(object):
    def first(self):
        print("first")


class Second(object):
    # function overriding
    def first(self):
        print("first, Override the first method of class First")
    def second(self):
        print("second")


class Third(Second, First):
    def third(self):
        print("I am third and inheriting ")

        self.second()
        print(" then ",end=" ")
        self.first()


class ThirdChanged(First, Second):
    def third(self):
        print("I am third and inheriting ")
        self.first()
        print(" then ", end=" ")
        self.second()


t = Third()
t.third()
t2 = ThirdChanged()
t2.third()

# function overloading : not allowed in python
# simply we just change parameters in function
# fun(int x) fun(float x) fun(int x, int y) all can exist
# with same name in C++
# Diamond problem in Multiple inheritance
#         A foo
# B(A)             C(A)
#       D(B,C)
# we don't know foo is coming from which path
# but in python the class declared in argument
# first will be given higher preference
# D(B, C) -> foo will come from B
# D(C, B) -> foo will come from C


class A:
    def foo1(self):
        print("foo from A")
        return 1


class B(A):

    def foo(self):
        x = self.foo1()

        print("foo from B", x)
        return x + 1


class C(A):
    def foo(self):
        x = self.foo1()
        print("foo from C", x)
        return x + 2

# C has given higher preference as we defined first in argument list


class D(B, C):
    def foo2(self):
        # value of x is modified by changing the order
        # this is diamond problem,
        # we have no clue how our data is modified in languages like java
        # that's why they don't support inheritance
        # but in python we resolve it by defining preference
        # if D(B, C) , x will be modified by B using foo method
        # if D(C, B) , x will be modified by C using foo method
        
        x = self.foo()
        
        print("foo from D", x)


d = D()
d.foo2()


