#%% Lambda functions
# Normally we define a function using the def keyword somewhere in the code and call it whenever we need to use it.

def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

#%%
'''
Now instead of defining the function somewhere and calling it, we can use python's lambda functions, which are inline functions defined at the same place we use it. So we don't need to declare a function somewhere and revisit the code just for a single time use.

They don't need to have a name, so they also called anonymous functions. We define a lambda function using the keyword lambda

Syntax : lambda arguments : expression
your_function_name = lambda inputs : output

A lambda function can take any number of arguments, but can only have one expression.
The expression is executed and the result is returned:
'''
#%% So the above sum example using lambda function would be,

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

# Here we are assigning the lambda function to the variable sum, and upon giving the arguments i.e. a and b, it works like a normal function.

#%% Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# %% Lambda functions can take any number of arguments:
# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

# %% Add the arguments a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#%% Exercise : Write a program using lambda functions to check if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))

# %% Why Use Lambda Functions?
'''
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
'''
def myfunc(n):
  return lambda a : a * n

#%% Use that function definition to make a function that always doubles the number you send in:

mydoubler = myfunc(2)
print(mydoubler(11))

#%% or triple that number

mytripler  = myfunc(3)
print(mytripler(11))

