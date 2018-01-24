
# Advanced Data Types in Python

# Dictionary or Hash

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]

# converting two arrays to dict
country_specialities = zip(countries, dishes)
country_specialities = dict(country_specialities)

print(country_specialities)


key_Hash = dict()

for i in range(5):
    key_Hash[i] = chr(65 + i)

print(key_Hash.items())
print(key_Hash.keys())
print(key_Hash.values())

print(key_Hash[0], end=" ")
print(key_Hash.get(1))

# delete the last item
key_Hash.popitem()

print(key_Hash.items())

# Lambda function
# lambda argument1,argument2 .. argument n : return statement

def sq(x):
    return x**2
square = lambda x: x**2

def plus(x,y):
    return x + y
add = lambda x, y: x + y

def maxim(x,y):
    if x > y:
        return x
    else:
        return y
    
mx = lambda x, y: x if x > y else y

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
fact = lambda n: 1 if n == 1 else n * fact(n-1)

print(square(2),", ",sq(2))
print(fact(5),", ",factorial(5))
print(add(2, 3),", ",plus(2, 3))
print(mx(2, 3),", ",maxim(2, 3))

# lambda functions and lists

arr = [i for i in range(5)]

# map function means modify
# each element of the list by the
# using lambda function 
# first arg: lambda function, second arg: arr


sqaure = lambda x: x**2
new_list = list(map(sqaure, arr))
print(new_list)

# filter function means filter
# each element of the list by the
# according lambda function
# first arg: lambda function, second arg: arr


is_even = lambda x: x % 2 == 0
new_list = list(filter(is_even, arr))
print(new_list)


# User Defined Abstract Data Types (Data Structures)
# Linked List : Linked structure 


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.start = None

    def insert(self, val):
        if self.start is None:
            self.start = Node(val)
        else:
            iterator = self.start

            # Reach to the end of the list

            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = Node(val)

    def pop(self):
        if self.start is not None:
            iterator = self.start

            # Reach to the end of the list

            while iterator.next.next is not None:
                iterator = iterator.next

            temp = iterator.next
            iterator.next = None
            del temp

    def search_node(self, key):
        if self.start is not None:

            iterator = self.start

            # Reach to the end of the list

            while iterator.next is not None:
                if iterator.data == key:
                    break

                iterator = iterator.next

            return iterator

    def print_nodes(self):
        if self.start is not None:

            iterator = self.start
            print("", end="\n")

            # Reach to the end of the list

            while iterator is not None:
                print(iterator.data, end="->")
                iterator = iterator.next


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.print_nodes()
LL.pop()
LL.print_nodes()
LL.pop()
LL.print_nodes()
