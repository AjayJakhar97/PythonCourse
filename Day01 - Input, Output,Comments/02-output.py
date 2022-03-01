# How to display output - Strings
# %% using "" or ' '
print("Hello World")
print('Hello World')

# %% printing " or ' in output
# Below will fail
print("He said, "Hello World"")

# %%  You can use single quotes to print "" in the output and vice versa
print('He said, "Hello World"')

# %%
print("This is my brother's bike")


# %% Exercises  01

print('He said, "The color of 'red' car is awesome"')
print("He said, "The color of 'red' car is awesome"")

# %%  You can also use an escape character symbol instead. See the examples below
print("He said, \"Hello World\"")
print('This is my brother\'s bike')

# %% Exercises  01

print('He said, \"The color of \'red\' car is awesome\"')
print("He said, \"The color of 'red' car is awesome\"")
print("He said, \"The color of \'red\' car is awesome\"")

# How to display output - Numbers & Strings
# %% print numbers
print("55 + 1")
print(55 + 1)

# %% try to combine string and number

# print("Malay" + 1)
# print(1 + "Malay")
print("Malay" + "1")

# %% print strings together

print("Hello" + "World!")
print("Hello"+" "+"World!")

# How to display calculation's output
# %% calculating values

print(5*5)
print(5/5)
print(5+5)
print(5-5)

# %% what if you do that with strings ?

# print("Hello" * "World")
# print("Hello" / "World")
print("Hello" + "World")
# print("Hello" - "World")

# %% what if you combine strings with numbers
print("Awesome"*5)
# print("Awesome"/5)
# print("Awesome"+5)
# print("Awesome"-5)

#%%
'''
Python end parameter in print()
==================================
By default python’s print() function ends with a newline. A programmer with C/C++ background may wonder how to print without newline.

Python’s print() function comes with a parameter called ‘end’. By default, the value of this parameter is ‘\n’, i.e. the new line character. You can end a print statement with any character/string using this parameter.
'''
#%% 
print("Welcome to")
print("Sunil's coding classes")

# %% ends the output with a <space>
print("Welcome to", end=' ')
print("Sunil's coding classes", end=' ')

#%% Task01 - How to print 'Python@KidBit.com' using parameter 'end= '

print("Python")
print("KidBit")
print("com")

# %% Solution 
print("Python", end='@')
print("KidBit",end='.')
print("com")

# Cover variables and then come back here...

#
# %% How to print variables
import datetime

name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)

print(name)
print(age)
print(anniversary)
print(anniversary.strftime('%A, %B %d, %Y'))
print()
print(anniversary.strftime('%A, %Y'))
print(anniversary.strftime('%B %d,%A, %Y'))
print(anniversary.strftime('%B,%A, %Y'))

# %%
# %% f string for formatting
import datetime

name = 'Fred'
age = 50
anniversary = datetime.date(1991, 10, 12)

'My name is {name}. Next year, my age will be {age+1}. My anniversary is {anniversary:%A, %B %d, %Y}.'

f'My name is {name}. Next year, my age will be {age+1}. My anniversary is {anniversary:%A, %B %d, %Y}.'

# %%
