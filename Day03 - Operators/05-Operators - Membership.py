# Membership operators are used to test if a sequence is presented in an object:

'''
in 	    :   Returns True if a sequence with the specified value is present in the object		
not in	:   Returns True if a sequence with the specified value is not present in the object

'''
#%% 
x = ["apple", "banana"]

print("banana" in x)
print("pineapple" in x)

print("banana" not in x)
print("pineapple" not in x)

# %%
y = [1,2,4,0]

print(1 in y)
print(3 in y)

print(1 not in y)
print(3 not in y)
