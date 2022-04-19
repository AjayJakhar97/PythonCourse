'''
JSON (JavaScript object notation) in Python
===============
++ JSON is a syntax for storing and exchanging data.
++ JSON is text, written with JavaScript object notation.
++ Python has a built-in package called json, which can be used to work with JSON data.

'''

# %% Import the json module:
import json

# %% Parse JSON
# 1- Convert from JSON to Python
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#%% 2- Convert from Python to JSON

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# %% You can convert Python objects of the following types, into JSON strings:
'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null

'''

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# %% Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# %% Use the indent parameter to define the numbers of indents:

json.dumps(x, indent=4)

# %% You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator:

json.dumps(x, indent=4, separators=(". ", " = "))
# %% Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)
# %%

'''
Check Your Understanding
'''
#%% Task: How to convert a txt string with \n to a dictionary ?

import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])

#%%  Task: Write a function that uses json.dumps to make a human-readable printout of a nested data structure.

import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

#%% Task: Say we had a JSON string in the following format. How would you convert it so that it is a python list?

entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""

# entertainment.json()
# json.dumps(entertainment)
# json.loads(entertainment)

#%% Task: Because we can only write strings into a file, if we wanted to convert a dictionary d into a json-formatted string so that we could store it in a file, what would we use?

'''
A. json.loads(d)
B. json.dumps(d)
C. d.json()

'''