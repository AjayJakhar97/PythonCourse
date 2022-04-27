#%% Booleans represent one of two values: True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

#%% Print a message based on whether the condition is True or False:

a = 200
b = 33

# if !True:
if not True:
  print("b is greater than a")
else:
  print("b is not greater than a")

#%% Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool())

#%% Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#%% Most Values are True

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#%% The following will return False:

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#%% Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

#%% You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#%% Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
y = "Hello"
print(isinstance(x, int))
print(isinstance(y, int))

#%% One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class MyClass:
    def __len__(self):
    # def something(self):
        return 0

MyObj1 = MyClass()
# print(MyObj1)
print(bool(MyObj1))


# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


#%% any()
'''
What you'll cover....
=======================
Basic usage of any()
How to eliminate long or chains from your code?
How to use any() with list compreshensions
How to use the inverse, not any()?
How any() evaluates values that aren't explicitly True or False?
Any important difference between any() and or
What short-circuting is?
'''
#%% 
'''
Basic
=====
++ It accepts one argument, an iterable.
> a list []
> a set {}
> a dictionary {key:value}
> a generator ()
++ Returns one boolean value, True or False

'''
x = True
y = True
z = False

# Let's run the code now
if x is True or y is True or z is True :
  print("One of the elements was True")
else:
  print("All are false")

#%% Let's see how to use any function now...

x = True
y = True
z = False

# Create different iterables... 
myList = [x,y,z]
# print(myList)

mySet = {x,y,z}
# print(mySet)

myDict = {
  'x':False,
  'y':False,
  'z':False
  }
# print(myDict)

myGenerator = (x,y,z)
# print(myGenerator)

# using any() now...

if any(myList):
  print("One of the elements was True")
else:
  print("All are false")

#%% We need to be careful when using dict
#%%
# if any(myDict):
# if any(myDict.keys()):
if any(myDict.values()):
  print("One of the elements was True")
else:
  print("All are false")

#%% Note: When used on a dictionary, the any() function checks if any of the keys are true, not the values.
mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)


#%% How would you check if any student is "True" here ?
# long method

students = [False,False,True,False]
any_pass = False

for student in students:
  if student is True:
    any_pass = True
    break

if any_pass is True:
  print("There is at least one student who passed")

#%% Short any function

if any(students) is True:
# if any(students):
  print("There is at least one student who passed")

# %% Task: Check if there is any open WiFi in your neighbourhood and return "Found an open WiFi" if there is any...

WiFi = {
'xBox' : 'Open',
'iPhone' : 'Locked',
'Arrow' : 'Locked',
'SuperMan' : 'Locked'
}

def myFunction(myDict):
    for item in WiFi.values():
        if item == 'Open':
            return True
    return False

if myFunction(WiFi) == True:
    print("Found an open WiFi")
else:
    print('No open WiFi')

#%% Short method

WiFi = {
'xBox' : 'Open',
'iPhone' : 'Locked',
'Arrow' : 'Locked',
'SuperMan' : 'Locked'
}

if any([True for item in WiFi.values() if item == 'Open']):
    print("Found an open WiFi")
else:
    print('No open WiFi')

#%% How to Use Python's any() Function to Check for Letters in a String

