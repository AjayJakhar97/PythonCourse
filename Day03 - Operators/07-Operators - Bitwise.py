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

#%% Convert int 40 to binary
print(format(6, "b"))

#%% Convert binary 1110 to an int 
print(int('0110',2))

#%% Let's have a look at binary numbers and try to see a pattern

for i in range(21):
    print(f"{i} = ",{format(i,"b")})

#%% How to convert number to binary manually
# https://www.rapidtables.com/convert/number/decimal-to-binary.html

#%% Examples of Bitwise operators
a = 10
b = 4
print(f"{a} in binary :",format(a,"b"))
print(f"{b} in binary :",format(b,"b"))

#%% Print bitwise AND operation
'''
10 in binary : 1010
4 in binary  : 0100
======================
a & b        : 0000
======================
'''
#%%
# 1010
# 0100
# ======
# 0000
# ======

print(a & b)

#%% Print bitwise OR operation
print(a | b)

# 1010
# 0100
# ======
# 1110
# ======

'''
01
11
====
11
===
'''

# Convert int 40 to binary
print(format(14, "b"))

#%% Print bitwise NOT operation
# ~   NOT : Inverts all the bits
print(format(5, "b"))
x = 5  # 101 in binary
x = ~x # -x-1 = -(101 + 001) = -(110) = -6

'''
101
001
=====
001
=====

~001 = 110
opposite (Inverts or One's complement ) of 001 is 110

'''

print(x)
print(int('110',2))

#%% print bitwise XOR operation
a = 10
b = 6

# 1010
# 0110
# ======
# 1100
# ======

# print(a ^ b)
result = a ^ b
print("XOR result ",end=str(result))
print()
print(f"{result} in binary :",format(result,"b"))

# 1010
# 0110
# ======
# 0010
# ======

print("AND result ",end=str(a & b))

#%% print bitwise right shift operation
a = 10
print(a >> 2)

# a = 10      #  1010
# x = a >> 2  #  0010
# print(x)    #  2
#             #  0010

print(format(2, "b"))
print(int('0010',2))

#%% print bitwise left shift operation
print(a << 2)

# a = 10      #  1010
# x = a << 2  #  101000
# print(x)    #  40
#             #  101000

