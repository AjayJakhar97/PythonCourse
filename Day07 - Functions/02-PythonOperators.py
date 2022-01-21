# Python Arithmetic Operators
#%% Addition
import math
2+5

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

#%%
#%% The Python ** operator is used to raise a number in Python to the power of an exponent
2**5

#%% get absolute value of a number
(5)

#%%
(-5)
abs(-5)
#%%
(5-5)

# %%
pow(2, 5)

# %%
math.pow(2, 5)

# use pow() if you need an integer outcome and math.pow() for a floating-point result.

# %% Task01 - print list of numbers raised to the power 3
# Some random values
values = [2, 1, 0, 5, 12]

# Raise each number to the power 3
exponents = []
for value in values:
    exponents.append(pow(value, 3))
# exponents = [pow(value, 3) for value in values]

# Output both lists
print("Original list:\n", values)
print("Raised to the power 3:\n", exponents)

# %%
