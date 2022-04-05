#%% In Python, variables are created when you assign a value to it:
x = 5                 # Data Type : int
y = "Hello, World!"   # Data Type : str

print(x)
print(f'{x}')
print(f'{x=}')
y = "Hello, World!"
print(f'{y=}')

#%% A variable is created the moment you first assign a value to it. below won't work
# z

#%% Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Duck"  # x is now of type str
print(x)

#%% Variable names are case-sensitive.
a = 4
A = "Duck"
#A will not overwrite a

#%% Assign Multiple values
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#%% And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)


#%% If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]

# x = fruit[0]
# y = fruit[1]
# z = fruit[2]

x, y, z = fruits
print(x)
print(y)
print(z)

#%% Store input to a variable and then use it
day = input("What day is today?")

print(day + "! I like "+day)
print(day * 2)
print("Happy " + day)
# print(day-1)

#%%
age = 25
print('my age is ',age)
print('my age is ' + age)

# Variable Names
# ==========================
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

#%% Legal variable names:

myvar = "Earth"
my_var = "Earth"
_my_var = "Earth"
myVar = "Earth"
MYVAR = "Earth"
myvar2 = "Earth"

#%% Illegal variable names:

2myvar = "Earth"
my-var = "Earth"
my var = "Earth"

#%% 3 famous cases used are below
# Camel Case
myVariableName = "Bill"

# Pascal Case
MyVariableName = "Bill"

# Snake Case
my_variable_name = "Bill"

#%%
"""
Caution: Notice that large numbers never include commas. Compare these two examples. In the second, Python thinks that it is printing 3 numbers not 1.
"""
print(12345678)
print(12, 345, 678)

#%%
print(1000000000 + 1)

print(000000000000000000000000000000000000000000) 
# print(000000000000000000000000000000000000000001) 
print(1,000,000,000 + 1)


print(1_000_000_000 + 1)

#%%
"""
Another caution. The following are Python keywords. They have special meaning and shouldn't be used as variable names:

and         del     from    not     while
as          elif    global  or      with
assert      else    if      pass    yield
break       except  import  print
class       exec    in      raise
continue    finally is      return
def         for     lambda  try

You'll just get a syntax error:
"""
#%% You'll just get a syntax error, if you try to use them. Check below examples

# except = 5
# if = 'hello'
# in = 'hello'

#%%
"""
Note: for readability, if you feel that you need to use one of these as a variable, you could use an underscore after it. For example, and_, class_, etc.
That makes it different from the Python keyword.
"""
#%%
newEngland = ["Maine", "New Hampshire", "Vermont", "Rhodes Island", "Massachusetts", "Connecticut"]


def for_state(state_list):
    for state in state_list:
        print(state)

# Output Variables
#%% To combine both text and a variable, Python uses the + character:
x = "amazing"
print("Weather is " + x)

#%% You can also use the + character to add a variable to another variable:
x = "Weather is "
y = "amazing"

z = x + y
print(z)

#%% For numbers, the + character works as a mathematical operator
x = 5
y = 10

print(x + y)

#%% If you try to combine a string and a number, Python will give you an error:
x = 5
y = "Bill"
print(x + y)

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#%% Global variables can be used by everyone, both inside of functions and outside.

x = "amazing"

def myfunc():
  print("Weather is " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
#%% The global variable with the same name will remain as it was, global and with the original value.
x = "amazing"

def myfunc():
  x = "fantastic"
  print("Weather is " + x)

myfunc()

print("Weather is " + x)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# Also, use the global keyword if you want to change a global variable inside a function.
#%% To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "amazing"

def myfunc():
  global x
  x = "fantastic"
  print("Weather is " + x)

myfunc()

print("Weather is " + x)


# %% Example 1: Create a Global Variable
x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)
# %% What if you want to change the value of x inside a function?
x = "global"

def foo():
    x = "local"  # comment this
    x = x * 2
    print(x)

foo()
print(x)

# %% Example 2: Accessing local variable outside the scope
def foo():
    Achintya = "local"

foo()
print(Achintya)


#%% Example 3: Create a Local Variable
def foo():
    y = "local"
    print(y)

foo()

#%% Example 4: Using Global and Local variables in the same code
x = "global "

def foo():
    global x   # If you comment this, you will get an error
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()
print(x)

# %% Example 5: Global variable and Local variable with same name
x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)

# Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
# Let's see an example of how a nonlocal variable is used in Python.

# %% Example 6: Create a nonlocal variable
x = "Global"

def outer():
    x = "local"

    def inner():
        nonlocal x # comment this to see the difference
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()
print("Main:", x) 

# %%
