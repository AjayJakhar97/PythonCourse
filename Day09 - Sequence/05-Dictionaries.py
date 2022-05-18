# Dictionary (Introduction)
# ================================

# Dictionary is used to store multiple items in a single variable.
# Dictionary is one of 4 built-in data types in Python used to store collections of data, the other 3 are List,Tuple and Set, all with different qualities and usage.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates
# Dictionaries are written with curly brackets, and have keys and values:

# %% Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# %% Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(thisdict["brand"])

# %% Get() method
print(thisdict.get("brand"))
print(thisdict.get("brand","Wrong key passed"))
print(thisdict.get("name","Wrong key passed"))

# %% Dictionaries cannot have two items with the same key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# %% Dictionary Length
print(len(thisdict))

# %% The values in dictionary items can be of any data type
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
    "thisdict": {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
}
print(thisdict)

# %% dictionaries are defined as objects with the data type 'dict

print(type(thisdict))

# %% change the value of a key
thisdict["year"] = 2022
print(thisdict)

# %% The keys() method will return a list of all the keys in the dictionary.
thisdict.keys()
# %%
thisdict.values()
# %% The items() method will return each item in a dictionary, as tuples in a list.
thisdict.items()
# %% Check if Key Exists
if "year" in thisdict.keys():
    print(thisdict["year"])
# %% Check if "2022" value Exists
if 2022 in thisdict.values():
    print("yes, it exists")
else:
    print("Nope, it doesn't exist")

# %% Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"year": 2020})
thisdict.update({"name": "Sunil"})

print(thisdict)

# %% Removing items
# The pop() method removes the item with the specified key name:

thisdict.pop("brand")
print(thisdict)

# %%
print(thisdict)
# %% The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)
# %% The del keyword removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# %% The del keyword can also delete the dictionary completely:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
# this will cause an error because "thisdict" no longer exists.
print(thisdict)
# %% The clear() method empties the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# %% You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# for item in thisdict:
# for item in thisdict.keys():
for item in thisdict.values():
    print(item)

# %% Print all values in the dictionary, one by one:

for x in thisdict:
    print(thisdict[x])

# %% You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
    print(x)

# %% You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
    print(x)

# %% Do you remember how to get items using items) method?

for x in thisdict.items():
    print(x)

# %% To loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
    print(x, y)

#%%
for x, y in thisdict.items():
    print(x,' = ', y)

# %% Create a new reference dictionary

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(id(dict1))

dict2 = dict1
print(id(dict1))

dict1.update({"year": 2022})

print(dict1)
print(id(dict1))
print(dict2)
print(id(dict2))

# %% Make a copy of a dictionary with the copy() method:
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dict2 = dict1.copy()

dict1.update({"year": 2022})

print(dict1)
print(dict2)
# %% Make a copy of a dictionary with the dict() function
dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict2 = dict(dict1)

dict1.update({"year": 2022})

print(dict1)
print(dict2)

# %% Nested Dictionaries

# 1st method - Create dictionaries first

child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

# Now create a new dictionary and add dictionaries there

myfamily = {
    "kid1": child1,
    "kid2": child2,
    "kid3": child3
}

print(myfamily)

print(myfamily["kid1"]["year"])

#%% 2nd method - Create dictionaries as values of your master dictionary

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)
print(myfamily["child1"]["year"])

# %% Task01 - How to remove duplicate items from a list using dictionary?


def removeDuplicateItems(myList):
    myList = list(dict.fromkeys(myList))
    return myList

myList01 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 2, 1]
print(removeDuplicateItems(myList01))

myList02 = ["Apple", "Banana", "Apple", "Cherry"]
print(removeDuplicateItems(myList02))

# %% How to merge dictionaries ?

dictA = {"a": 1, "b": "something"}
dictB = {"name": "John", "class": "medium"}
dictC = dictA | dictB
print(dictC)

#%% What's wrong here with Keys?

dictA={
    "age" : 13,
    "height" : "5.2ft"
}
dictB={
    "age" : 18,
    "height" : "6.0ft"
}
dictC = dictA | dictB
print(dictC)

# %% Task: How to get unique ordered list?

list1 = ["Hey", "How", "are", "Hey", "you", "?", "?"]
list2 = list(dict.fromkeys(list1))
print(list2)

# %% Task : Extract the value associated with the key 'color' and assign it to the variable 'color'. Do not hard code this

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

# color = # you logic goes here...
color = info['personal_data']['physical_features']['color']['hair']
print(color)

#%% 

D = dict() 

D[0] = 1
D[1] = 0 

print(D)

#%% 
x = [0,1]

D = dict() 

D[x[0]] = x[1]
D[x[1]+7] = x[0] 

print(D)

#%%
D = dict() 
for x in range(2): 
    print(D) 

#%%
D = dict() 
for x in enumerate(range(2)): 
    D[x[0]] = x[1] 
    D[x[1]+7] = x[0] 
print(D) 

#%% Assessment 

# 1. Select the correct ways to get the value of marks key.

student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

m = student.get(2)
m = student.get('marks')
m = student[2]
m = student['marks']

# 2. In Python, Dictionaries are immutable

False
True

# 3. Select the correct way to access the value of a history subject

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

sampleDict['class']['student']['marks']['history']
sampleDict['class']['student']['marks'][1]
sampleDict['class'][0]['marks']['history']

# 4. What is the output of the following dictionary operation

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)
KeyError: ‘age’
None

# 5. Dictionary keys must be immutable

True
False

# 6. Items are accessed by their position in a dictionary and All the keys in a dictionary must be of the same type.

True
False

# 7. Select the all correct way to remove the key marks from a dictionary

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

student.pop("marks")
del student["marks"]
student.remove("marks")
student.popitem("marks")

# 8. Select all correct ways to copy a dictionary in Python

dict2 = dict1.copy()
dict2 = dict(dict1)
dict2 = dict1

# 9. What is the output of the following code

dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)

True
False

# 10. Select correct ways to create an empty dictionary

sampleDict = {}
sampleDict = dict()
sampleDict = dict{}

# 11. What is the output of the following dictionary operation

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)

KeyError: ‘age’
None

# 12. Select the correct way to print Emma’s age.

student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
student[0][1]
student[1]["age"]
student[0]["age"]

# 13. Please select all correct ways to empty the following dictionary

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

del student
del student[0:2]
student.clear()

# 14. What is the output of the following

sampleDict = dict([
    ('first', 1),
    ('second', 2),
    ('third', 3)
])
print(sampleDict)
'''
[ (‘first’, 100), (‘second’, 200), (‘third’, 300) ]

Options: SyntaxError: invalid syntax

{‘first’: 1, ‘second’: 2, ‘third’: 3}

'''
