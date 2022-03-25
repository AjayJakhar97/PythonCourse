'''
Python Try Except
====================
1- The try block lets you test a block of code for errors.
2- The except block lets you handle the error.
3- The else block lets you execute code when there is no error.
4- The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
====================
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:
'''

#%% Example : The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")

#%% This statement will raise an error, because x is not defined:

'''Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error:

'''
print(x)

#%% Many Exceptions
'''You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example
Print one message if the try block raises a NameError and another for other errors:
'''
# x = "something"
try:
    # print(x)
    x+5
except NameError:
    print("Not defined")
except:
    print("something else went wrong")

#%% Else
'''You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:
'''
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#%% Finally
'''The finally block, if specified, will be executed regardless if the try block raises an error or not.
'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#%% This can be useful to close objects and clean up resources:

# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# The program can continue, without leaving the file object open.

#%% Raise an exception
'''As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.

Example
Raise an error and stop the program if x is lower than 0:
'''
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

#%% The raise keyword is used to raise an exception.
'''
You can define what kind of error to raise, and the text to print to the user.

Example
Raise a TypeError if x is not an integer:
'''
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


# %% Task 01 - Create a program to test if number is 0,+ve or -ve

number = input("Enter your number: ")
try:
    int(number)
    # number = int(number)
    if number > 0:
        print("+ve")
    elif number == 0:
        print("zero")
    elif number < 0:
        print("-ve")
except:
    print("Invalid Input")

#%%

#%% Task 02 - Create a coffee maker program 
# You have below resources 
# water, milk, coffee beans and sugar

'''
1 cup of coffee uses 
==========================
Water : 200 ml
Milk  : 70 ml
Coffee beans : 8 gm
Sugar : 50 gm
'''

# set the quantity of resources for each cup of a coffee and reduce it everytime you make a cup of a coffee
# if you fall short of resources, you report it

# water in ml
water = 300

# Milk in ml
milk = 300

# coffee beans in gms
coffeeBeans = 50

# sugar in gms
sugar = 500

# Program
def makeCoffee():
    pass

makeCoffee()
