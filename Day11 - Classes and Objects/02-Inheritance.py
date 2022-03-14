'''
Python Inheritance
=====================

++ Inheritance allows us to define a class that inherits all the methods and properties from another class.
++ Parent class is the class being inherited from, also called base class.
++ Child class is the class that inherits from another class, also called derived class.

'''

#%% Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method:

from fnmatch import fnmatch


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#%% Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass  # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

#%% Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()

# %% When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
class Student(Person):
  def __init__(self, fname, lname):
      # Use the super() Function
      # super().__init__(fname, lname)
      # or specify class name to inherit the methods and properties from its parent.
      Person.__init__(fname, lname)

# %% Add Properties
class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname, lname)
      self.graducationYear = 2022

# %%
obj1 = Student("Sunil","Kr")
print(obj1.graducationYear)
# %%
class Student(Person):
  def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graducationYear = year

# %%
obj1 = Student("Sunil","Kr",2010)
print(obj1)
# %% Add Methods
class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname, lname)
  
  def welcome(self):
    print("Welcome students")
  
  # def printname(self):
  #   print(self.firstname)

obj1 = Student("Sunil","Kr")
obj1.welcome()
obj1.printname()
# %% If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname, lname)
  
  def welcome(self):
    print("Welcome students")
  
  # def printname(self):
  #   print(self.firstname)

obj1 = Student("Sunil","Kr")
obj1.welcome()
obj1.printname()
