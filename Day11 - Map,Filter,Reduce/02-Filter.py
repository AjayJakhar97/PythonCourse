'''
Filter
While map() passes each element in the iterable through a function and returns the result of all elements having passed through the function, filter(), first of all, requires the function to return boolean values (true or false) and then passes each element in the iterable through the function, "filtering" away those that are false. It has the following syntax:

filter(func, iterable)

The following points are to be noted regarding filter():

++ Unlike map(), only one iterable is required.
++ The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
++ filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".

'''
#%% Here are scores of 10 students. Let's filter out those who passed with scores more than 75...using filter.
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    # returns True if score is more than 75 else false
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

#%% The next example will be a palindrome detector. A "palindrome" is a word, phrase, or sequence that reads the same backwards as forwards. Let's filter out words that are palindromes from a tuple (iterable) of suspected palindromes.

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# 'demigod'[::-1] will return 'dogimed'
palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
