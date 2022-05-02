# Python Generators
# ===================
# Let's get some terminology right first...

# Iterable - An object with method __iter__ or __getitem__ which creates iterator
# Iterator - Iterators has mehod __next__() and it helps to get next item
# Iteration -  It is the process of iterating items

# Generators are iterator which can generator values ONLY ONCE
# Generators generate values on the fly like range function is a generator in 'for item in range(10)'
#  
# How to create iterations easily using Python generators, how it is different from iterators and normal functions, and why you should use it.
# yeild is to generator values on the fly 

#%% unlike function we don't use return or print, we use yield instead

def myGenerator(myNumber):
    for i in range(myNumber):
        # return i
        # print(i)
        yield i

print(myGenerator)

# %%
g = myGenerator(10)
print(g)
# %% Let's run this now
g.__next__()
# %% again..n again..n again.. unit it runs out of the items and then it stops
g.__next__()
# %% for loop handles generators automatically

for i in g:
    print(i)

#%% remember how we could iterate strings but not integers?

for item in "Hello":
    print(item)

# It was possible because of string has method __iter__ and __getitem__ but int doesn't 

"Hello".__iter__
"Hello".__getitem__

#%% Using this knowledge we can generate it like this

myVariable = 'Hello'

myStrIter = iter(myVariable)

print(myStrIter.__next__())
print(myStrIter.__next__())
print(myStrIter.__next__())
print(myStrIter.__next__())
print(myStrIter.__next__())

# %%
