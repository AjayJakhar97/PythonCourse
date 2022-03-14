'''
Python Iterators
===================
++ An iterator is an object that contains a countable number of values
++ An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
++ An iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()

'''
#%% Return an iterator from a tuple, and print each value

myTuple = ("apple","banana","cherry")
myIt = iter(myTuple)

# for i in range(len(myTuple)):
#     print(myIt.__next__())

for i in range(len(myTuple)):
    print(next(myIt))

# %% Strings are also iterable objects, containing a sequence of characters:
myStr = "apple"
myIt = iter(myStr)

# for i in range(len(myStr)):
#     print(myIt.__next__())

for i in range(len(myStr)):
    print(next(myStr))
# %% for loop to iterate through an iterable object:

myTuple = ("apple","banana","cherry")

for i in myTuple:
    print(i)

# %% Create an Iterator

class myClass:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

class1 = myClass()
myit = iter(class1)

print(next(myit))
print(next(myit))

# ++ To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# ++ The __iter__() method can do operations (initializing etc.), but must always return the iterator object itself
# ++ The __next__() method also allows you to do operations, and must return the next item in the sequence.

# %% StopIteration
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

# %% Let's iterate with for loop now
for item in myit:
    print(item)

#%% Using StopIteration below

class myClass:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration()

class1 = myClass()
myit = iter(class1)

print(next(myit))
print(next(myit))

# %% Let's iterate with for loop now
for item in myit:
    print(item)

# %%
