# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Reference : https://docs.python.org/3/library/random.html

#%% display a random number between 1 and 9
import random
print(random.randrange(1, 10))
# %%
print(random.randrange(1, 2))

# %%
print(random.randrange(1, 3))

# %% random always starts with 0 unless specified otherwise
print(random.randrange(10))