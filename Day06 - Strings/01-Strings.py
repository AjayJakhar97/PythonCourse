#%% Strings in python are surrounded by either single quotation marks, or double quotation marks.
# You can display a string literal with the print() function
print('Hello World')
print("Hello World")

# Strings in Python are arrays of bytes representing unicode characters
# An array is a collection of items stored at contiguous memory locations
#%% Let's check if this is true
for i in "Hello World":
  print(i)

print(list("Hello World"))

#%% It is not true for int and it will fail with TypeError: 'int' object is not iterable
print(list(123456789))

#%% OK. What is Unicode and ASCII
'''Unicode is an International character encoding standard that includes different languages, scripts and symbols. Each letter, digit or symbol has its own unique Unicode value. Unicode is an extension of ASCII that allows many more characters to be represented
https://en.wikipedia.org/wiki/List_of_Unicode_characters

ASCII is a 7-bit character set containing 128 characters. It contains the znumbers from 0-9, the upper and lower case English letters from A to Z, and some special characters. The character sets used in modern computers, in HTML, and on the Internet, are all based on ASCII.

What is the difference between UTF-8 and Unicode?
https://stackoverflow.com/questions/643694/what-is-the-difference-between-utf-8-and-unicode

'''


#%% convert Dec to binary
'''
+---------+--------+--------+----------------+
|    Bin. |   Hex. |   Dec. | ASCII Symbol   |
+=========+========+========+================+
| 1000001 |     41 |     65 | A              |
+---------+--------+--------+----------------+
| 1000010 |     42 |     66 | B              |
+---------+--------+--------+----------------+
'''
myVariable = 65

print(bin(myVariable))

print(bin(myVariable).replace('0b', ''))
myVariable = 66
print(bin(myVariable))
print(bin(myVariable).replace('0b', ''))

# Python does not have a character data type, a single character is simply a string with a length of 1
# Square brackets can be used to access elements of the string. Check the example below
#%% Get the character at position 1 (remember that the first character has the position 0)
a = "Hello, World!"
print(a[1])   

#%% Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)

#%% The len() function returns the length of a string
a = "Hello, World!"
print(len(a))

#%% To check if a certain phrase or character is present in a string a.k.a. Containment Testing
txt = "The best things in life are free!"
print("free" in txt)
print("Free" in txt)

#%% Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#%% To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# %%

