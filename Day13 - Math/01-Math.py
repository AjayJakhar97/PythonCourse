'''
Python Math
=============

Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
'''

# Built-in Math Functions
#%% The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#%% The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)

#%% The pow(x, y) function returns the value of x to the power of y (xy).
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)

# The Math Module
# ==================
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:

#%% The math.sqrt() method for example, returns the square root of a number:
import math
x = math.sqrt(64)

print(x)
#%% The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
#%% The math.pi constant, returns the value of PI (3.14...):

import math

x = math.pi
print(x)

# %% Write you own abs function

def myAbs(myNumber):
    if myNumber < 0:
        return -myNumber
    else:
        return myNumber

print(myAbs(0))
print(myAbs(-1))
print(myAbs(1))
