#%% Upper and Lower Case
myVariable = "Hello, World!"

print(myVariable.upper())
print(myVariable.lower())

# %% The strip() method removes any whitespace from the beginning or the end:
myVariable = "        Hello, World!   "
print(myVariable.strip())

# %% Replace String
myVariable = "Hello, World! Hello Hello Hello ...."
print(myVariable.replace("Hello", "Hi",1))
print(myVariable.replace("Hello", "Hi",-1))
print(myVariable.replace("Hello", "Hi",-2))


# %% The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
print(a.split("!"))  # returns ['Hello, World', '']
print(a.split("o"))  # returns ['Hello, World', '']


# %%
