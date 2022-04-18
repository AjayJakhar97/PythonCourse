'''
Inheritance
=====================
Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
'''
#%% Example 3: Use of Inheritance in Python

# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

'''
In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). The child class inherits the functions of parent class. We can see this from the swim() method.

Again, the child class modified the behavior of the parent class. We can see this from the whoisThis() method. Furthermore, we extend the functions of the parent class, by creating a new run() method.

Additionally, we use the super() function inside the __init__() method. This allows us to run the __init__() method of the parent class inside the child class.

Encapsulation
==============
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.

'''
#%% Example 4: Data Encapsulation in Python

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

'''
In the above program, we defined a Computer class.

We used __init__() method to store the maximum selling price of Computer. Here, notice the code

c.__maxprice = 1000
Here, we have tried to modify the value of __maxprice outside of the class. However, since __maxprice is a private variable, this modification is not seen on the output.

As shown, to change the value, we have to use a setter function i.e setMaxPrice() which takes price as a parameter.
'''
'''
Polymorphism

Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

'''
#%% Example 5: Using Polymorphism in Python

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

'''
In the above program, we defined two classes Parrot and Penguin. Each of them have a common fly() method. However, their functions are different.

To use polymorphism, we created a common interface i.e flying_test() function that takes any object and calls the object's fly() method. Thus, when we passed the blu and peggy objects in the flying_test() function, it ran effectively.

https://www.programiz.com/python-programming/class

'''

























'''

Python Inheritance
=====================

++ Inheritance allows us to define a class that inherits all the methods and properties from another class.
++ Parent class is the class being inherited from, also called base class.
++ Child class is the class that inherits from another class, also called derived class.

'''

#%% Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method:

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
