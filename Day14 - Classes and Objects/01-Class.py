'''
Python Classes/Objects
=============================

Python is a multi-paradigm programming language. It supports different programming approaches.

One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

attributes
behavior

Let's take an example:

A parrot is an object, as it has the following properties:

name, age, color as attributes
singing, dancing as behavior

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

In Python, the concept of OOP follows some basic principles:

Class : A class is a blueprint for the object.
We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.

The example for class of parrot can be :

class Parrot:
    pass

Here, we use the class keyword to define an empty class Parrot. 

'''

#%% Create a Class

class Parrot:
    pass

class MyClass:
    x = 5

#%%
'''
Object : From class, we construct instances. An instance is a specific object created from a particular class.
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

The example for object of parrot class can be:

obj = Parrot()

Here, obj is an object of class Parrot.
'''
#%% Create an object from that class

obj = Parrot()

p1 = MyClass()
print(p1.x)

#%% Suppose we have details of parrots. Now, we are going to show how to build the class and objects of parrots.

# Example 1: Creating Class and Object in Python

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

'''
In the above program, we created a class with the name Parrot. Then, we define attributes. The attributes are a characteristic of an object.

These attributes are defined inside the __init__ method of the class. It is the initializer method that is first run as soon as the object is created.

Then, we create instances of the Parrot class. Here, blu and woo are references (value) to our new objects.

We can access the class attribute using __class__.species. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using blu.name and blu.age. However, instance attributes are different for every instance of a class.
'''
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

  def Greetings(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.Greetings()

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
'''
Methods
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

'''
# Example 2 : Creating Methods in Python

class Parrot:
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

'''
In the above program, we define two methods i.e sing() and dance(). These are called instance methods because they are called on an instance object i.e blu.
'''