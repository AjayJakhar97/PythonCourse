'''
Reduce
reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument. It has the following syntax:

reduce(func, iterable[, initial])

Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is the optional value that gets placed before the elements of the iterable in the calculation, and serves as a default when the iterable is empty. 

The following should be noted about reduce(): 

1. func requires two arguments, the first of which is the first element in iterable (if initial is not supplied) and the second element in iterable. If initial is supplied, then it becomes the first argument to func and the first element in iterable becomes the second element. 
2. reduce "reduces" iterable into a single value.

'''
#%% Below custom_sum function returns the sum of all the items in the iterable passed to it.

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

'''
The result, as you'll expect is 68.

So, what happened?

As usual, it's all about iterations: reduce takes the first and second elements in numbers and passes them to custom_sum respectively. custom_sum computes their sum and returns it to reduce. reduce then takes that result and applies it as the first element to custom_sum and takes the next element (third) in numbers as the second element to custom_sum. It does this continuously (cumulatively) until numbers is exhausted.
'''
#%% Let's see what happens when I use the optional initial value.

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)

# The result, as you'll expect, is 78 because reduce, initially, uses 10 as the first argument to custom_sum.

#%% Exercise: In this exercise, you'll use each of map, filter, and reduce to fix broken code.

from functools import reduce 

# Use map to print the square of each numbers rounded to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]


#%% Solution
from functools import reduce 

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
