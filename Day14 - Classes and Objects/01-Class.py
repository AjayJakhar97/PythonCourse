'''
Python Classes/Objects
=============================
++ Python is an object oriented programming language.
++ Almost everything in Python is an object, with its properties and methods.
++ A Class is like an object constructor, or a "blueprint" for creating objects.

'''
#%% Create a Class

class MyClass:
    x = 5

#%% Create an object from that class

p1 = MyClass()
print(p1.x)

# %% but how do I modify x ( Object Properties)?

p1.x = 9
print(p1.x)


# %% can we do it while creating an oject itself in a constructor ?

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

class MyClass:
    def __init__(self,x) -> None:
        self.x = x

p1 = MyClass(5)
print(p1.x)

p1 = MyClass(9)
print(p1.x)

# %% Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# %% Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#%% delete an attribute from object
del p1.age

print(p1.age)
# %% Delete Objects
del p1
print(p1)
# %% The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass

# %%
