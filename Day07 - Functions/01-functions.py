#%% In-Built functions
abs(-5)
print()

#%% You can create your own functions too


def hello():
    ''' prints Hello, world!'''
    print("Hello, world!")


hello()

#%%


def myName(name):
    print("My name is ", name)


myName("Sunil")

#%% default parameter


def ourschool(name="KidBit"):
    print(name, " is our school")


ourschool()
#%% default parameter can be none


def ourschool(name=None):
    if name:  # means if True or name is not none
        print(name, " is our school")
    else:
        print("I don't know my school name")


ourschool()
# ourschool("KidBit")

#%% What if you create function with name that already exists


def print():
    print("This is my print function")


print()

#%% Task 01- Create a function to calculate area of a circle


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
#%% Test01 - areaTriangle(1,2)
areaTriangle(1, 2)

#%% Test02 - areaTriangle(1,4)
areaTriangle(1, 4)

# %% Task 03 - Write a function 'Fahrenheit_To_Celcius'.
'''Celcius = 5/9 * (Fahrenheit - 32)'''


def Fahrenheit_To_Celcius(TempratureInFahrenheit):
    TempratureInCelcius = 5/9 * (TempratureInFahrenheit - 32)
    print(TempratureInFahrenheit, "Farhenheit = ",
          TempratureInCelcius, "Celcius")


#%% Test Fahrenheit_To_Celcius
Fahrenheit_To_Celcius(212)

#%% Task04 - Create your own version of absolute and print functions


def myAbs(number):
    if number > 0:
        return number
    else:
        return -number


#%% Let's test it
myAbs(5)
myAbs(-5)
myAbs(0)

#%%  Notice while True


def forever():
    """ This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
    while True:
        pass


#%% test it
forever()
