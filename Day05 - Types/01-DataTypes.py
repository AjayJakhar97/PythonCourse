#%% You can get the data type of a variable with the type() function

x = 5
y = "John"
print(type(x))
print(type(y))

# Setting the Data Type

#%% Text type
x = "Hello World"  # Data Type : str

#%% Numeric types
x = 20  # Data Type : int	; Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length
# Data Type : float	; Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 20.5
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
# Data Type : complex	; Complex numbers are written with a "j" as the imaginary part:
x = 1j
# real number + Complex numbers are written with a "j" as the imaginary part:
x = 3+5j

#%% Sequence Types
x = ["apple", "banana", "cherry"]  # Data Type : list
x = ("apple", "banana", "cherry")  # Data Type : tuple
x = range(6)  # Data Type : range

#%% Mapping Type
x = {"name": "John", "age": 36}  # Data Type : dict

y = {
    "name": "John",
    "age": 36
}


#%% Set Types
x = {"apple", "banana", "cherry"}  # Data Type : set
y = frozenset({"apple", "banana", "cherry"})  # Data Type : frozenset

#%% Boolean Type
x = True  # Data Type : bool

#%% Binary Types
x = b"Hello"  # Data Type : bytes
print(type(x))

y = bytearray(5)  # Data Type : bytearray
print(type(y))

z = memoryview(bytes(5))  # Data Type : memoryview
print(type(z))

#%% If you want to specify the data type, you can use the following constructor functions

x = str("Hello World")		# Data Type : str
x = int(20)		# Data Type : int
x = float(20.5)		# Data Type : float
x = complex(1j)		# Data Type : complex
x = list(("apple", "banana", "cherry"))		# Data Type : list
x = tuple(("apple", "banana", "cherry"))		# Data Type : tuple
x = range(6)		# Data Type : range
x = dict(name="John", age=36)		# Data Type : dict
x = set(("apple", "banana", "cherry"))		# Data Type : set
x = frozenset(("apple", "banana", "cherry"))		# Data Type : frozenset
x = bool(5)		# Data Type : bool
x = bytes(5)		# Data Type : bytes
x = bytearray(5)		# Data Type : bytearray
x = memoryview(bytes(5))		# Data Type : memoryview

#%% Please note: Bool 0 is "False" and every other number is True

test1 = bool(0)
print("test1 = ", test1)

test2 = bool(1)
print("test2 = ", test2)

test3 = bool(2)
print("test3 = ", test3)
