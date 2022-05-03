# Python Generators
# ===================
# Let's get some terminology right first...

# Iterable - An object with method __iter__ or __getitem__ which creates iterator
# Iterator - Iterators has mehod __next__() and it helps to get next item
# Iteration -  It is the process of iterating items

# Generators are iterator which can generator values ONLY ONCE
# Generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.
# When an iteration over a set of item starts using the for statement, the generator is run. 
# Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. 
# The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

#%% unlike function we don't use return or print, we use yield instead

def myGenerator(myNumber):
    for i in range(myNumber):
        # return i
        # print(i)
        yield i

myGeneratorObject = myGenerator(10)
print(myGeneratorObject)

# %%
import inspect
print(inspect.isgenerator(myGeneratorObject))
print(inspect.isgenerator(myGenerator(10)))

# %% Let's run this now
myGeneratorObject.__next__()
# %% again..n again..n again.. unit it runs out of the items and then it stops
myGeneratorObject.__next__()
# %% for loop handles generators automatically

for i in myGeneratorObject:
    print(i)

#%% Another example 
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

print(inspect.isgenerator(lottery()))

for random_number in lottery():
    print("And the next number is... %d!" %(random_number))

#%% Exercise : Write a generator function which returns the Fibonacci series

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break

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

#%% Let's have a look at another example

def Searcher():
    import time
    Greetings = "Hello World, How are you all doing ?"
    
    # Below is Optional: I am giving it time to read something...
    time.sleep(5)

    while True:
        txt = yield
        if txt in Greetings:
            print('present...')
        else:
            print('Not present')

mySearch = Searcher()

#%%
print(mySearch)
#%% check the type
print(type(mySearch))

#%% 
'''
next(iterator[, default])
Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

Also, can't send non-None value to a just-started generator
'''
# next(mySearch)
mySearch.send(None)
mySearch.send('hey')

#%% You can continue to send it until closed

mySearch.send('World')
mySearch.send('you')

#%% Now let's close it 
mySearch.close()

#%% Now you can't send it anymore can continue to send it until closed

mySearch.send('World')
mySearch.send('you')

#%%
import inspect

print(inspect.iscoroutine(mySearch))
print(inspect.isgenerator(mySearch))
