'''
A function is a block of code which only runs when it is called. 
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''

# %% In-Built functions
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


def my_function(*kids):
    print("The youngest child is " + kids[0])


my_function("Olivia", "Emma", "Ava","Sunil")
my_function("Olivia", "Emma", "Ava")
my_function("Olivia")


# %% Keyword Arguments:
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Olivia", child2="Emma", child3="Ava")

# Note: The phrase Keyword Arguments are often shortened to kwargs in Python documentations

# %% Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Sunil", lname="Kumar")


# %% default parameter: If we call the function without argument, it uses the default value


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# %% default parameter can be none


def ourschool(name=None):
    if name:  # means if True or name is not none
        print(name, " is our school")
    else:
        print("I don't know my school name")


ourschool()
ourschool("KidBit")

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

# %% Task 03 - Write a function 'Fahrenheit_To_Celcius'.
'''Celcius = 5/9 * (Fahrenheit - 32)'''

def Fahrenheit_To_Celcius(TempratureInFahrenheit):
    TempratureInCelcius = 5/9 * (TempratureInFahrenheit - 32)
    print(TempratureInFahrenheit, "Farhenheit = ",
          TempratureInCelcius, "Celcius")

Fahrenheit_To_Celcius(212)


# %%  Notice while True

def forever():
    """ This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
    while True:
        pass

forever()
