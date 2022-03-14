'''
What is a Module?
===================
++ Consider a module to be the same as a code library.
++ A file containing a set of functions you want to include in your application.

'''
#%% Create a Module
# To create a module just save the code you want in a file with the file extension .py: for Example, Save this code in a file named mymodule.py
'''
def greeting(name):
  print("Hello, " + name)
'''
#%% Use a Module
# Now we can use the module we just created, by using the import statement:
# Import the module named mymodule, and call the greeting function:

import mymodule

# When using a function from a module, use the syntax: module_name.function_name.
mymodule.greeting("Jonathan")

# %% Import From Module
# You can choose to import only parts from a module, by using the from keyword.

# from mymodule import *
from mymodule import AddTenFunction

# import mymodule

AddTenFunction(5)

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

#%% Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
'''
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
'''

import mymodule

a = mymodule.person1["age"]
print(a)

#%% Re-naming a Module; You can create an alias when you import a module, by using the as keyword:

import mymodule as mx

a = mx.person1["age"]
print(a)

#%% List all the defined names belonging to the platform module:

x = dir(mx)

for i in x:
    # if "__" not in i:
        print(i)

# %% Find the source code of a function
import inspect

def myAbs(number):
    if number > 0:
        return number
    else:
        return -number


source_myAbs = inspect.getsource(myAbs)
print(source_myAbs)

# it seems to work only for objects defined in a file. Not for those defined in interpreter

#%% Can I call built in function ???
import inspect

source_myAbs = inspect.getsource(abs)
print(source_myAbs)

# %% Find the source code of a built-in function
source_max = inspect.getsource(max)  # max is a built-in function
print(source_max)



