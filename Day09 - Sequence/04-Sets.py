# Sets (Introduction)
# ================================

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

myset = {"apple", "banana", "cherry"}

#%% Create a set
myset = {"apple", "banana", "cherry"}
print(myset)

# %% Duplicates Not Allowed and will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# %% Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# %% Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

#%%
#%% Be careful when using bool with int 0 and 1 or decimal 1.0

var1 = {1,'Python', ('abc','xyz'),False}
print(var1)

var2 = {0,'Python', ('abc','xyz'),True}
print(var2)

var3 = {1,'Python', ('abc','xyz'),True}
# var3 = {1.0,'Python', ('abc','xyz'),True}
print(var3) # Where is True

var4 = {0,'Python', ('abc','xyz'),False}
print(var4) # Where is False

var5 = {2,'Python', ('abc','xyz'),True}
print(var5)

var6 = {1,'Python', ('abc','xyz'),str(True)}
print(var6)

# %% sets are defined as objects with the data type 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset))

# %% set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# %% You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, 

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#%% or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("orange" in thisset)

# %% Add an item to a set, using the add() method
thisset = {"apple", "banana", "cherry"}
print(id(thisset))
thisset.add("orange")
print(thisset)
print(id(thisset))


# %% Add Sets or any other iterable
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]

thisset.update(tropical,mylist)

print(thisset)

# %% Remove Item - Remove() method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)

# %% Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")

# %% Remove Item - discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)
# %% No errors if it doesn't exist
thisset.discard("banana")

# %% Remove Item - pop() method
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed


# %% The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# %% The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# %% There are several ways to join two or more sets in Python
# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# %% The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

#%% Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
print(x)

y = {"google", "microsoft", "apple"}
print(y)

x.intersection_update(y)
# x = x.intersection(y)

print(x)

# %% The intersection() method will return a new set, that only contains the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# %% Keep All, But NOT the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# %%  The symmetric_difference() method will return a new set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#%% Write a Python program to add member(s) in a set.

#A new empty set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)

#%% Write a Python program to check if two given sets have no elements in common.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","apple"}

z = x.intersection(y)
if z:
  print(z)
else:
  print('No common elements found')


#%% isdisjoint() method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

if z:
  print('No common elements found')
else:
  print('There is at least one command element')

