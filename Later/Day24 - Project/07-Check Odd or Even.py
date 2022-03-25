#%% Check if a Given Integer is Odd or Even 

# Method 1: Brute Force Naive Approach

def Method1_IsOddOrEven(myNumber):
    if myNumber%2 == 0:
        return "Even"
    else:
        return "Odd"

print(Method1_IsOddOrEven(41))
print(Method1_IsOddOrEven(4))

# Method 2: Using bitwise operators
# Bitwise OR
def Method2_OR_IsOddOrEven(myNumber):
    if myNumber | 1 > myNumber:
        return "Even"
    else:
        return "Odd"

print(Method2_OR_IsOddOrEven(41))
print(Method2_OR_IsOddOrEven(4))

# Bitwise AND
def Method2_AND_IsOddOrEven(myNumber):
    if myNumber & 1 == 0:
        return "Even"
    else:
        return "Odd"

print(Method2_AND_IsOddOrEven(41))
print(Method2_AND_IsOddOrEven(4))

# Bitwise XOR
def Method2_XOR_IsOddOrEven(myNumber):
    if myNumber ^ 1 == myNumber + 1:
        return "Even"
    else:
        return "Odd"

print(Method2_XOR_IsOddOrEven(41))
print(Method2_XOR_IsOddOrEven(4))

#%% Method 3

x = []
print(type(x))

# %%
