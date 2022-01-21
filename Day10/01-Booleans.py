#%% Booleans represent one of two values: True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

#%% Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#%% Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

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
        return 0

MyObj1 = MyClass()
print(MyObj1)
print(bool(MyObj1))