# Operators are used to perform operations on variables and values


# Python Arithmetic Operators
# ==============================

#%% Addition
2 + 5

#%% Subtraction
2-5

#%% Multiplication
2*5

#%% Divsion (float number)
5/2

#%% Floor division (just the integer part )
5//2

#%% Modulus (To get the remainder)
5 % 2

#%% The Python ** operator is used to raise a number in Python to the power of an exponent
2**5
# it is equal to 2*2*2*2*2

#%% Find square root : numer ** 0.5

mylist = [
1 ** 0.5,
2 ** 0.5,
36 ** 0.5,
81 ** 0.5]

for item in mylist:
    print(item)

#%% get absolute value of a number
(5)

#%%
(-5)
abs(-5)

#%%
(5-5)

# %%
pow(2, 5)
# it is equal to 2*2*2*2*2 or 2**5

#%%
pow(2, 5, 5 ) # 3rd parameter can used to do this : pow(2, 5)%5

#%% use pow() if you need an integer outcome and math.pow() for a floating-point result.
import math
math.pow(2, 5)


# %%
