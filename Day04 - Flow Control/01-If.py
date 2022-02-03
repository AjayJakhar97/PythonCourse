'''
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:


These conditions can be used in several ways, most commonly in "if statements" and loops.

'''
#%% An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
  print("b is greater than a")

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

# %% or like below can rewrite this like below
a = 333
b = 200

if b > a:
    print("b is greater than a")
elif b < a:
    print("b is smaller than a")

# %% The else keyword catches anything which isn't caught by the preceding conditions.

a = 200
b = 200

if b > a:
    print("b is greater than a")
elif b < a:
    print("b is smaller than a")
else:
    print("a and b are equal")

# %% Task 01 - Create a program to test if number is 0,+ve or -ve
number = int(input("Enter your number: "))

if number > 0:
    print("+ve")
elif number == 0:
    print("zero")
else:
    print("-ve")

#%% Short Hand If
a = 201
b = 200
if a > b: print("a is greater than b")

#%% Short Hand If ... Else
# This technique is known as Ternary Operators, or Conditional Expressions.

a = 201
b = 200
print("A") if a > b else print("B")

#%% You can also have multiple else statements on the same line:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#%% The and keyword is a logical operator, and is used to combine conditional statements
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#%% The or keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#%% Nested If : You can have if statements inside if statements, this is called nested if statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#%% The pass Statement : if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass

