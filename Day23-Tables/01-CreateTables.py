# How to easily draw tables in terminal/console applications
# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data/26937531#26937531

'''
1- Tabulate : pip install tabulate

2- Prettytable : pip install prettytable

3- Texttable : pip install texttable

4- Termtables : pip install termtables

5- Terminaltables : pip install terminaltables
  Easily draw tables in terminal/console applications from a list of lists of strings. Supports multi-line rows.
  https://pypi.org/project/terminaltables/

6- Beautifultable : pip install beautifultable
  Full support for colors using ANSI sequences or any library of your choice. It just works
  https://pypi.org/project/beautifultable/

7 - Pandas : pip install pandas
  pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
  https://pandas.pydata.org/docs/getting_started/index.html#getting-started
  
'''

# Let's create a table to show ASCII representation in binary, Hex and Dec
#%% Method 1: Using Tabulate module

from tabulate import tabulate

myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]

myData = [
  ["1000001", 41, 65, "A"],
  ["1000010", 42, 66, "B"]
]

print(tabulate(myData, headers=myHeader, tablefmt="grid"))

#%% Method 2: Using PrettyTable module

from prettytable import PrettyTable

myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]

myTable = PrettyTable(myHeader)
myTable.add_row(["1000001", 41, 65, "A"])
myTable.add_row(["1000010", 42, 66, "B"])

print(myTable)

# %% Method 3: Using texttable module

from texttable import Texttable 

myTable = Texttable()
myTable.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
print(myTable.draw())

# %% Method 4: Using termtables module

import termtables

myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]

myData = [
  ["1000001", 41, 65, "A"],
  ["1000010", 42, 66, "B"]
]

myTable = termtables.to_string(myData,myHeader)
# myTable = termtables.to_string(myData,myHeader,alignment="l", padding=(0, 1), style=termtables.styles.thin_double)
print(myTable)

# %% Method 5: Using terminaltables

from terminaltables import AsciiTable

myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]
myData = [
  myHeader,
  ["1000001", 41, 65, "A"],
  ["1000010", 42, 66, "B"]
]

myTable = AsciiTable(myData,title="My table")
myTable.justify_columns[3]='right'
print(myTable.table)

# %% Method 6: Using beautifultable

from beautifultable import BeautifulTable
from termcolor import colored

myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]

myTable = BeautifulTable()
myTable.rows.append(["1000001", 41, 65, "A"])
myTable.rows.append([colored("1000010",'red'), 42, 66, colored("B",'blue')])
myTable.columns.header = myHeader
print(myTable)

# %% Method 7 : Using pandas
import pandas
myIndex = [1,2]
myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]
myData = [
  ["1000001", 41, 65, "A"],
  ["1000010", 42, 66, "B"]
]

pandas.DataFrame(myData,columns=myHeader,index=myIndex)

# %% using str.format() and the Format Specification Mini-Language.
# https://docs.python.org/3/library/stdtypes.html#str.format
# https://docs.python.org/3/library/string.html#formatspec

myHeader = [
  "Bin.","Hex.","Dec.","ASCII Symbol"
]
myData = [
  ["1000001", 41, 65, "A"],
  ["1000010", 42, 66, "B"]
]

row_format ="{:>10}" * (len(myHeader) + 1)
print(row_format.format('',*myHeader))
for item in myData:
  print(row_format.format('',*item))

# %%
'''
one day each 20 to 23
======================
numPy
sciPy
matplotlib
pandas


Remove "Re"
Day 8 - venv - virtual environment

Day 17 before day 11

'''