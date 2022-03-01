# Python Identity Operators : Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# ==============================

#%%
x = 3
y = 31

print(x is y)
print(x is not y)

print(f"Memory location of x is {id(x)}")
print(f"Memory location of y is {id(y)}")

