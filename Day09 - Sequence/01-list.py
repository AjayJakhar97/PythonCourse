# List (Introduction)
# ================================

# Lists are used to store multiple items in a single variable
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# List items are ordered, changeable, and allow duplicate values.
# Lists are created using square brackets:

#%% The empty list is []
myList1 = []
print(myList1)

#%% The following are list of one item ["a"]
myList1 = ["a"]
print(myList1)

myList2 = [3]
print(myList2)

#%% Here is a list with 3 items
myList = ["apple", "banana", "cherry"]
print(myList)

#%% How to verify if it is a list?
print(type(myList))

#%% We can use a list constructor as well to create a list
myList = list()
print(myList)

myList = list(("apple","cherry")) # note the double round-brackets
print(myList)

myList = list(["apple","cherry"]) # We can put square brackets
print(myList)

#%% List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

#%% I can make list of lists as well
list5 = [list1,list2,list3,list4]
for item in list5:
    print(item)

#%% How to call all the items in the lists
list5 = [list1,list2,list3,list4]
for item1 in list5:
    for item in item1:
        print(item)

#%% Lists allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#%% To determine how many items a list has, use the len() function:
myList = ["a", "b", "c", "d", "e", "f"]
len(myList)

#%% To find index value an item has in a list
print(myList.index("b"))

# List - How to access items of the list
# ===============================

# List items are indexed, the first item has index [0], the second item has index [1] etc.
#%% myList[0] is the first element of the list. (index is 0)
myList[0]

#%% myList[1] is the second element of the list and so on. (index is 1)
myList[1]

#%% Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc
print(myList[-1])
print(myList[-2])

#%% Range of Indexes : You can specify a range of indexes by specifying where to start and where to end the range
myList[2:5]

# The search will start at index 2 (included) and end at index 5 (not included)
# Note: When specifying a range, the return value will be a new list with the specified items

#%% By leaving out the start value, the range will start at the first item:
myList[:4]

#%% By leaving out the end value, the range will end at the last item:
myList[3:]

#%% Exercise 1 - print the list listing items from the beginning to, but NOT including, "kiwi"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]



# Solution
# print(thislist[:4])

#%% Exercise 2 - print the list starting from "cherry" to the end

# Solution
# print(thislist[2:])

#%% Exercise 3 - print the list returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Solution
# print(thislist[-4:-1])

# List - How to determine if a specified item is present in a list use the in keyword:
# =====================

#%% running this statement will return True
myList = ["a", "b", "c", "d", "e", "f"]
"a" in myList

#%% running this statement will return False
"r" in myList
#%% running this statement will return False
"a" not in myList
#%% running this statement will return True
"r" not in myList

# List - How to change items
#%% =====================

#%% To add an item to the end of the list, use the append() method. It will add/insert at the end of the list
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.append("orange")
print(thislist)

#%%
myList = ["a", "b", "c", "d", "e", "f"]
print(myList)

myList.append("g")
print(myList)

#%% To append elements from another list to the current list, use the extend() method.
# Example 1
thislist = ["apple", "banana", "cherry"]
myList = ["a", "b", "c", "d", "e", "f"]
thislist.extend(myList)
print(thislist)
print(myList)

#%% Example 2
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#%%
# Note
# 1- The elements will be added to the end of the list.
# 2- you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"] # List
thistuple = ("kiwi", "orange") # Tuple

thislist.extend(thistuple) # Adding tuple to list
print(thislist) # List

# Note: 'tuple' object has no attribute 'extend'

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thistuple.extend(thislist)
# print(thistuple)

#%% List - Change list items
# ==========================
myList = ["a", "b", "c", "d", "e", "f"]
print(myList)

#%% Change the second item
myList[1] = "x"
print(myList)

#%% replace items within a specificed range of index values
myList[3:5] = ["Hello","World"]
print(myList)

#%% The length of the list will change when the number of items inserted does not match the number of items replaced
myList = ["a", "b", "c", "d", "e", "f"]
myList[4:5] = ["Hello","World"]
print(myList)

#%% If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
myList = ["a", "b", "c", "d", "e", "f"]
myList[1:5] = ["Hello"]
print(myList)

# List - To insert items without changing list/items of list, we can use the insert() method.
#%% =====================
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# List - Remove list items
# ==========================

#%% The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#%% To remove using index value, use pop(index)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#%% Note: If you do not specify the index, the pop() method removes the last item.
thislist = ["A", "B", "C"]
thislist.pop()
print(thislist)

#%% The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#%% The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
print(thislist)

del thislist
print(thislist)

#%% The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist.clear()
print(thislist)

# Python - Loop Lists
# =======================

#%% Print all items in the list, one by one  by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#%% You can also loop through the list items by referring to their index number.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Use the range() and len() functions to create a suitable iterable. The iterable created in the example above is [0, 1, 2]

#%% Using a While Loop
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#%% Iterable
'''
The iterable can be any iterable object, like a list, tuple, set etc.

Example
You can use the range() function to create an iterable:
'''
newlist = []
for x in range(10):
    # newlist += [x]
    newlist.append(x)
print(newlist)

# with a condition
newlist = []
for x in range(10):
    if x < 5:
        newlist += [x]
print(newlist)

#%% Looping Using List Comprehension

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

[print(x) for x in range(10) if x < 5]
print()

#%% List Comprehension (shortest syntax)
'''
The Syntax
===============
newlist = [expression for item in iterable if condition == True]
Note: The condition is optional and can be omitted:
'''
# =================================================

thislist = ["apple", "banana", "cherry"]
print([x for x in thislist])

#%% Expression
'''
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
# x is expression here
for x in fruits: 
    # x can be manipulated here and added to the list after that
    newlist.append(x.upper()) 
print(newlist)

# newlist = [x.upper() for x in fruits]
# print(newlist)

#%% Without list comprehension you will have to write a for statement with a conditional test inside
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#%% With list comprehension you can do all that with only one line of code

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

#%% You can set the outcome to whatever you like
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

#%% The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".

