# Python Comparison Operators
# ==============================

'''
==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
'''
#%% 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# %%
x = 5
y = 3

print(x == y)

# %%
x = 5
y = 5

print(x == y)
# %%
x = 'Hello'
y = 'Hello'

print(x == y)

#%% Task : Take two inputs and check compare it with each other and output the results

x = input("Enter a number: ")
y = input("Enter another number: ")

if x==y:
    print("x and y are equal")

elif x>y:
    print("x is greater than y")

elif x<y:
    print("x is less than y")
