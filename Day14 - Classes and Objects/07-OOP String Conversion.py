# %% Pythonic OOP String Conversion: __repr__ vs __str__

'''
Reference: https://docs.python.org/3/reference/datamodel.html#object.__repr__

object.__repr__(self)
========================
Called by the repr() built-in function to compute the “official” string representation of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value (given an appropriate environment). If this is not possible, a string of the form <...some useful description...> should be returned. The return value must be a string object. If a class defines __repr__() but not __str__(), then __repr__() is also used when an “informal” string representation of instances of that class is required.

This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.

object.__str__(self)
========================
Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely printable string representation of an object. The return value must be a string object.

This method differs from object.__repr__() in that there is no expectation that __str__() return a valid Python expression: a more convenient or concise representation can be used.

The default implementation defined by the built-in type object calls object.__repr__().
'''

# str() and repr() both are used to get a string representation of object.

# Example of str():

import datetime
s = 'Hello, Geeks.'
print('============Example of str()============')
print(str(s))
print(str(2.0/11.0))
print('============Example of repr()============')

# Example of repr():

s = 'Hello, Geeks.'
print(repr(s))
print(repr(2.0/11.0))

# %% Let's check one more example

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))
# str() displays today’s date in a way that the user can understand the date and time.

# prints the official format of date-time object
print(repr(today))
# repr() prints “official” representation of a date-time object (means using the “official” string representation we can reconstruct the object).

#   we can use repr() function with eval() to construct the object.
temp = eval(repr(today))
print(temp)

# %% How to make them work for our own defined classes?

# A user defined class should also have a __repr__ if we need detailed information for debugging. And if we think it would be useful to have a string version for users, we create a __str__ function.

# Python program to demonstrate writing of __repr__ and
# __str__ for user defined classes

# A user defined class to represent Complex numbers


class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

# Same as "print t"
print(str(t))
print(repr(t))

# %%
# dunder methods are methods that start with a double underscore (__)—it’s just kind of been shortened to dunder.

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'


a = Car('Red', '20')

# We have both of these methods now
a.__str__
a.__repr__

my_car = Car('Red', '20')

# %%
print(my_car)
# %%
my_car

# %% Now let's remove below from class Car and run my_car again.
# and you will see <__main__.Car at 0x2559f2d8160>
# instead of  __repr__ for Car

'''
    def __repr__(self):
        return '__repr__ for Car'
'''

# %%

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)


my_car = Car('Red', '20')
print(my_car)
my_car

# %% Example ( version 1)

class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age


p = Person('Sunil', 34)

print(p.__str__())
print(p.__repr__())

# %% Example ( version 2)
# As you can see that the default implementation is useless. Let’s go ahead and implement both of these methods.

class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

p = Person('Sunil', 34)

print(p.__str__())
print(p.__repr__())

# %%
# Earlier we mentioned that if we don’t implement __str__ function then the __repr__ function is called.
# Just comment the __str__ function implementation from the Person class and print(p) will print {name:Sunil, age:34}.

class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    # def __str__(self):
    #     return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

p = Person('Sunil', 34)

print(p.__str__())
print(p.__repr__())

# %% Both __str__ and __repr__ functions return string representation of the object. The __str__ string representation is supposed to be human-friendly and mostly used for logging purposes, whereas __repr__ representation is supposed to contain information about object so that it can be constructed again. You should never use these functions directly and always use str() and repr() functions.

print(str(p))
print(repr(p))

# %%

fruit = ['Cherry', 'Banana', 'Apple']
[str(item) for item in fruit]
