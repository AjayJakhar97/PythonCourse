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

# %%
