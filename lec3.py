# Working with external libraries in Python

# Installing Library :

# 1. Connect your pc to internet
# 2. Go to command prompt(cmd/terminal) and type : pip install graphics.py
# pip service will automatically find the library and install it 
# on your PC

# Introduction to working of graphics/animation in computer

import graphics as g


width = 1000  # in pixels
height = 500  # in pixels

win = g.GraphWin(' Title ', width, height)

# Drawing lines from
# the existing library functions

x1 = 10
y1 = 20

x2 = 30

# increase y2 above 100 see the significant signal loss

y2 = 300


pt1 = g.Point(x1, y1)
pt2 = g.Point(x2, y2)
line = g.Line(pt1, pt2)
line.draw(win)

# you can import specific class or
# function also from imported package
# given below we are importing sleep
# function from time package

from time import sleep
sleep(3)  # argument of sleep function is Time in seconds.

# Drawing line using intuition point by point
slope = float((y2 - y1)/(x2 - x1))

# plotting the line as y = f(x)
# which means we plot x and compute y

for x in range(x1, x2):

    # Computing y

    y = slope * x
    pt = g.Point(x, y)
    pt.draw(win)

sleep(3)  # Time in seconds.

# Using our intuition we find loss in signal
# we need some technique to fix this loss
# The technique we will use is called
# Digital differential Analyser (DDA) algorithm

# We will be discussing the concept of DDA algorithm
# which will solve the existing problem only

# In DDA algorithm, we take the derivative(slope) of the function
# for our case : (10, 20) -> (30, 100)

# slope = (y2-y1)/(x2-x1) = (100-20)/(30-10) = 80/20 = 4/1
# for interval of 1 in x axis there exist 4 values of y

# we must move value of y, four times faster than x
# or there exists four times more values of y than x
# in the given line.

# DDA suggests that the faster moving value should be plotted
# and slower should be computed
# So, we are plotting y and computing x

sleep(3)  # Time in seconds

for y in range(y1, y2):
    # Computing x

    x = (1/slope) * y
    # round off x mathematically to it's nearest integer value
    # eg. 5.75 = 6, 5.4 = 5.5 = 6, 5.99 = 6, 5.1 = 5
    x = round(x)
    pt = g.Point(x, y)
    pt.draw(win)

# still there is a problem with round off, round off
# function require computation as we need to convert
# float to integer which is expensive operation which ultimately
# slow the line draw .
# if we are making an animation using DDA then we will see significant
# slow processing. This problem is known as floating point problem

# Jack Elton Bresenham, a computer scientist in US solve this problem with
# unique approach in which he introduce the concept of decision parameters


win.getMouse()
win.close()

