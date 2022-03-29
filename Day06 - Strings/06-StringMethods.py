# Python has a set of built-in methods that you can use on strings.

'''
Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''

#%% capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
txt = "python is FUN!"
x = txt.capitalize()
print (x)

# See what happens if the first character is a number
txt = "36 is my age."
x = txt.capitalize()
print (x)

#%% casefold()	Converts string into lower case
'''
Purely ASCII Text -> lower()
Unicode text/user input -> casefold()

Casefolding is a more aggressive version of lower() that is set up to make many of the more unique unicode characters more comparable. It is another form of normalizing text that may initially appear to be very different, but it takes characters of many different languages into account

Casefolding is more effective when comparing two strings

'''

txt = "Hello, And Welcome To My World!"

x = txt.casefold()
y = txt.lower()
print(x)
print(y)

german = 'ß'
print(german.lower())
print(german.casefold())


#%% center()	Returns a centered string
txt = "Hello, And Welcome To My World!"
x = txt.center(20)  # padding value
print(x)

# here you will see the difference. We are saying take 20 letter space and put banana in the center of it. The space will include the space taken by the string thus you don't see the difference in above line

txt = "banana"
x = txt.center(20)
print(x)
       banana       

#%% count()	Returns the number of times a specified value occurs in a string

txt = "I love apple . Apple is my favorite fruit"

x = txt.count("apple")
print(x)

# string.count(value, start, end)

# Search from position 10 to 24:

txt = "I love apple , apple are my favorite fruit"

x = txt.count("apple", 8, 24)
# pple , apple are my favorite fruit

print(x)

x = txt.count("apple", 7, 24)
# apple , apple are my favorite fruit
print(x)


#%% encode()	Returns an encoded version of the string
txt = "My name is Ståle"

x = txt.encode()
print(txt)
print(x)

#%% if you want to raise error when not able to encode a string use. Default, raises an error on failure
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="strict"))

#%% string.encode(encoding=encoding, errors=errors)
txt = "My name is Ståle"

# uses a backslash instead of the character that could not be encoded
print(txt.encode(encoding="ascii",errors="backslashreplace"))

# ignores the characters that cannot be encoded
print(txt.encode(encoding="ascii",errors="ignore"))

# replaces the character with a text explaining the character
print(txt.encode(encoding="ascii",errors="namereplace"))

# replaces the character with a questionmark
print(txt.encode(encoding="ascii",errors="replace"))

# replaces the character with an xml character
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#%% endswith()	Returns true if the string ends with the specified value

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# string.endswith(value, start, end)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

#%% expandtabs()	Sets the tab size of the string
# string.expandtabs(tabsize)

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(6))
print(txt.expandtabs(8))   # this is default \t tab size
print(txt.expandtabs(10))

#%% find()	Searches the string for first occurrence of a specified value and returns the position of where it was found
# string.find(value, start, end)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
x = txt.index("welcome")
print(x)


txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# Note: The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found and find() returns -1


txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))

#%% format()	Formats specified values in a string
# Reference : https://docs.python.org/3/library/string.html

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

# Formatting Types
# Inside the placeholders you can add a formatting type to format the result:

#   :<		Left aligns the result (within the available space)

txt = "We have {:<8} chickens."
print(txt.format(49))


#   :>		Right aligns the result (within the available space)

txt = "We have {:>8} chickens."
print(txt.format(49))

#   :^		Center aligns the result (within the available space)

txt = "We have {:^8} chickens."
print(txt.format(49))

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."
print(txt.format(13800000000))

#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "c" to convert the value into the corresponding unicode character

txt = "The binary version of {0} is {0:c}"
print(txt.format(65))
txt = "The binary version of {0} is {0:c}"
print(txt.format(66))
txt = "The binary version of {0} is {0:c}"
print(txt.format(64))

#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))

#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))

#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')
y = float('nan')
z = float(12)

txt = "The price is {:F} dollars."
print(txt.format(x))
print(txt.format(y))
print(txt.format(z))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))
print(txt.format(y))
print(txt.format(z))

#%% 
from decimal import *

getcontext()
getcontext().prec = 7
txt = "We have {:g} chickens."
print(txt.format(564646546464646))

txt = "We have {:G} chickens."
print(txt.format(564646546464646))

#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(564646546464646))

#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(564646546464646))

#%% format_map()	Formats specified values in a string
point = {'x':4,'y':-5}
print('{x} {y}'.format(**point)) # str.format(**mapping)

point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

# How format_map() works with dict subclass?

class Coordinate(dict):
    def __missing__(self, key):
      return key

print('({x}, {y})'.format_map(Coordinate(x='6')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))

# Conclusion: format_map(mapping) is more flexible than format(**mapping) as you can have missing keys.


#%% index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
print(txt.index(","))
print(txt.index("e", 5, 10))
print(txt.index("q"))

#%% isalnum()	Returns True if all characters in the string are alphanumeric

txt = "#"
print(txt.isalnum())
txt = "12"
print(txt.isalnum())
txt = "Company"
print(txt.isalnum())
txt = "Company12"
print(txt.isalnum())

#%% isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
print(txt.isalpha())

txt = "Company12"
print(txt.isalpha())

#%% isascii()	Returns True if all characters in the string are ascii characters

#%% isdecimal() method returns True if all the characters are decimals (0-9)
txt = "\u0033" #unicode for 3
print(txt.isdecimal())

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

#%% isdigit()	Returns True if all characters in the string are digits
txt = "50800"
print(txt.isdigit())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "\u0072" #unicode for r

print(a.isdigit())
print(b.isdigit())
print(c.isdigit())

print(u'{0}'.format(a))
print(u'{0}'.format(b))
print(u'{0}'.format(c))


#%% isidentifier()	Returns True if the string is an identifier
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

print("Demo".isidentifier())

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#%% islower()	Returns True if all characters in the string are lower case
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

#%% isnumeric()	Returns True if all characters in the string are numeric
txt = "123456"
print(txt.isnumeric())

#%% isprintable()	Returns True if all characters in the string are printable

txt = "123456"
print(txt.isprintable())

german = 'ß'
print(german.isprintable())

txt = 'This is my brother\'s bike'
print(txt.isprintable())

txt = 'Hello\n World'
print(txt.isprintable())

#%% isspace()	Returns True if all characters in the string are whitespaces

#%% istitle()	Returns True if the string follows the rules of a title

#%% isupper()	Returns True if all characters in the string are upper case

#%% join()	Converts the elements of an iterable into a string

#%% ljust()	Returns a left justified version of the string

#%% lower()	Converts a string into lower case

#%% lstrip()	Returns a left trim version of the string

#%% maketrans()	Returns a translation table to be used in translations

#%% partition()	Returns a tuple where the string is parted into three parts

#%% replace()	Returns a string where a specified value is replaced with a specified value

#%% rfind()	Searches the string for a specified value and returns the last position of where it was found

#%% rindex()	Searches the string for a specified value and returns the last position of where it was found

#%% rjust()	Returns a right justified version of the string

#%% rpartition()	Returns a tuple where the string is parted into three parts

#%% rsplit()	Splits the string at the specified separator, and returns a list

#%% rstrip()	Returns a right trim version of the string

#%% split()	Splits the string at the specified separator, and returns a list

#%% splitlines()	Splits the string at line breaks and returns a list

#%% startswith()	Returns true if the string starts with the specified value

#%% strip()	Returns a trimmed version of the string

#%% swapcase()	Swaps cases, lower case becomes upper case and vice versa

#%% title()	Converts the first character of each word to upper case

#%% translate()	Returns a translated string

#%% upper()	Converts a string into upper case

#%% zfill()	Fills the string with a specified number of 0 values at the beginning
