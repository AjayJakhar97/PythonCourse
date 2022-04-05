'''
=========================
Python - Slicing Strings
=========================
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
'''
#%% Get the characters from position 2 to position 5 (not included):
myVariable = "Hello, World!"
print(myVariable[2:5])

#%% Slice From the Start
myVariable = "Hello, World!"
print(myVariable[:5])


#%% Slice To the End
myVariable = "Hello, World!"
print(myVariable[2:])

#%% Use negative indexes to start the slice from the end of the string:
myVariable = "Hello, World!"
print(myVariable[-5:-2])

#%% Task01 - How to reverse a string?
#  the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.

myVariable = "Hello, World!"
print(myVariable[::-1])

#%% Let's create a function for this

def my_ReverseString_function(x):
  return x[::-1]

mytxt = my_ReverseString_function("I wonder how this text looks like backwards")

print(mytxt)

# %%
