# Type Conversion
# The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.

# 1- Implicit Type Conversion
# 2- Explicit Type Conversion

'''
Key Points to Remember
============================
1- Type Conversion is the conversion of object from one data type to another data type.
2- Implicit Type Conversion is automatically performed by the Python interpreter.
3- Python avoids the loss of data in Implicit Type Conversion.
4- Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
5- In Type Casting, loss of data may occur as we enforce the object to a specific data type.
'''

# Implicit Type Conversion
# ================================
#%% Example 1: Converting integer to float
num_int = 123
num_flo = 123.565

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

# Now, let's try adding a string and an integer, and see how Python deals with it.

#%% Example 2: Addition of string(higher) data type and integer(lower) datatype

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str:", type(num_str))

print(num_int+num_str)

# Explicit Type Conversion ( a.k.a Type casting)
# =============================
# Syntax : <required_datatype>(expression)

print(num_int+int(num_str))

#%% If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
print(x)

y = int(3)    # y will be 3
print(y)

z = float(3)  # z will be 3.0
print(z)


#%% Example 3: Addition of string and integer using explicit conversion
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))


#%% Here is a simple program showing when you might want to use this technique.
def multiply():
    numstr1 = input("Enter a number: ")
    numstr2 = input("Enter another number: ")

    print(type(numstr1))
    print(type(numstr2))

    num1 = float(numstr1)
    num2 = float(numstr2)
    
    print("Their product is ", num1 * num2)
    print("Won't work: ", numstr1 * numstr2)

#%% Let's run multiply()
multiply()

