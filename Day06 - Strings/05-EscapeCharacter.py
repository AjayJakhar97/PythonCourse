#%% To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

#%% Escape characters used in Python:
'''
Code	Result
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''

#%% \'	Single Quote
txt = 'It\'s alright.'
print(txt) 

#%% \\	Backslash
txt = "This will insert one \\ (backslash) and this will insert two \\\\ (backslashes) ."
print(txt) 

#%% \n	New Line
txt = "Hello\nWorld!"
print(txt)

#%% \r	Carriage Return	
txt = "Hello\rWorld!"
print(txt)

string = 'I did an awesome job on that project. \r and you did '
print(string)

#%% \t	Tab	
txt = "Hello\tWorld!"
print(txt)

txt = "Hello\t\tWorld!"
print(txt)

#%% erases one character (backspace):
txt = "Hello World!"
print(txt)

txt = "Hello \bWorld!"
print(txt)

txt = "Hello \b\bWorld!"
print(txt)

txt = "Hello \b\b World!"
print(txt)

#%% \f	Form Feed
txt = "Hello \fWorld!"
print(txt)

#%% \ooo	Octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110"
print(txt)

txt = "\110\145\154\154\157"
print(txt)

txt = "\112"
print(txt)

#%% \xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# %%
