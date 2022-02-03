# Python Assignment Operators
# ==============================

#%% =	
x = 5
print(x)

#%% +=	  
x += 3
# x = x + 3   
print(x)

#%% -=   
x -= 3
# x = x - 3   
print(x)

#%% *=		
x *= 3
# x = x * 3     
print(x)

#%% /=	
x /= 3	
# x = x / 3 
print(x)

#%% %=		
x %= 3
# x = x % 3
print(x)

#%% //=
x = 5
x //= 3	
# x = x // 3	
print(x)

#%% **=	
x = 5

x **= 3
# x = x ** 3	

print(x)

'''
Come back to this after we cover BitWise Operators
'''

#%% &=			AND : Sets each bit to 1 if both bits are 1
print(format(5, "b"))
print(format(3, "b"))
'''
101
011
=====
001
=====
'''

x = 5
x &= 3
# x = x & 3
print(x)
print(format(1, "b"))

#%% |= 			OR : Sets each bit to 1 if one of two bits is 1
print(format(5, "b"))
print(format(3, "b"))
'''
101
011
=====
111
=====
'''

x = 5
x |= 3
# x = x | 3
print(x)
print(format(7, "b"))


#%% ^=	    XOR : Sets each bit to 1 if only one of two bits is 1
print(format(5, "b"))
print(format(3, "b"))
'''
101
011
=====
110
=====
'''

x = 5
x ^= 3
# x = x ^ 3
print(x)
print(format(6, "b"))

#%% ~   NOT : Inverts all the bits
print(format(5, "b"))
x = 5  # 101 in binary
x = ~x # -x-1 = -(101+1) = -(110) = -6
print(x)

print(int('110',2))

#%% <<=	  	Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
# Shift left by pushing zeros in from the right

x = 170  #  10101010
x <<= 1  #  101010100
print(x) #  340
         #  101010100

print(format(340, "b"))
print(int('101010100',2))

#%% >>=	    Returns x with the bits shifted to the right by y places. 
# Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

x = 170  #  10101010
x >>= 1  #  01010101
print(x) #  85
         #  01010101

print(format(85, "b"))
print(int('01010101',2))

