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
# while writing the code

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

# Two types of data types

# Primitive (means earliest in evolution): built in the language
# Derived (evolved): derived from the combination of existing primitive data type

# Derived data types can be implemented as a class

# Class in python

# Access Specifications (public, private, protected


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

stud1.isfailed()
# print(stud1.__isPassed) , # again you can't access members outside the class directly
