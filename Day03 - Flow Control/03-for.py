# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

#%% Create a quick list
fruits = ["apple", "banana", "cherry"]

#%% Let's get each item from the list
for items in fruits:
    print(items)

#%% Let's get output on single line with seperator like space ' ' or a comma , etc.
for items in fruits:
    print(items, end=' ')

for items in fruits:
    print(items, end=',')

#%% We can also output positions along with elements like below
for items in range(len(fruits)):
    print(items, " - ", fruits[items])
# %% Looping Through a String : Even strings are iterable objects, they contain a sequence of characters:

for x in "banana":
  print(x)

# You can use break statement for for loop as well

#%% Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#%% Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#%% The continue Statement
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#%% The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Using the range() function:

for x in range(6):
  print(x)

#%% Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#%% Else in For Loop

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#%% Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#%% Nested Loops : The "inner loop" will be executed one time for each iteration of the "outer loop":

adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjective:
  for y in fruits:
    print(x, y)

#%% The pass Statement is allowed in for loops
for x in [0, 1, 2]:
  pass
