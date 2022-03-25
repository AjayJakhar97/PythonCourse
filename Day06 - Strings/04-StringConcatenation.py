#%% To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

#%% To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#%% Python - Format - Strings 
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this
age = 36
txt = "My name is John, I am " + age
print(txt)

# %% Below are two methods to solve this issue

def getAge(age):
    return age

myAge = getAge(36)

# method 1
txt = "My name is John, I am " + str(myAge)
print(txt)

# method 2
txt = "My name is John, I am {}"
print(txt.format(myAge))

# %% But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# Use the format() method to insert numbers into strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# %% The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${} dollars."
print(myorder.format(quantity, itemno, price))

# myOrder = "I want to pay 49.95 dollars for 3 pieces of item 567."
myOrder = "I want to pay ${} dollars for {} pieces of item {}"
print(myOrder.format(price, quantity,itemno))

#%% You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# %%
