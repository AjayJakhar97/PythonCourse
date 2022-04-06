'''
++ A RegEx, or regular expressions can be defined as the sequence of characters which are used to search for a pattern in a string.
++ Python has a built-in package called "re" which provides regular expression operations.
++ The re module throws an exception if there is some error while using the regular expression.     

'''
# %% Import the re module
import re
import string

# %% The search() function searches the string for a match, and returns a Match object if there is a match. If there is more than one match, only the first occurrence of the match will be returned:

# ====================
# Metacharacters
# ====================
# Metacharacters are characters with a special meaning

# %% []	A set of characters.
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

txt = "Let's see if this works"
searchResult = re.search("[a-m]", txt)
print("Match found:", searchResult.group())

searchResult = re.findall("[a-m]", txt)
print("Match found:", searchResult)

# %% [arn]	Returns a match where one of the specified characters (a, r, or n) are present
txt = "learn it"
searchResult = re.findall("[arn]", txt)
print("Match found:", searchResult)

# %% [^arn]	Returns a match where none of the specified characters are present
txt = "learn it"
searchResult = re.findall("[^arn]", txt)
print("Match found:", searchResult)

# %% [a-z]	Returns a match where the character is a letter between a and z (both included)
txt = "learn it"
searchResult = re.findall("[a-e]", txt)
print("Match found:", searchResult)

# %% [^a-z]	Returns a match where the character is not a letter between a and z (both included)
txt = "learn it"
searchResult = re.findall("[^a-e]", txt)
print("Match found:", searchResult)

# %% [0123]  Returns a match where any of the specified digits (0, 1, 2, or 3) are present
txt = "learn it on 1st day or 2nd day"
searchResult = re.findall("[0123]", txt)
print("Match found:", searchResult)

# %% [^0123]	Returns a match where none of the specified digits are present
txt = "learn it on 1st day or 2nd day"
searchResult = re.findall("[^0123]", txt)
print("Match found:", searchResult)

# %% [0-9]	Returns a match where the character is a digit between 0 and 9 (both included)
txt = "learn it on 1st day or 2nd day"
searchResult = re.findall("[0-9]", txt)
print("Match found:", searchResult)

# %% [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
txt = "007 is the code. Not 58 or 59 or 60"
searchResult = re.findall("[0-5][0-9]", txt)
print("Match found:", searchResult)

# %% [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
txt = "2 + 2 = 4"
searchResult = re.findall("[+]", txt)
print("Match found:", searchResult)

# %% [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
txt = "007 is the code. Not 58 or 59 or 60"
searchResult = re.findall("[a-zA-Z]", txt)
print("Match found:", searchResult)

# %% .     Any character (except newline character)
txt = "Let's see if this works"
searchResult = re.findall(".", txt)
print("Match found:", searchResult)

# %% ^     Starts with
txt = "Let's see if this works"
searchResult = re.findall("^L", txt)
print("Match found:", searchResult)

# %% $     Ends with
txt = "Let's see if this works"
searchResult = re.findall("s$", txt)
print("Match found:", searchResult)

# %% *     Zero or more occurrences
txt = "Let's see if this works"
searchResult = re.findall("s*", txt)
print("Match found:", searchResult)

# %% +     One or more occurrences
txt = "Let's see if this works"
searchResult = re.findall("s+", txt)
print("Match found:", searchResult)

# %% ?     zero or one occurrence
txt = "Let's see if this works"
searchResult = re.findall("s?", txt)
print("Match found:", searchResult)

# %% {m}	Exactly m occurrences
txt = "Let's see if this works"
searchResult = re.findall("t.{2}s", txt)
print("Match found:", searchResult) if searchResult else print("No match found")

# %% |    Either or
txt = "Let's see if this works"
searchResult = re.findall("t|s", txt)
print("Match found:", searchResult) if searchResult else print("No match found")

# ====================
# Special Sequences
# ====================
# %% Use \ to escape special characters in a string
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# %% \A     Returns a match if the specified characters are at the beginning of the string
txt = "Hello World"
searchResult = re.search("\AHello", txt)
print("Match found:", searchResult.group()
      ) if searchResult else print("No match found")

# %% \b	Returns a match where the specified characters are at the beginning or at the end of a word
txt = "Hello World"
searchResult = re.search(r"\bWorld", txt)
print("Match found:", searchResult.group()
      ) if searchResult else print("No match found")

# %% \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
txt = "Hello World"
# searchResult = re.search(r"\BWorld", txt)
searchResult = re.search(r"\Borld", txt)
print("Match found:", searchResult.group()
      ) if searchResult else print("No match found")

# %% \d	Any numeric digit from 0 to 9
txt = "King of 5 countries"
# txt = "King of 05 countries"
searchResult = re.search("\d", txt)
print("Match found:", searchResult.group()
      ) if searchResult else print("No match found")

# %% \D	Any character that is not a numeric digit from 0 to 9

txt = "My-05-countries"
searchResult = re.findall("\D", txt)
print("Match found:", searchResult) if searchResult else print("No match found")

# %% \s	Any space, tab, or newline character
txt = "Hello World"
searchResult = re.search("\s", txt)
print(searchResult)
print("Match found:", searchResult.group()
      ) if searchResult else print("No match found")

# %% Let's try to find all here from this list of texts.
myList = ["Hi", "Hello World", "Hello  World", "Hello\nWorld"]

for i in range(len(myList)):
    print(i+1, "-", myList[i])
    searchResult = re.search("\s", myList[i])
    # print(searchResult)
    print("Match found:", searchResult.group()
          ) if searchResult else print("No match found")

# %% \S	Any non-whitespace character
txt = "Hello World"
searchResult = re.findall("\S", txt)
print(searchResult)
print("Match found:", searchResult) if searchResult else print("No match found")

# %% \w	Any word character [a-zA-Z0-9_]
txt = "Hello2022@World.com"
searchResult = re.findall("\w", txt)
print(searchResult)
print("Match found:", searchResult) if searchResult else print("No match found")

# %% \W	Any non-word character [^a-zA-Z0-9_]
txt = "Hello2022@World.com"
searchResult = re.findall("\W", txt)
print(searchResult)
print("Match found:", searchResult) if searchResult else print("No match found")

# %% \Z	Returns a match where the specified characters are at the end of string
txt = "Hello World"
searchResult = re.search(r"ld\Z", txt)
# searchResult = re.search(r"l\Z", txt)
print("Match found:", searchResult.group()
      ) if searchResult else print("No match found")

# ================
# RegEx Functions
# ================

# %% split - Splits the string at the positions where the pattern matches
txt = "The rain in Spain"
# You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", txt)
# This will only split the string at the first space, and return only "The"
x = re.split("\s", txt, 1)
print(x)

# %% sub - Replaces the matched pattern in the string with a new pattern
txt = "The rain in Spain"
# This will replace all the white-space characters with the number 9
x = re.sub("\s", "9", txt)
# This will only replace the first two white-space characters with the number 9
x = re.sub("\s", "9", txt, 2)
print(x)

# %% subn - Returns a tuple containing the original string and the number of replacements made
txt = "The rain in Spain"
# This will replace all the white-space characters with the number 9
x = re.subn("\s", "9", txt)
print(x)

# %% compile - Compiles the pattern into a regular expression object
pattern = re.compile("\d")
txt = "The rain in Spain in 1970"
x = re.findall(pattern, txt)
print(x)

# %% search - Once match is found, you can use the start() and end() methods to find the position of the match:
txt = "The rain in Spain in 1970"
searchResult = re.search("9+", txt)
print(searchResult.start())
print(searchResult.end())

# %% finditer - Returns an iterator yielding Match objects over all non-overlapping matches for the RE pattern in the string
myText = "Hello Hello"
var = re.finditer("Hello", myText)
for match in var:
    print(match.group())

# %%
# ================================
# Match object's properties
# ================================
'''
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
'''

txt = "Let's see if this works"
searchResult = re.search("w+", txt)
# searchResult = re.search("s+", txt)

print(searchResult.span())
print(searchResult.string)
print(searchResult.group())


# %% Task 1 : Create a function that replaces a substring with another substring at a specified position
'''
use simple function, which lists all occurrences, picks the nth one's position and uses it to split original string into two substrings. Then it replaces first occurrence in the second substring and joins substrings back into the new string:

# You need to know below for that

1- Re module
2- Re finditer function
'''

def replace_Nth(myText,n):
      import re
      var = re.finditer("Hello", myText)
            # for match in var:
            #       print(match.group())

      where = [match.start() for match in var]
      #     print(where[1])
      where = where[n-1]
      before = myText[:where]
      #     print(before)
      after = myText[where:]
      #     print(after)
      after = after.replace("Hello", "Hi", 1)
      newString = before + after
      return newString

myText = "Hello Hello"
result = replace_Nth(myText,2)
print(result)
