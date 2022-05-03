'''
A function is a block of code which only runs when it is called. 
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

# %% In-Built functions
from ast import Not


print()

abs(-5)


# %% You can create your own functions too
# In Python a function is defined using the def keyword


def hello():
    ''' prints Hello, world!'''
    print("Hello, world!")

# To call a function, use the function name followed by parenthesis
hello()

# %% Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma

def myName(name):
    print("My name is", name)

myName("Sunil")

# Parameters or Arguments?
'''From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
'''

# %% By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less

def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Sunil", "Kumar")

# If you try to call the function with 1 or 3 arguments, you will get an error
my_function("Sunil")

# %% Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:


def my_function(firstKid, *kids):
    print(f"The youngest kid is {firstKid}")
    print(f"The rest of the kids are {list[kids]}" )


my_function("Olivia", "Emma", "Ava")

# %% Keyword Arguments:
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Olivia", child2="Emma", child3="Ava")

# %% Arbitrary Keyword Arguments, **kwargs
# Note: The phrase Keyword Arguments are often shortened to kwargs in Python documentations
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly


def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Sunil", lname="Kumar")

#%% It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax. 
# The following code yields the following output: The sum is: 6 Result: 1

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

#%% Exercise : Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more).
# The foo function must return the amount of extra arguments received. 
# The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.

def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")

# %% default parameter: If we call the function without argument, it uses the default value


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# %% default parameter can be none

def my_function(country = None):
    if country:
        print("I am from " + country)
    else:
        print("I am from nowhere")

my_function()
my_function("India")

# %% What if you have bool? default parameter can be none

def my_function(typeOfNumber = None):
    if typeOfNumber == True:
        return typeOfNumber
    else:
        return -1

# 1st two give -1
print(my_function(0))
print(my_function())
# Below is correct
print(my_function(1))

# %% How to fix it?

def my_function(typeOfNumber = None):
    if typeOfNumber is not None:
        return typeOfNumber
    else:
        return -1

print(my_function(0))
print(my_function())
print(my_function(1))

# %% The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


def myfunction():
    pass

# %% Task 01- Create a function to calculate area of a circle


def areaCircle(radius):
    area = 3.14 * radius ** 2
    print("Area of circle = ", area)


# %% Test your functions
areaCircle(1)
areaCircle(2)

# %% Task 02 - Write a function 'areaTriangle(base,height)'. Formula is 0.5*base*height


def areaTriangle(base, height):
    area = 0.5*base*height
    print("Area of triangle = ", area)


# Let's test it
# %% Test01 - areaTriangle(1,2)
areaTriangle(1, 2)

# %% Test02 - areaTriangle(1,4)
areaTriangle(1, 4)

# %% Task 03 - Write a function 'Fahrenheit_To_Celsius'.
'''Celsius = 5/9 * (Fahrenheit - 32)'''

def Fahrenheit_To_Celsius(TemperatureInFahrenheit):
    TemperatureInCelsius = 5/9 * (TemperatureInFahrenheit - 32)
    print(TemperatureInFahrenheit, "Fahrenheit = ",
          TemperatureInCelsius, "Celsius")

Fahrenheit_To_Celsius(212)


# %%  Notice while True

def forever():
    """ This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
    while True:
        pass

forever()

#%% task 04 - Write a function that takes your first name and says Hi to you.
# for example - 'Hi Sunil'

def Hi(name="Superman"):
    print("Hi", name)

Hi("Sunil")