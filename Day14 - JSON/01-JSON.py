'''
JSON in Python
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
