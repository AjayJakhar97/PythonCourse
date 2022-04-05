#%% Upper and Lower Case
myVariable = "Hello, World!"

print(myVariable.upper())
print(myVariable.lower())

# %% The strip() method removes any whitespace from the beginning or the end:
myVariable = "        Hello, World!   "
print(myVariable.strip())

# %% Replace String
myVariable = "Hello, World! Hello Hello Hello ...."
print(myVariable.replace("Hello", "Hi",1))
print(myVariable.replace("Hello", "Hi",-1))
print(myVariable.replace("Hello", "Hi",-2))

#%%
myText = "Hello Hello Hello Hello"

# To replace specific number of matches
print(myText.replace("Hello", "Hi",1))
print(myText.replace("Hello", "Hi",2))

# To replace all the occurrences of a substring
print(myText.replace("Hello", "Hi"))
print(myText.replace("Hello", "Hi",-1))

#%% Task : Replace nth occurrence of substring in string
'''
inbuilt function replace() replaces all or specific number of occurrences of a substring
How do we replace a specific occurrence of a substring in a string?

You need to know below two things to solve this problem:

1- str.find(sub[, start[, end]])
2- while loop

'''
#%% Solution : You can use a while loop with str.find to find the nth occurrence if it exists and use that position to create the new string

def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

myText = "Hello Hello Hello Hello"
nth_repl(myText, "Hello", "Hi", 2)

# %%
myText = "Hello World. I like to say Hello and not Hi"

nth_repl(myText, "Hello", "Hi", 2)

# %% The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
print(a.split("!"))  # returns ['Hello, World', '']
print(a.split("o"))  # returns ['Hello, World', '']
