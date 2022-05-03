'''
Map, Filter, Reduce
===================
Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like loops and branching.

Essentially, these three functions allow you to apply a function across a number of iterables, in one fell swoop.

map and filter come built-in with Python (in the __builtins__ module) and require no importing. reduce, however, needs to be imported as it resides in the functools module. 

Map
The map() function in python has the following syntax:

map(func, *iterables)

'''
#%% Say I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase. Traditonally, in normal pythoning, I would do something like this:

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

#%% With map() functions, it's not only easier, but it's also much more flexible. I simply do this:

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# Note that using the defined map() syntax above, func in this case is str.upper and iterables is the my_pets list -- just one iterable. Also note that we did not call the str.upper function (doing this: str.upper()), as the map function does that for us on each element in the my_pets list.

# What's more important to note is that the str.upper function requires only one argument by definition and so we passed just one iterable to it. So, if the function you're passing requires two, or three, or n arguments, then you need to pass in two, three or n iterables to it. Let me clarify this with another example.

# Say I have a list of circle areas that I calculated somewhere, all in five decimal places. And I need to round each element in the list up to its position decimal places, meaning that I have to round up the first element in the list to one decimal place, the second element in the list to two decimal places, the third element in the list to three decimal places, etc. With map() this is a piece of cake. Let's see how.

# Python already blesses us with the round() built-in function that takes two arguments -- the number to round up and the number of decimal places to round the number up to. So, since the function requires two arguments, we need to pass in two iterables.
#%%
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)

# The range(1, 7) function acts as the second argument to the round function (the number of required decimal places per iteration). So as map iterates through circle_areas, during the first iteration, the first element of circle_areas, 3.56773 is passed along with the first element of range(1,7), 1 to round, making it effectively become round(3.56773, 1). During the second iteration, the second element of circle_areas, 5.57668 along with the second element of range(1,7), 2 is passed to round making it translate to round(5.57668, 2). This happens until the end of the circle_areas list is reached.

#%% "What if I pass in an iterable less than or more than the length of the first iterable? That is, what if I pass range(1, 3) or range(1, 9999) as the second iterable in the above function". And the answer is simple: nothing! Okay, that's not true. "Nothing" happens in the sense that the map() function will not raise any exception, it will simply iterate over the elements until it can't find a second argument to the function, at which point it simply stops and returns the result.

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 3)))

print(result)

#%% The same thing happens if circle_areas is less than the length of the second iterable. Python simply stops when it can't find the next element in one of the iterables.

# To consolidate our knowledge of the map() function, we are going to use it to implement our own custom zip() function. The zip() function is a function that takes a number of iterables and then creates a tuple containing each of the elements in the iterables. Like map(), in Python 3, it returns a generator object, which can be easily converted to a list by calling the built-in list function on it. Use the below interpreter session to get a grip of zip() before we create ours with map()

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))

print(results)

#%% As a bonus, can you guess what would happen in the above session if my_strings and my_numbers are not of the same length? No? try it! Change the length of one of them.

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

# Just look at that! We have the same result as zip.

# Did you also notice that I didn't even need to create a function using the def my_function() standard way? That's how flexible map(), and Python in general, is! I simply used a lambda function. This is not to say that using the standard function definition method (of def function_name()) isn't allowed, it still is. I simply preferred to write less code (be "Pythonic").
