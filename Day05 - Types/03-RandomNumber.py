# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Reference : https://docs.python.org/3/library/random.html

#%% display a random number between 1 and 9
import random
print(random.randrange(1, 3))

# %%
print(random.randrange(1, 2))

# %%
print(random.randrange(1, 3))

# %% random always starts with 0 unless specified otherwise
print(random.randrange(10))


#%% Exercise 01 - (if and random)

'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
'''

# Remember to use the random module 👇
import random

# Get the two random numbers
randomSide = random.randrange(0, 2)
# randomSide = random.randint(0, 1)

# write the logic using those random numbers
if randomSide == 1:
    print("Heads")
else:
    print("Tails")

#%%
print (5)