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


#%% Task: Check if fruit exists in your list or not

fruit = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi", "lemon", "lime", "mango", "nectarine", "orange", "papaya", "peach", "pear", "pineapple", "plum", "pomegranate", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

x = input("Enter a Fruit: ")

if x in fruit:
    print("Yes, I have that fruit")

elif x not in fruit:
    print("No, I don't have that fruit")
