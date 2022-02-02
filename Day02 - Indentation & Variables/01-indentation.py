# Indentation refers to the spaces at the beginning of a code line.
# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

#%% Let's see a quick example
i = 1
# Notice carefully, I am puttng a 4 spaces as an indentation below
if i == 1:
    print("I have four spaces here...")

#%% The number of spaces is up to you as a programmer, but it has to be at least one.

if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

#%% Notice carefully, I am puttng a single space as an indentation now..
if i == 1:
 print("I have a single spaces here...")

#%% Below code doesn't work because I didn't put any space or Indentation before print

# if i == 1:
# print("Hello")

#%% You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
if 5 > 2:
    print("Five is greater than two!")
    # print("Five is greater than two!")


# %%
