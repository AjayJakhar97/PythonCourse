# Tuple (Introduction)
# ================================

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets

#%% Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple")
print(thistuple)


#%% Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#%% It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(type(thistuple))

#%% Below code shows tuple are immutable ( or unchangeable) as the ID means object is changed if we change it
list_data = ['an', 'example', 'of', 'a', 'list']
tuple_data = ('this', 'is', 'an', 'example', 'of', 'tuple')

# get IDs of them
print(id(list_data))
print(id(tuple_data))

# Adding elements to list and tuple
list_data += ['Headset']
tuple_data += ('Keyboard','mouse')

# print them
print(list_data)
print(tuple_data)

# get IDs of them
print(id(list_data))
print(id(tuple_data))

#%% compare data of list or tuple

list_data1 = [1,2,33,5,2]
list_data2 = [1,2,33,5,2]

print(list_data1 is list_data2)
print(list_data1 == list_data2)

#%% You can't compare list with tuple

list_data1 = [1,2,33,5,2]
tuple_data = (1,2,33,5,2)
print(list_data1 == tuple_data)

# %% You can use len to count the number of elements
studentList = ("Ram", "Gita", "Chris")
print(studentList)

count = len(studentList)

print(f"Total elements : {count}")

#%% even this will create a tuple 
studentList = "Ram", "Gita", "Chris"

print(studentList)

count = len(studentList)
print(f"Total elements : {count}")

#%% but we shouldn't do this. try 

studentList1 = "Ram"
print(studentList1)
print(type(studentList1))
count = len(studentList1)
print(f"Total elements : {count}")


#%% or this...
studentList2 = ("Ram")
print(studentList2)
print(type(studentList2))

count = len(studentList2)
print(f"Total elements : {count}")

#%% What if have to get one element out of this for example just "Ram" as one?
studentList = ["Ram"]
print(type(studentList))
count = len(studentList)
print(count)

#%% Change Tuple Values
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)

print(x)

# %% Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# %% Remove Items 
# (Workaround) : Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# %% delete the tuple completely
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# %% Packing a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking". Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

# Note: The number of variables must match the number of values in the tuple
green, yellow, red = fruits

print(green)
print(yellow)
print(red)

# %% Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example : Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# %% Example 2: If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# %% Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# %% If you want to multiply the content of a tuple a given number of times, you can use the * operator
# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# %%
