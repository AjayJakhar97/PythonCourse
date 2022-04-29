'''
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

===============
File Handling
===============
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

'''

# %% Syntax: To open a file for reading it is enough to specify the name of the file:

import os
f = open("demofile.txt")

# %% The code above is the same as:

f = open("demofile.txt", "rt")

# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# %% To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("demofile.txt", "r")
print(f.read())

# %% Read Only Parts of the File
# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))
# %% You can return one line by using the readline() method

f = open("demofile.txt", "r")
print(f.readline())

# %% Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# %% Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
    print(x)

# %% Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# %% Write to an Existing File

# Open the file "demofile2.txt" and append content to the file at the end:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# %% Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

# %% Open the file "demofile3.txt" and "x" - Create - will create a file, returns an error if the file exist

f = open("demofile3.txt", "x")
f.write("Woops! I have deleted the content!")
f.close()

# %% Delete a File
# Remove the file "demofile.txt":

os.remove("demofile.txt")

# %% Check if file exists, then delete it:

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# %% Remove the folder "myfolder":

os.rmdir("myfolder")

# Note: You can only remove empty folders.

# %% rename a file
# https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python

import os
os.rename('a.txt', 'b.kml')

#%% File may be inside a directory, in that case specify the path:

import os

directory = r'C:\Users\Administrator\Downloads\Class 7\English\HoneyComb'
print(os.path.exists(directory))

if os.path.exists(directory):

    old_file = os.path.join("directory", "a.txt")
    new_file = os.path.join("directory", "b.kml")
    os.rename(old_file, new_file)

    os.rename('a.txt', 'b.kml')

else:
    raise exception

#%%

'''
If you used below then you will get an issue

fileLocation = 'C:\Users\Administrator\Downloads\Class 7\English\HoneyComb'
print(os.path.exists)

  Input In [3]
    fileLocation = f'C:\Users\Administrator\Downloads\Class 7\English\HoneyComb'
                                                                                ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

==============
Explaination
==============

The problem is with the string

"C:\Users\Eric\Desktop\beeline.txt"
Here, \U in "C:\Users... starts an eight-character Unicode escape, such as \U00014321. In your code, the escape is followed by the character 's', which is invalid.

You either need to duplicate all backslashes:

"C:\\Users\\Eric\\Desktop\\beeline.txt"
Or prefix the string with r (to produce a raw string):

r"C:\Users\Eric\Desktop\beeline.txt"

'''

#%%  As of Python 3.4 one can use the pathlib module to solve this.


some_path = 'a/b/c/the_file.extension'
# So, you can take your path and create a Path object out of it:

from pathlib import Path
p = Path(some_path)

#%%


import os

directory = r'C:\Users\Administrator\Downloads\Class 7\English\HoneyComb'
print(os.path.exists(directory))

if os.path.exists(directory):
    os.walk(directory)

#%%

import os 
from os.path import join, getsize 
# for root, dirs, files in os.walk('python/Lib/email'):
directory = r'C:\Users\Administrator\Downloads\Class 7\English\HoneyComb'

for root, dirs, files in os.walk(directory):
    print(root, "consumes", end="") 
    print(sum(getsize(join(root, name)) for name in files), end="")
    print("bytes in", len(files), "non-directory files")
    if 'CVS' in dirs:
        dirs.remove('CVS') # don't visit CVS directories
    
    for name in files:
        print(name)

#%% How to list directory tree structure in python?

# You can use the os.walk() method to get the list of all children of path you want to display the tree of. Then you can join the paths and get the absolute path of each file.
# For example

import os
def tree_printer(root):
    for root, dirs, files in os.walk(root):
        for d in dirs:
            print(os.path.join(root, d)  )  
        for f in files:
            print(os.path.join(root, f))

tree_printer('.')
tree_printer(directory)


# %%
