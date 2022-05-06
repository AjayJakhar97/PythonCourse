
'''
https://www.datacamp.com/tutorial/decorators-python
https://realpython.com/primer-on-python-decorators/

Decorators : A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate. 

A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

Decorator allows you to make simple modifications to callable objects like functions, methods, or classes. 

The syntax for decorator on function is

@decorator
def functions(arg):
    return "value"

Is equivalent to:

def function(arg):
    return "value"
function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions
'''
#%% Functions :
# =======================================
# Before you can understand decorators, you must first understand how functions work. For our purposes, a function returns a value based on the given arguments. Here is a very simple example:

def plus_one(number):
    return number + 1

add_one = plus_one # returning a reference to the function plus_one
add_one(5)

#%% First-Class Objects : 
# =======================================
# In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). Consider the following three functions:

def say_hello(name): # name given as a string
    return f"Hello {name}"

def be_awesome(name): # name given as a string
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func): # expects a function as its argument
    return greeter_func("Bob")

# We can, for instance, pass it the say_hello() or the be_awesome() function:
greet_bob(say_hello)
greet_bob(be_awesome)

# Note: The say_hello function is named without parentheses. This means that only a reference to the function is passed. The function is not executed. The greet_bob() function, on the other hand, is written with parentheses, so it will be called as usual.

#%% 2nd example of passing function as an argument

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)

#%% Functions Returning other Functions
# ======================================= 

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi # returning a reference to the function say_hi

hello = hello_function() # returning a reference to the function say_hi
hello() # then we call say_hi()

#%% 2nd example 

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        # Do not add parentheses to the inner functions — first_child — upon returning. 
        # That way, you got a reference to each function that you could call in the future.
        return first_child
    else:
        # Again...do not add parentheses to the inner functions — second_child — upon returning. 
        return second_child

first = parent(1)
first
'''
<function __main__.parent.<locals>.first_child()>

The first variable refers to the local first_child() function inside of parent()

'''
second = parent(2)
second
'''
<function __main__.parent.<locals>.second_child()>
The second variable refers to the local second_child() function inside of parent()
'''
#%% You can now use first and second as if they are regular functions, even though the functions they point to can’t be accessed directly

first()
second()

# %% Inner Functions :
# =======================================
# It’s possible to define functions inside other functions. Such functions are called inner functions. Here’s an example of a function with two inner functions:

def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

# What happens when you call the parent() function?
parent()

# Whenever you call parent(), the inner functions first_child() and second_child() are also called. But because of their local scope, they aren’t available outside of the parent() function.

#%% Another example of inner functions

def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result

plus_one(4)


#%% Nested Functions have access to the Enclosing Function's Variable Scope

def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")


#%% Now that we have seen that functions are just like any other object in Python, let's explore decorator
# Simple Decorators
# ======================

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# The so-called decoration happens at the following line:
say_whee = my_decorator(say_whee)
# The name say_whee now points to the wrapper() inner function because that's my_decorator(say_whee) retruned reference to wrapper
say_whee

#%% Can you guess what happens when you call say_whee()
say_whee()

# Put simply: decorators wrap a function, modifying its behavior.



#%% More examples

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

# decorator
say_whee = not_during_the_night(say_whee)

say_whee()

#%% @decorator syntax
'''
Syntactic Sugar!
The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times. In addition, the decoration gets a bit hidden away below the definition of the function.

Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:

'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.


#%% A decorator is just another function which takes a functions and returns one. For example you could do this:
def repeater(multiply):
    def new_function(num1, num2):
        multiply(num1, num2) # we run the old function
        multiply(num1, num2) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value

# This would make a function repeat twice.
@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)

#%% We could do below as well

def repeater(old_function):
    def new_function(*args):
        old_function(*args) # we run the old function
        old_function(*args) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value

# This would make a function repeat twice.
@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)


#%% You can also make it change the output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function

@double_out
def multiply(num1, num2):
    return num1 * num2

multiply(2, 3)

#%%
# change input
def double_Ii(old_function):
    def new_function(arg): # only works if the old function has one argument
        return old_function(arg * 2) # modify the argument passed
    return new_function

# and do checking.
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function

#%% Let's say you want to multiply the output by a variable amount. You could define the decorator and use it as follows:

def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15
# You can do anything you want with the old function, even completely ignore it! Advanced decorators can also manipulate the doc string and argument number

#%% Exercise : Make a decorator factory which returns a decorator that decorates functions with one argument. The factory should take one argument, a type, and then returns a decorator that makes function should check if the input is the correct type. If it is wrong, it should print("Bad Type") (In reality, it should raise an error, but error raising isn't in this tutorial). Look at the tutorial code and expected output to see what it is if you are confused (I know I would be.) Using isinstance(object, type_of_object) or type(object) might help.

def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])

