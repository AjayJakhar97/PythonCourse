'''
The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops.

class range(stop)
class range(start, stop[, step])

++ The arguments to the range constructor must be integers. 
++ If the step argument is omitted, it defaults to 1. 
++ If the start argument is omitted, it defaults to 0. 
++ If step is zero, ValueError is raised.
++ The contents of a range r are determined by the formula r[i] = start + step*i

'''
#%% list(range(10))
list(range(10))
# %% list(range(1, 11))
list(range(1, 11))
# %% list(range(0, 30, 5))
list(range(0, 30, 5))
# %% list(range(0, 10, 3))
list(range(0, 10, 3))
# %% list(range(0, -10, -1))
list(range(0, -10, -1))
# %% list(range(0))
list(range(0))
# %% list(range(1, 0))
list(range(1, 0))
# %%
s = range(0, 20, 2)
print(list(s))

# Range objects implement the collections.abc.Sequence ABC, and provide features such as 
# 1- containment tests
#%% Does below number exist in the range?
print(11 in s)
print(11 not in s)
#%% Let's test when something is present in the range
print(10 in s)

#%% 2- element index lookup
print(s.index(10))
print(s[5])
#%% 3- slicing
print(list(s[:5]))
print(list(s[1:5]))
print(list(s[1:5:2]))

#%% 4- support for negative indices
print(s[-1])

#%% 5- length of s
len(s)

#%% smallest item of s
min(s)
#%% largest item of s
max(s)

#%% index of the first occurrence of x in s (at or after index i and before index j)
# s.index(x[, i[, j]])
# s.index(6,0,9) # This fails so try s[i:j].index(x)
s[0:9].index(6)

#%% index raises ValueError when x is not found in s
print(s.index(11))

#%% total number of occurrences of x in s
s.count(6)

# Testing range objects for equality with == and != compares them as sequences. 
# That is, two range objects are considered equal if they represent the same sequence of values. 

# %% Example 1
print(list(range(0, 3, 2)))
print(list(range(0, 4, 2)))
range(0, 3, 2) == range(0, 4, 2)

# %% Example 2
range(0) == range(2, 1, 3)

# %% Example 3
range(0) != range(2, 1, 3)

#%% Define ‘==’ and ‘!=’ to compare range objects based on the sequence of values they define (instead of comparing based on object identity)
var1 = range(2, 1, 3)
var2 = range(0)
print(id(var1))
print(id(var2))
var1 == var2

# The + (concatenation) and * (repetition) operations are not support by range sequence  (due to the fact that range objects can only represent sequences that follow a strict pattern and repetition and concatenation will usually violate that pattern).
#%% Let's check by creating below ranges
myVar1 = range(10)
myVar2 = range(5)
print(list(myVar1))
print(list(myVar2))
# %% + (concatenation)
var1 + var2
# %% * (repetition)
myVar1 * myVar2
# %%
print(list(myVar1[3:5]))

'''
The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).
'''

#%% Exercise - 

# Python program to print Fizz Buzz
 
# Loop for 100 times i.e. range
for fizzbuzz in range(1,100):
 
    # Number divisible by 15,(divisible
    # by both 3 & 5), print 'FizzBuzz'
    # in place of the number
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")                                        
        continue
 
    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif fizzbuzz % 3 == 0:    
        print("Fizz")                                        
        continue
 
    # Number divisible by 5,
    # print 'Buzz' in
    # place of the number
    elif fizzbuzz % 5 == 0:        
        print("Buzz")                                    
        continue
 
    # Print numbers
    print(fizzbuzz)