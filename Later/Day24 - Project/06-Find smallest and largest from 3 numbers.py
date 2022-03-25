#%% Task01 - Take input and find the Largest and Smallest of Three Numbers

'''
Input
==========
a = 1
b = 2
c = 3

Output
==========
max is 3
min is 1

Input
==========
a = 3
b = 2
c = 1

Output
==========
max is 3
min is 1

'''

#%% Solution 01 - Find the Largest and Smallest of Three Numbers

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

def largest(a, b, c):
    max = a
    if b > max:
      max = b
    if c > max:
      max = c
    return max

def smallest(a, b, c):
    min = a
    if b < min:
      min = b
    if c < min:
      min = c
    return min

max = largest(a, b, c)
min = smallest(a, b, c)

print(f"max is {max}")
print(f"min is {min}")

