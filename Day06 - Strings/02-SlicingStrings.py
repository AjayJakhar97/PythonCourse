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

#%%
