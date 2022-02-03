# Python Bitwise Operators :: Bitwise operators act on bits and perform the bit-by-bit operations. These are used to operate on binary numbers.
# ==============================

'''
Operator	Description	Syntax
&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<
'''

#%% 
# Examples of Bitwise operators
a = 10
b = 4
# print(f"{a} in binary :",format(a,"b"))
# print(f"{b} in binary :",format(b,"b"))

# Print bitwise AND operation
print(a & b)
# print(format(a & b,"b"))

# Print bitwise OR operation
print(a | b)
# print(format(a | b,"b"))

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print(format(a ^ b,"b"))
# print(int('1110',2))

# print bitwise right shift operation
print(a >> 2)

# a = 10      #  1010
# x = a >> 2  #  0010
# print(x)    #  2
#             #  0010

# print(format(2, "b"))
# print(int('0010',2))

# print bitwise left shift operation
print(a << 2)

# a = 10      #  1010
# x = a << 2  #  101000
# print(x)    #  40
#             #  101000

# print(format(40, "b"))
# print(int('101000',2))

# %%
