#%% You can make a function return the value that you can use later with "return" keyword
from MyFunctions import *


def myNumberFive():
    return 5

#%% Calculate Total Bill with 5% tip
TotalExpense = 100
tip = TotalExpense * myNumberFive()/100
print("Total Bill with tip of", tip, "is = ", TotalExpense+tip)

# Task01- Make use of return and print table of 5
for item in range(10):
    print((item+1)*myNumberFive())

#%% method to add two numbers


def AddTwoNumbers(x, y):
    return x+y


# %% import functions from another file
AddTenFunction(5)

# %%
